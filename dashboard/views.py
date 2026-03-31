from django.shortcuts import render


def home(request):
    context = {
        "resident_name": "Thabo",
        "status_cards": [
            {"label": "Pending", "count": 2, "tone": "pending"},
            {"label": "In Progress", "count": 1, "tone": "progress"},
            {"label": "Resolved", "count": 4, "tone": "resolved"},
        ],
        "recent_reports": [
            "Pothole on Main Street",
            "Broken streetlight near taxi rank",
            "Blocked drain in Galeshewe",
        ],
    }
    return render(request, "dashboard/home.html", context)
