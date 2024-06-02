from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def research_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'research.html', context)