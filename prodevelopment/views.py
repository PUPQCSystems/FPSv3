from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from .models import ContinuingDevelopment
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Func, F, Value, CharField
from django.db.models.functions import Substr

@login_required(login_url='login')
def prodev_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    participants_pryr = ax_prodev_peryear(request)
    international_count = ax_prodev_scope_intl(request)
    local_count = ax_prodev_scope_local(request)
    context = {
        'requestz' : serialized_state , 
        'participants_per_year': participants_pryr,
        'international_count' : international_count,
        'local_count' : local_count,
    }
    return render(request, 'prodev.html', context)
    #return JsonResponse(context, safe=False)


@login_required(login_url='login')
def prodev_tableviews(request):
    participants = ContinuingDevelopment.objects.select_related('participant').all()
    serialized_data = []
    for item in participants:
        serialized_data.append({
            'participants': item.participant.faculty_name,
            'training': item.event,
            'organizer': item.organizer,
            'hours': item.hrs_accumulated,
            'scope': item.scope,
            'event_date': item.event_date,
            'performance_score': item.prodev_performance_score
        })
    return JsonResponse({'data': serialized_data})


@login_required(login_url='login')
def ax_prodev_peryear(request):
    prodev_data = ContinuingDevelopment.objects \
        .values('event_date') \
        .annotate(total_events=Count('prodev_id')) \
        .order_by('event_date')
    year_events = {}
    for entry in prodev_data:
        year = entry['event_date'][-4:]
        if year in year_events:
            year_events[year] += entry['total_events']
        else:
            year_events[year] = entry['total_events']
    sorted_year_events = dict(sorted(year_events.items()))
    return json.dumps(
        [{'year': year, 'total_events': total_events} for year, total_events in sorted_year_events.items()],
        cls=DjangoJSONEncoder
    )   
    # return json.dumps(
    #     #[{'year': year, 'total_events': total_events} for year, total_events in year_events.items()],
    #     # [{'year': year} for year in year_events.items()],
    #     #[{'total_events': total_events} for total_events in year_events.items()],
    #     cls=DjangoJSONEncoder
    # )   


@login_required(login_url='login')
def ax_prodev_scope_intl(request):
    intl_count = ContinuingDevelopment.objects.filter(scope='International').count()
    local_count = ContinuingDevelopment.objects.filter(scope='Local').count()
    total_count = intl_count + local_count
    intl_percentage = (intl_count / total_count) * 100 if total_count > 0 else 0
    return json.dumps(intl_percentage,cls=DjangoJSONEncoder)


@login_required(login_url='login')
def ax_prodev_scope_local(request):
    intl_count = ContinuingDevelopment.objects.filter(scope='International').count()
    local_count = ContinuingDevelopment.objects.filter(scope='Local').count()
    total_count = intl_count + local_count
    local_percentage = (local_count / total_count) * 100 if total_count > 0 else 0
    return json.dumps(local_percentage,cls=DjangoJSONEncoder)