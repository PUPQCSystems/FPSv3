from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from ranking.models import FacultyRankEvaluations
from django.http import JsonResponse

@login_required(login_url='login')
def manangement_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'management.html', context)

def GET_rankingtable(request):
    ranking_data = FacultyRankEvaluations.objects.select_related('faculty').all() \
        .filter(faculty__faculty_type='Regular') 
    serialized_data = []
    for item in ranking_data:
        serialized_data.append({
            'faculty_name': item.faculty.faculty_name,
            'evaluations': item.kra_one_pts,
            'researchpapers': item.kra_two_pts,
            'prodev': item.kra_three_pts,
            'extension': item.kra_four_pts,
            'grandtotal': item.grandtotal_score,
            'bracketcount': item.rank_bracket_count,
            'oldrank': item.current_rank,
            'newrank': item.new_rank,
            'assessment': item.impression,
            'evaldate': item.rank_eval_date.strftime('%b. %d, %Y') if item.rank_eval_date else 0
        })
    return JsonResponse({'data':serialized_data})