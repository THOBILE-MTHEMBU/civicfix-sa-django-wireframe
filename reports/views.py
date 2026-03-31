from django.shortcuts import render


def create_report(request):
    context = {
        "issue_types": ["Pothole", "Streetlight", "Water leak", "Blocked drain"],
    }
    return render(request, "reports/report_form.html", context)
