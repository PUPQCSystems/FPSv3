from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TeachingEffectiveness
import json
from django.http import JsonResponse
from django.db.models import Avg, ExpressionWrapper, F, DecimalField
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


# @login_required(login_url='login')
# def eval_table_view(request):
#     evaluations = TeachingEffectiveness.objects.select_related('faculty').all()
#     serialized_data = []
#     for item in evaluations:
#         serialized_data.append({
#             'faculty': item.faculty.faculty_name,
#             'semester': item.semesters,
#             'academic_year': item.academic_yr,
#             'average_rating': item.average_rate,
#             'interpretation': item.ar_interpretation,
#             'performance_score': item.eval_performance_score,
#             'student_rating': item.student_rate,
#             'student_interpretation': item.sr_interpretation,
#             'supervisor_rating': item.supervisor_rate,
#             'supervisor_interpretation': item.sp_interpretation
#         })
#     return JsonResponse({'data': serialized_data})


# @login_required(login_url='login')
# def eval_table_view(request):
#     evaluations = TeachingEffectiveness.objects.select_related('faculty')
#     serialized_data = []
#     for item in evaluations:
#         # Compute average_rating
#         average_rating = float(item.average_rate) * 0.6
        
#         # Compute performance_score
#         performance_score = (average_rating / 10) * 100
        
#         # Compute overall_ave_student_rating
#         overall_ave_student_rating = float(item.student_rate) * 0.36
        
#         # Compute student_interpretation
#         # student_interpretation = ''
#         # if 1.00 <= overall_ave_student_rating <= 1.99:
#         #     student_interpretation = 'Poor'
#         # elif 2.00 <= overall_ave_student_rating <= 2.99:
#         #     student_interpretation = 'Fair'
#         # elif 3.00 <= overall_ave_student_rating <= 3.99:
#         #     student_interpretation = 'Satisfactory'
#         # elif 4.00 <= overall_ave_student_rating <= 4.99:
#         #     student_interpretation = 'Very Satisfactory'
#         # else:
#         #     student_interpretation = 'Outstanding'
        
#         # Compute overall_ave_supervisor_rating
#         overall_ave_supervisor_rating = float(item.supervisor_rate) * 0.24
        
#         # Compute supervisor_interpretation
#         # supervisor_interpretation = ''
#         # if 1.00 <= overall_ave_supervisor_rating <= 1.99:
#         #     supervisor_interpretation = 'Poor'
#         # elif 2.00 <= overall_ave_supervisor_rating <= 2.99:
#         #     supervisor_interpretation = 'Fair'
#         # elif 3.00 <= overall_ave_supervisor_rating <= 3.99:
#         #     supervisor_interpretation = 'Satisfactory'
#         # elif 4.00 <= overall_ave_supervisor_rating <= 4.99:
#         #     supervisor_interpretation = 'Very Satisfactory'
#         # else:
#         #     supervisor_interpretation = 'Outstanding'
        
#         # Append computed values to serialized_data
#         serialized_data.append({
#             'faculty': item.faculty.faculty_name,
#             'average_rating': round(average_rating,2),
#             'performance_score': round(performance_score,2),
#             'overall_ave_student_rating': round(overall_ave_student_rating,2),
#             # 'student_interpretation': student_interpretation,
#             'overall_ave_supervisor_rating': round(overall_ave_supervisor_rating,2),
#             # 'supervisor_interpretation': supervisor_interpretation
#         })
#     return JsonResponse({'data': serialized_data})


@login_required(login_url='login')
def eval_table_view(request):
    # Group evaluations by faculty and compute averages
    evaluations = TeachingEffectiveness.objects.values('faculty__faculty_name').annotate(
        # average_rating=ExpressionWrapper(Avg(F('average_rate')) * 0.6, output_field=DecimalField()),
        overall_ave_student_rating=ExpressionWrapper(Avg(F('student_rate')), output_field=DecimalField()),
        overall_ave_supervisor_rating=ExpressionWrapper(Avg(F('supervisor_rate')), output_field=DecimalField()),
    )

    serialized_data = []
    for item in evaluations:
        serialized_data.append({
            'faculty': item['faculty__faculty_name'],
            # 'average_rating': round(float(item['average_rating']), 2),
            'overall_ave_student_rating': round(float(item['overall_ave_student_rating']), 2),
            'overall_ave_supervisor_rating': round(float(item['overall_ave_supervisor_rating']), 2),
            
            'sr_perf': round(float(float(item['overall_ave_student_rating'] /5) * 100), 2),
            'sp_perf': round(float(float(item['overall_ave_supervisor_rating'] /5) *100), 2),
            
            # 'performance_score': round((float(item['average_rating']) / 10) * 100, 2),
            'performance_score': round(round(float(float(item['overall_ave_student_rating'] /5) * 100) *0.36, 2) + round(float(float(item['overall_ave_supervisor_rating'] /5) *100) * 0.24, 2),2)
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