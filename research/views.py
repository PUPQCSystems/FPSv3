from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from .models import PaperCounts
from django.http import JsonResponse
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime

@login_required(login_url='login')
def research_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    categories   = ax_research_peryear(request)
    total_categs = ax_research_counts(request)
    output_types = ax_research_outputs(request)
    title_series = ax_research_series(request)
    card_thisyr  = card_research_thisyear(request)
    card_ongoing = card_research_ongoing(request)

    context = {
        'requestz': serialized_state,
        "categories": categories,
        "series": total_categs,
        "research_types": output_types,
        "research_series": title_series,
        "papers_this_year": card_thisyr,
        "papers_ongoings" : card_ongoing
    }
    return render(request, 'research.html', context)
    # return JsonResponse(context, safe=False)


@login_required(login_url='login')
def research_table_view(request):
    research = PaperCounts.objects.select_related('author').all()
    serialized_data = []
    for item in research:
        serialized_data.append({
            'author': item.author.faculty_name,
            'research_paper': item.title,
            'research_type': item.output_type,
            'publisher': item.journal_publisher,
            'status': item.status,
            'date_published': item.date_published,
            'year_published': item.year_published,
            'performance_score': item.research_performance_score
        })
    return JsonResponse({'data': serialized_data})


@login_required(login_url='login')
def ax_research_peryear(request):
    publication_data = PaperCounts.objects                                                  \
                            .values('year_published')                                       \
                            .annotate(total=Count('research_id'))                           \
                            .order_by('year_published')
    return json.dumps([entry['year_published'] for entry in publication_data], cls=DjangoJSONEncoder)


@login_required(login_url='login')
def ax_research_counts(request):
    publication_data = PaperCounts.objects                                                  \
                            .filter(status='Published')                                     \
                            .values('year_published')                                       \
                            .annotate(total=Count('research_id'))                           \
                            .order_by('year_published')
    return json.dumps([entry['total'] for entry in publication_data], cls=DjangoJSONEncoder)


@login_required(login_url='login')
def ax_research_outputs(request):
    research_types_data = PaperCounts.objects                                               \
                            .values('output_type')                                          \
                            .annotate(total=Count('research_id'))                           \
                            .order_by('output_type')
    return json.dumps([entry['output_type'] for entry in research_types_data], cls=DjangoJSONEncoder)


@login_required(login_url='login')
def ax_research_series(request):
    research_types_data = PaperCounts.objects                                               \
                            .values('output_type')                                          \
                            .annotate(total=Count('research_id'))                           \
                            .order_by('output_type')
    return json.dumps([entry['total'] for entry in research_types_data], cls=DjangoJSONEncoder)


@login_required(login_url='login')
def card_research_thisyear(request):
    current_year = datetime.now().year
    papers_this_year = PaperCounts.objects                                                  \
                            .filter(year_published=str(current_year), status='Published')   \
                            .count()
    return papers_this_year


@login_required(login_url='login')
def card_research_ongoing(request):
    current_year = datetime.now().year
    ongoing_papers = PaperCounts.objects                                                    \
                            .filter(year_published=str(current_year), status='Ongoing')     \
                            .count()
    return ongoing_papers