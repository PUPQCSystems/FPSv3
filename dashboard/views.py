from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from evaluations.views import average_student_rate, average_spvisor_rate
from research.views import card_research_thisyear, card_research_ongoing
from prodevelopment.views import ax_prodev_scope_intl, ax_prodev_scope_local
from extensionservices.views import ax_extension_head, ax_extension_participant

@login_required(login_url='login')
def dashboard_module(request):
    state = 'active'
    serialized_state = json.dumps(state)
    student_analytics = average_student_rate(request)
    spvisor_analytics = average_spvisor_rate(request)
    card_thisyr  = card_research_thisyear(request)
    card_ongoing = card_research_ongoing(request)
    international_count = ax_prodev_scope_intl(request)
    local_count = ax_prodev_scope_local(request)
    head_counts = ax_extension_head(request)
    participant_counts = ax_extension_participant(request)
    context = {
        'requestz' : serialized_state ,
        'ave_sr_rate': student_analytics,
        'ave_sp_rate': spvisor_analytics, 
        "papers_this_year": card_thisyr,
        "papers_ongoings" : card_ongoing,
        'international_count' : international_count,
        'local_count' : local_count,
        'head_counts': head_counts,
        'participant_counts' : participant_counts , 
    }
    return render(request, 'dashboard.html', context)