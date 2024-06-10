from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from ranking.models import FacultyRankEvaluations
from accounts.models import Faculty
from django.http import JsonResponse, HttpResponse
import io
import xlsxwriter


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

def POST_export(request):
    if request.method == 'POST':
        faculty_name = request.POST.get('faculty_name')
        rankingtable = FacultyRankEvaluations.objects.filter(faculty__faculty_name=faculty_name).first()
        if rankingtable:
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()

            bold = workbook.add_format({'bold': True})
            cent = workbook.add_format({'align': 'center'})
            bordx1 = workbook.add_format({'border': 1})
            bordbn = workbook.add_format({'border': 1, 'align': 'center'})
            bordn = workbook.add_format({'border': 1, 'italic': True})
            bordbcn = workbook.add_format({'border': 1, 'align': 'center', 'bold': True})
            bordwbc = workbook.add_format({'border': 1, 'align': 'center', 'bold': True, 'valign': 'vcenter'})
            bordwrp = workbook.add_format({'border': 1, 'bold': True, 'text_wrap': True})

            worksheet.write('A1', 'A. INDIVIDUAL PERFORMANCE COMMITMENT REVIEW (IPCR)', bold)
            worksheet.write('A3', 'I, _______________________________________ of the __________________________________, commit to deliver and agree to be rated on the attainment of')
            worksheet.write('A4', 'the following Targets in accordance with the indicated measures for the period of _________________________.')
            worksheet.merge_range('J8:M8', 'Rate', cent)
            worksheet.write('J9', 'Date:', cent)
            worksheet.write('A10', 'Reviewed by:')
            worksheet.write('I10', 'Approved by:')
            worksheet.merge_range('A11:F11', ' ', bordx1)
            worksheet.merge_range('G11:H11', 'Date', bordx1)
            worksheet.merge_range('I11:N11', ' ', bordx1)
            worksheet.merge_range('O11:P11', 'Date', bordx1)
            worksheet.merge_range('A12:F13', ' ', bordx1)
            worksheet.merge_range('G12:H14', ' ', bordx1)
            worksheet.merge_range('I12:N13', ' ', bordx1)
            worksheet.merge_range('O12:P14', ' ', bordx1)
            worksheet.merge_range('A14:F14', 'Immediate Supervisor', bordwbc)
            worksheet.merge_range('I14:N14', 'Head of Office', bordwbc)
            worksheet.merge_range('A16:D17', 'OUTPUT', bordwbc)
            worksheet.merge_range('E16:I16', 'SUCCESS INDICATORS', bordwbc)
            worksheet.merge_range('J16:M17', 'ACTUAL ACCOMPLISHMENTS', bordwbc)
            worksheet.merge_range('N16:Q16', 'RATING', bordwbc)
            worksheet.merge_range('R16:T17', 'REMARKS', bordwbc)
            worksheet.merge_range('E17:I17', '(TARGETS+MEASURES)', bordwbc)
            worksheet.write('N17', 'Q1', bordwbc)
            worksheet.write('O17', 'E2', bordwbc)
            worksheet.write('P17', 'T3', bordwbc)
            worksheet.write('Q17', 'A4', bordwbc)
            worksheet.merge_range('A18:D18', ' ', bordx1)
            worksheet.merge_range('E18:I18', ' ', bordx1)
            worksheet.merge_range('J18:M18', ' ', bordx1)
            worksheet.write('N18', ' ', bordx1)
            worksheet.write('O18', ' ', bordx1)
            worksheet.write('P18', ' ', bordx1)
            worksheet.write('Q18', ' ', bordx1)
            worksheet.merge_range('A19:D19', ' ', bordx1)
            worksheet.merge_range('E19:I19', ' ', bordx1)
            worksheet.merge_range('J19:M19', ' ', bordx1)
            worksheet.write('N19', ' ', bordx1)
            worksheet.write('O19', ' ', bordx1)
            worksheet.write('P19', ' ', bordx1)
            worksheet.write('Q19', ' ', bordx1)
            worksheet.merge_range('A20:D20', ' ', bordx1)
            worksheet.merge_range('E20:I20', ' ', bordx1)
            worksheet.merge_range('J20:M20', ' ', bordx1)
            worksheet.write('N20', ' ', bordx1)
            worksheet.write('O20', ' ', bordx1)
            worksheet.write('P20', ' ', bordx1)
            worksheet.write('Q20', ' ', bordx1)
            worksheet.merge_range('A21:D21', ' ', bordx1)
            worksheet.merge_range('E21:I21', ' ', bordx1)
            worksheet.merge_range('J21:M21', ' ', bordx1)
            worksheet.write('N21', ' ', bordx1)
            worksheet.write('O21', ' ', bordx1)
            worksheet.write('P21', ' ', bordx1)
            worksheet.write('Q21', ' ', bordx1)
            worksheet.merge_range('A22:D22', ' ', bordx1)
            worksheet.merge_range('E22:I22', ' ', bordx1)
            worksheet.merge_range('J22:M22', ' ', bordx1)
            worksheet.write('N22', ' ', bordx1)
            worksheet.write('O22', ' ', bordx1)
            worksheet.write('P22', ' ', bordx1)
            worksheet.write('Q22', ' ', bordx1)
            worksheet.merge_range('A23:D23', ' ', bordx1)
            worksheet.merge_range('E23:I23', ' ', bordx1)
            worksheet.merge_range('J23:M23', ' ', bordx1)
            worksheet.write('N23', ' ', bordx1)
            worksheet.write('O23', ' ', bordx1)
            worksheet.write('P23', ' ', bordx1)
            worksheet.write('Q23', ' ', bordx1)
            worksheet.merge_range('A24:D24', ' ', bordx1)
            worksheet.merge_range('E24:I24', ' ', bordx1)
            worksheet.merge_range('J24:M24', ' ', bordx1)
            worksheet.write('N24', ' ', bordx1)
            worksheet.write('O24', ' ', bordx1)
            worksheet.write('P24', ' ', bordx1)
            worksheet.write('Q24', ' ', bordx1)
            worksheet.merge_range('A25:D25', ' ', bordx1)
            worksheet.merge_range('E25:I25', ' ', bordx1)
            worksheet.merge_range('J25:M25', ' ', bordx1)
            worksheet.write('N25', ' ', bordx1)
            worksheet.write('O25', ' ', bordx1)
            worksheet.write('P25', ' ', bordx1)
            worksheet.write('Q25', ' ', bordx1)
            worksheet.merge_range('R18:T18', ' ', bordx1)
            worksheet.merge_range('R19:T19', ' ', bordx1)
            worksheet.merge_range('R20:T20', ' ', bordx1)
            worksheet.merge_range('R21:T21', ' ', bordx1)
            worksheet.merge_range('R22:T22', ' ', bordx1)
            worksheet.merge_range('R23:T23', ' ', bordx1)
            worksheet.merge_range('R24:T24', ' ', bordx1)
            worksheet.merge_range('R25:T25', ' ', bordx1)
            worksheet.merge_range('A28:E28', 'Final Average Rating', bordwrp)
            worksheet.merge_range('F28:M28', ' ', bordx1)
            worksheet.write('N28', ' ', bordx1)
            worksheet.write('O28', ' ', bordx1)
            worksheet.write('P28', ' ', bordx1)
            worksheet.write('Q28', ' ', bordx1)
            worksheet.merge_range('R28:T28', ' ', bordx1)
            worksheet.merge_range('A29:E30', 'Comments and Recommendations for Development Purposes', bordwrp)
            worksheet.merge_range('F29:M30', ' ', bordx1)
            worksheet.merge_range('N29:N30', ' ', bordx1)
            worksheet.merge_range('O29:O30', ' ', bordx1)
            worksheet.merge_range('P29:P30', ' ', bordx1)
            worksheet.merge_range('Q29:Q30', ' ', bordx1)
            worksheet.merge_range('R29:T30', ' ', bordx1)
            worksheet.merge_range('A31:T31', ' ', bordx1)
            worksheet.merge_range('A32:T32', ' ', bordx1)
            worksheet.merge_range('A34:D34', 'Disscussed with', bordbn)
            worksheet.merge_range('E34:F34', 'Date:', bordbn)
            worksheet.merge_range('G34:J34', 'Assessed by:', bordbn)
            worksheet.merge_range('K34:L34', 'Date:', bordbn)
            worksheet.merge_range('M34:Q34', 'Final Rating by:', bordbn)
            worksheet.merge_range('R34:T34', 'Date:', bordbn)
            worksheet.merge_range('A35:D36', ' ', bordx1)
            worksheet.merge_range('E35:F37', ' ', bordx1)
            worksheet.merge_range('G35:J36', ' ', bordx1)
            worksheet.merge_range('K35:L37', ' ', bordx1)
            worksheet.merge_range('M35:Q36', ' ', bordx1)
            worksheet.merge_range('R35:T37', ' ', bordx1)
            worksheet.merge_range('A37:D37', 'Employee', bordwbc)
            worksheet.merge_range('G37:J37', 'Supervisor', bordwbc)
            worksheet.merge_range('M37:Q37', 'Head of Office', bordwbc)
            worksheet.merge_range('A38:T38', 'Legend:  1-Quantity     2-Efficiency     3-Timeliness     4-Average', bordn)
            # worksheet.write('D1', rankingtable.faculty.faculty_name)
            # worksheet.write('D2', rankingtable.current_rank)

            workbook.close()
            output.seek(0)
            file_facultyname = faculty_name
            filename = f"IPCR - {file_facultyname}.xlsx"
            response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
    return HttpResponse(status=400)