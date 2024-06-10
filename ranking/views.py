from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

from .models import FacultyRankEvaluations
from extensionservices.models import ServiceToTheCommunity
from prodevelopment.models import ContinuingDevelopment
from evaluations.models import TeachingEffectiveness
from research.models import PaperCounts
from accounts.models import Faculty

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Count, Avg
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils import timezone



def faculty_ranks_list():
    return [
        ('Instructor I', 1),
        ('Instructor II', 1),
        ('Instructor III', 1),
        ('Assistant Professor I', 1),
        ('Assistant Professor II', 1),
        ('Assistant Professor III', 1),
        ('Assistant Professor IV', 1),
        ('Associate Professor I', 1),
        ('Associate Professor II', 1),
        ('Associate Professor III', 1),
        ('Associate Professor IV', 1),
        ('Associate Professor V', 1),
        ('Professor I', 1),
        ('Professor II', 1),
        ('Professor III', 1),
        ('Professor IV', 1),
        ('Professor V', 1),
        ('Professor VI', 1),
        ('University Professor', 1),
    ]


def get_rank_index(faculty_rank):
    ranks = faculty_ranks_list()
    for index, (rank, _) in enumerate(ranks):
        if rank == faculty_rank:
            return index
    return None


def points_bracket(points):
    points_brackets = [
        (41, 50, 1),
        (51, 60, 2),
        (61, 70, 3),
        (71, 80, 4),
        (81, 90, 5),
        (91, 100, 6)
    ]
    for bracket in points_brackets:
        if bracket[0] <= points <= bracket[1]:
            return bracket[2]
    if points < 41:
        return 0
    return None


def compute_total(points):
    sub_rank_increment = points_bracket(points)
    return sub_rank_increment


def kra_one_teachingeffectiveness(faculty_rank):
    if 'Instructor' in faculty_rank:
        return 0.60
    elif 'Assistant Professor' in faculty_rank:
        return 0.50
    elif 'Associate Professor' in faculty_rank:
        return 0.40
    elif 'Professor' in faculty_rank:
        return 0.30
    elif 'University Professor' in faculty_rank:
        return 0.20
    else:
        return 0 


def kra_two_researchpublications(faculty_rank):
    if 'Instructor' in faculty_rank:
        return 0.10
    elif 'Assistant Professor' in faculty_rank:
        return 0.20
    elif 'Associate Professor' in faculty_rank:
        return 0.30
    elif 'Professor' in faculty_rank:
        return 0.40
    elif 'University Professor' in faculty_rank:
        return 0.50
    else:
        return 0 


def kra_three_professionaldevelopment(faculty_rank):
    return 0.20


def kra_four_extensionservices(faculty_rank):
    return 0.10


def compute_new_rank(current_faculty_rank, kra_one_score, kra_two_score, kra_three_score, kra_four_score):
    percentage1 = kra_one_teachingeffectiveness(current_faculty_rank)
    percentage2 = kra_two_researchpublications(current_faculty_rank)
    percentage3 = kra_three_professionaldevelopment(current_faculty_rank)
    percentage4 = kra_four_extensionservices(current_faculty_rank)
    final_points_for_kra_teaching = kra_one_score * percentage1
    final_points_for_kra_research = kra_two_score * percentage2
    final_points_for_kra_prodevlp = kra_three_score * percentage3
    final_points_for_kra_extservc = kra_four_score * percentage4
    total_points = round((final_points_for_kra_teaching + 
                    final_points_for_kra_research + 
                    final_points_for_kra_prodevlp + 
                    final_points_for_kra_extservc),0)
    ranks = faculty_ranks_list()
    rank_index = get_rank_index(current_faculty_rank)
    if rank_index is not None:
        result = compute_total(total_points)
        if result is not None:
            new_rank_index = rank_index + result
            if new_rank_index >= len(ranks):
                new_rank_index = len(ranks) - 1
            new_rank = ranks[new_rank_index][0]
            impression = 'Promoted' if result > 0 else 'Retained'
            return new_rank, total_points, result, impression
        else:
            result = 0
            impression = 'Retained'
            return current_faculty_rank, total_points, result, impression
    else:
        na_newrank = 'Reclassified rank is not yet applicable'
        na_pts_score = 'Score not yet applicable'
        na_increm = 'Sub-rank increment is not yet applicable'
        na_impres = 'Retained'
        return na_newrank, na_pts_score, na_increm, na_impres


def kra_1(request):
    semesters = ['First', 'Second']
    faculty_name = get_facultyname(request)
    academic_year = '2023-2024'
    faculty_evaluations = TeachingEffectiveness.objects.select_related('faculty') \
        .filter(faculty__faculty_name=faculty_name, semesters__in=semesters, academic_yr=academic_year)
    total_score = sum(float(eval_score.eval_performance_score) for eval_score in faculty_evaluations)
    average_score = total_score / len(faculty_evaluations) if faculty_evaluations else 0
    final_score = round(average_score, 2)
    return final_score


def kra_2(request):
    status = 'Published'
    facultyname = get_facultyname(request)
    research_counts = PaperCounts.objects.select_related('author')\
        .filter(author__faculty_name=facultyname, status=status)
    total_score = sum(research_pts.research_performance_score for research_pts in research_counts)
    average_score = total_score / len(research_counts) if research_counts else 0
    rounded_average = round(average_score,2)
    return rounded_average


def kra_3(request):
    facultyname = get_facultyname(request)
    prodev_counts = ContinuingDevelopment.objects.select_related('participant') \
        .filter(participant__faculty_name=facultyname)
    total_score = sum(prodev_pts.prodev_performance_score for prodev_pts in prodev_counts)
    average_score = total_score / len(prodev_counts) if prodev_counts else 0
    rounded_average = round(average_score,2)
    return rounded_average


def kra_4(request):
    facultyname = get_facultyname(request)
    extension_counts = ServiceToTheCommunity.objects.select_related('ext_faculty') \
        .filter(ext_faculty__faculty_name=facultyname)
    total_score = sum(extension_pts.extension_performance_score for extension_pts in extension_counts)
    average_score = total_score / len(extension_counts) if extension_counts else 0
    rounded_average = round(average_score,2)
    return rounded_average


def get_faculty_rank(faculty_name):
    try:
        faculty = Faculty.objects.get(faculty_name=faculty_name)
        return faculty.faculty_rank
    except Faculty.DoesNotExist:
        return None


def get_facultyname(request):
    faculty_name = request.POST.get('faculty_name')
    return faculty_name


@login_required(login_url='login')
@csrf_exempt
@require_POST
def POST_facultyname(request):
    faculty_name = get_facultyname(request)
    if faculty_name:
        return JsonResponse({'status': 'success', 'faculty_name': faculty_name})
    else:
        return JsonResponse({'status': 'error', 'message': 'Faculty name not provided'}, status=400)


@login_required(login_url='login')
def GET_facultynewrank(request):
    faculty_name = get_facultyname(request)
    current_faculty_rank = get_faculty_rank(faculty_name)
    if current_faculty_rank is None:
        return JsonResponse({'status': 'error', 'message': 'Faculty not found'}, status=404)
    kra_one_score = kra_1(request)
    kra_two_score = kra_2(request)
    kra_three_score = kra_3(request)
    kra_four_score = kra_4(request)
    kra1 = kra_1(request)
    kra2 = kra_2(request)
    kra3 = kra_3(request)
    kra4 = kra_4(request)
    new_rank, total_points, rank_increment, impression = compute_new_rank(current_faculty_rank, kra_one_score, kra_two_score, kra_three_score, kra_four_score)
    reclassified = {
        'faculty_name': faculty_name,
        'current_faculty_rank': current_faculty_rank,
        'kra1' : kra1,
        'kra2' : kra2,
        'kra3' : kra3,
        'kra4' : kra4,
        'total_points': total_points,
        'rank_increment': rank_increment,
        'new_rank': new_rank,
        'impression': impression ,
    }
    return JsonResponse(reclassified, safe=False)


@login_required(login_url='login')
def ranking_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state ,
    }
    return render(request, 'ranking.html', context)


@login_required(login_url='login')
def ranking_tableview(request):
    ranking_data = Faculty.objects.all() \
        .filter(faculty_type='Regular') 
    serialized_data = []
    for item in ranking_data:
        serialized_data.append({
            'faculty_name': item.faculty_name,
            'faculty_type': item.faculty_type,
            'faculty_rank': item.faculty_rank,
        })
    return JsonResponse({'data':serialized_data})


def POST_rankingtable(request):
    if request.method == 'POST':
        facultyname = request.POST.get('faculty_name')
        new_rank = request.POST.get('new_rank')
        impression = request.POST.get('impression')
        current_rank = request.POST.get('current_rank')
        rank_increment = request.POST.get('rank_increment')
        kra1 = request.POST.get('kra1')
        kra2 = request.POST.get('kra2')
        kra3 = request.POST.get('kra3')
        kra4 = request.POST.get('kra4')
        total_points = request.POST.get('total_points')
        try:
            faculty = Faculty.objects.get(faculty_name=facultyname)
        except Faculty.DoesNotExist:
            return HttpResponse("Faculty not found.", status=404)
        evaluation = FacultyRankEvaluations(
            faculty=faculty,
            current_rank=current_rank,
            kra_one_pts=kra1,
            kra_two_pts=kra2,
            kra_three_pts=kra3,
            kra_four_pts=kra4,
            grandtotal_score=total_points,
            rank_bracket_count=rank_increment,
            new_rank=new_rank,
            impression=impression,
            rank_eval_date=timezone.now()
        )
        evaluation.save()
        return HttpResponse("Form submitted and data saved successfully.")
    return render(request, 'ranking.html')
