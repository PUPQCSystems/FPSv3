from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from .models import ServiceToTheCommunity
from django.http import JsonResponse
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder


@login_required(login_url='login')
def extension_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    ext_counts = ax_extension_peryear(request)
    head_counts = ax_extension_head(request)
    participant_counts = ax_extension_participant(request)
    context = {
        'extension_counts': ext_counts, 
        'head_counts': head_counts,
        'participant_counts' : participant_counts , 
        'requestz' : serialized_state ,
    }
    return render(request, 'extensionservices.html', context)
    #return JsonResponse(context, safe=False)


@login_required(login_url='login')
def extension_tableviews(request):
    participants = ServiceToTheCommunity.objects.select_related('ext_faculty').all()
    serialized_data = []
    for item in participants:
        serialized_data.append({
            'participants': item.ext_faculty.faculty_name,
            'activity': item.activity,
            'community': item.community,
            'role': item.role,
            'date': item.date_of_activity,
            'hours': item.hours_completed,
            'performance_score': item.extension_performance_score
        })
    return JsonResponse({'data': serialized_data})


def ax_extension_peryear(request):
    extensions_data = ServiceToTheCommunity.objects \
        .values('date_of_activity') \
        .annotate(total_events=Count('extension_id')) \
        .order_by('date_of_activity')
    year_events = {}
    for entry in extensions_data:
        year = entry['date_of_activity'][-4:]
        if year in year_events:
            year_events[year] += entry['total_events']
        else:
            year_events[year] = entry['total_events']
    sorted_year_events = dict(sorted(year_events.items()))
    return json.dumps(
        [{'year': year, 'total_events': total_events} for year, total_events in sorted_year_events.items()],
        cls=DjangoJSONEncoder
    )   


@login_required(login_url='login')
def ax_extension_head(request):
    ext_head_count = ServiceToTheCommunity.objects.filter(role='Head').count()
    ext_memb_count = ServiceToTheCommunity.objects.filter(role='Participant').count()
    total_count = ext_head_count + ext_memb_count
    head_percentage = (ext_head_count / total_count) * 100 if total_count > 0 else 0
    head_percentage = round(head_percentage, 2)
    return json.dumps(head_percentage,cls=DjangoJSONEncoder)


@login_required(login_url='login')
def ax_extension_participant(request):
    ext_head_count = ServiceToTheCommunity.objects.filter(role='Head').count()
    ext_memb_count = ServiceToTheCommunity.objects.filter(role='Participant').count()
    total_count = ext_head_count + ext_memb_count
    participant_percentage = (ext_memb_count / total_count) * 100 if total_count > 0 else 0
    participant_percentage = round(participant_percentage, 2)
    return json.dumps(participant_percentage,cls=DjangoJSONEncoder)