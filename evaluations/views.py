from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TeachingEffectiveness
import json
from django.http import JsonResponse
from django.db.models import Avg
from django.core.serializers.json import DjangoJSONEncoder


@login_required(login_url='login')
def evaluations_view(request):
    state = 'active'
    serialized_state = json.dumps(state)
    student_analytics = average_student_rate(request)
    spvisor_analytics = average_spvisor_rate(request)
    context = {
        'ave_sr_rate': student_analytics,
        'ave_sp_rate': spvisor_analytics,
        'requestz' : serialized_state , 
    }
    return render(request, 'evaluations.html', context)
    # return JsonResponse(context, safe=False)


@login_required(login_url='login')
def eval_table_view(request):
    evaluations = TeachingEffectiveness.objects.select_related('faculty').all()
    serialized_data = []
    for item in evaluations:
        serialized_data.append({
            'faculty': item.faculty.faculty_name,
            'semester': item.semesters,
            'academic_year': item.academic_yr,
            'average_rating': item.average_rate,
            'interpretation': item.ar_interpretation,
            'performance_score': item.eval_performance_score,
            'student_rating': item.student_rate,
            'student_interpretation': item.sr_interpretation,
            'supervisor_rating': item.supervisor_rate,
            'supervisor_interpretation': item.sp_interpretation
        })
    return JsonResponse({'data': serialized_data})


@login_required(login_url='login')
def average_student_rate(request):
    aggregated_data = TeachingEffectiveness.objects.values('academic_yr', 'semesters').annotate(average_student_rating=Avg('student_rate'))
    
    result = {
        'First': {},
        'Second': {}
    }
    for item in aggregated_data:
        academic_year = item['academic_yr']
        semester = item['semesters']
        avg_rating = round(float(item['average_student_rating']), 2)
        if semester == 'First':
            result['First'][academic_year] = avg_rating
        elif semester == 'Second':
            result['Second'][academic_year] = avg_rating
    all_academic_years = sorted(set(result['First'].keys()).union(set(result['Second'].keys())))
    serialized_data = {
        'academic_years': all_academic_years,
        'first_semester_ratings': [result['First'].get(year, 0) for year in all_academic_years],
        'second_semester_ratings': [result['Second'].get(year, 0) for year in all_academic_years]
    }
    return json.dumps(serialized_data, cls=DjangoJSONEncoder)


@login_required(login_url='login')
def average_spvisor_rate(request):
    aggregated_data = TeachingEffectiveness.objects.values('academic_yr', 'semesters').annotate(average_svisor_rating=Avg('supervisor_rate'))
    
    result = {
        'First': {},
        'Second': {}
    }
    for item in aggregated_data:
        academic_year = item['academic_yr']
        semester = item['semesters']
        avg_rating = round(float(item['average_svisor_rating']), 2)
        if semester == 'First':
            result['First'][academic_year] = avg_rating
        elif semester == 'Second':
            result['Second'][academic_year] = avg_rating
    all_academic_years = sorted(set(result['First'].keys()).union(set(result['Second'].keys())))
    serialized_data = {
        'academic_years': all_academic_years,
        'first_semester_ratings': [result['First'].get(year, 0) for year in all_academic_years],
        'second_semester_ratings': [result['Second'].get(year, 0) for year in all_academic_years]
    }
    return json.dumps(serialized_data, cls=DjangoJSONEncoder)