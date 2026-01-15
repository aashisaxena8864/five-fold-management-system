from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import AuditLog


# ========================
# DASHBOARDS
# ========================

@login_required
def admin_dashboard(request):
    return render(request, "student/dashboard/admin_dashboard.html")



# ========================
# RESOURCE REQUESTS
# ========================

@login_required
def resource_requests(request):
    return render(request, "student/dashboard/resource_requests.html")


# ========================
# FEEDBACK SYSTEM
# ========================

FEEDBACK_DATA = {
    "physical": [
        {
            "title": "Yoga & Physical Fitness",
            "rating": 5,
            "text": "Very energetic and refreshing activity.",
            "date": "03 Jan 2026, 20:15"
        },
        {
            "title": "Morning Parade & Drill",
            "rating": 4,
            "text": "Improved discipline and coordination.",
            "date": "05 Jan 2026, 18:40"
        }
    ],
    "aesthetic": [
        {
            "title": "Classical Music Training",
            "rating": 5,
            "text": "Music classes were very soothing.",
            "date": "02 Jan 2026, 14:20"
        }
    ],
    "practical": [
        {
            "title": "Craft & Handicraft Work",
            "rating": 4,
            "text": "Learned many hands-on skills.",
            "date": "04 Jan 2026, 16:10"
        }
    ],
    "moral": [
        {
            "title": "Morning Prayer & Geeta Path",
            "rating": 5,
            "text": "Prayer sessions brought inner peace.",
            "date": "01 Jan 2026, 07:00"
        }
    ],
    "intellectual": [
        {
            "title": "Environmental Studies Project",
            "rating": 5,
            "text": "Project-based learning is excellent.",
            "date": "06 Jan 2026, 11:30"
        }
    ],
}


@login_required
def feedback_home(request):
    return render(
        request,
        "student/dashboard/feedback/feedback_list.html",
        {"selected_fold": "Physical", "feedbacks": FEEDBACK_DATA["physical"]},
    )


@login_required
def feedback_by_fold(request, fold):
    feedbacks = FEEDBACK_DATA.get(fold, [])

    return render(
        request,
        "student/dashboard/feedback/feedback_list.html",
        {
            "selected_fold": fold.capitalize(),
            "feedbacks": feedbacks,
        },
    )


@login_required
def feedback_detail(request, fold, activity_id):
    activity = FEEDBACK_DATA.get(fold, [])[activity_id]

    return render(
        request,
        "student/dashboard/feedback/feedback_detail.html",
        {
            "fold": fold.capitalize(),
            "activity": activity,
        },
    )


# ========================
# NOTIFICATIONS
# ========================


@login_required
def notification_hub(request):
    return render(request, "student/notifications/notification_hub.html")

@login_required
def notifications_compose(request):
    return render(request, "student/notifications/compose.html")


@login_required
def notifications_drafts(request):
    return render(request, "student/notifications/drafts.html")


@login_required
def notifications_sent(request):
    return render(request, "student/notifications/sent.html")



# ========================
# AUDIT LOGGING
# ========================

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    AuditLog.objects.create(
        user=user,
        role="ADMIN" if user.is_superuser else "STUDENT",
        action="LOGIN",
        path=request.path,
        method=request.method,
        ip_address=request.META.get("REMOTE_ADDR"),
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    AuditLog.objects.create(
        user=user,
        role="ADMIN" if user and user.is_superuser else "STUDENT",
        action="LOGOUT",
        path=request.path,
        method=request.method,
        ip_address=request.META.get("REMOTE_ADDR"),
    )


# ---------------------------
# ADMIN → STUDENTS (NEW MODULE)
# ---------------------------


# =========================
# CENTRAL DATA (STATIC FOR NOW)
# =========================

STUDENT_ACTIVITY_DATA = {
    "physical": {
        "parade": [
            {"name": "Priya Verma", "roll": "CS21-04", "program": "B.Tech", "year": "3rd", "status": "Active"},
            {"name": "Anjali Sharma", "roll": "CS21-09", "program": "B.Tech", "year": "3rd", "status": "Active"},
            {"name": "Riya Gupta", "roll": "CS22-03", "program": "B.Tech", "year": "2nd", "status": "Active"},
        ],
        "yoga": [
            {"name": "Muskan Saxena", "roll": "CS22-11", "program": "B.Tech", "year": "2nd", "status": "Active"},
            {"name": "Neha Jain", "roll": "CS21-15", "program": "B.Tech", "year": "3rd", "status": "Active"},
        ],
    },

    "aesthetic": {
        "music": [
            {"name": "Kriti Mehta", "roll": "CS21-06", "program": "B.Tech", "year": "3rd", "status": "Active"},
            {"name": "Pooja Arora", "roll": "CS22-19", "program": "B.Tech", "year": "2nd", "status": "Active"},
        ],
        "painting": [
            {"name": "Simran Kaur", "roll": "CS23-02", "program": "B.Tech", "year": "1st", "status": "Active"},
        ],
    },

    "practical": {
        "craft": [
            {"name": "Aditi Singh", "roll": "CS22-07", "program": "B.Tech", "year": "2nd", "status": "Active"},
            {"name": "Isha Patel", "roll": "CS21-13", "program": "B.Tech", "year": "3rd", "status": "Active"},
        ],
        "tailoring": [
            {"name": "Sneha Verma", "roll": "CS23-05", "program": "B.Tech", "year": "1st", "status": "Active"},
        ],
    },

    "moral": {
        "prayer": [
            {"name": "Kavya Joshi", "roll": "CS21-18", "program": "B.Tech", "year": "3rd", "status": "Active"},
            {"name": "Nisha Yadav", "roll": "CS22-14", "program": "B.Tech", "year": "2nd", "status": "Active"},
        ]
    },

    "intellectual": {
        "projects": [
            {"name": "Rohini Mishra", "roll": "CS21-02", "program": "B.Tech", "year": "3rd", "status": "Active"},
            {"name": "Tanvi Kulkarni", "roll": "CS22-10", "program": "B.Tech", "year": "2nd", "status": "Active"},
        ]
    },
}

# =========================
# FACULTY DATA (STATIC FOR NOW)
# =========================

FACULTY_DATA = [
    {
        "name": "Dr. Neha Sharma",
        "department": "Physical",
        "activity": "Basketball",
        "email": "neha@bv.edu",
        "fold": "physical",
    },
    {
        "name": "Prof. Anjali Mehta",
        "department": "Aesthetic",
        "activity": "Guitar",
        "email": "anjali@bv.edu",
        "fold": "aesthetic",
    },
    {
        "name": "Ms. Kavita Joshi",
        "department": "Practical",
        "activity": "Craft",
        "email": "kavita@bv.edu",
        "fold": "practical",
    },
    {
        "name": "Dr. Sunita Jain",
        "department": "Moral",
        "activity": "Prayer",
        "email": "sunita@bv.edu",
        "fold": "moral",
    },
    {
        "name": "Dr. Pooja Iyer",
        "department": "Intellectual",
        "activity": "Projects",
        "email": "pooja@bv.edu",
        "fold": "intellectual",
    },
]

# =========================
# ALL STUDENTS (DEFAULT VIEW)
# =========================

@login_required
def students_all(request):
    students = []

    for fold in STUDENT_ACTIVITY_DATA.values():
        for activity in fold.values():
            students.extend(activity)

    return render(
        request,
        "student/dashboard/students/students_all.html",
        {"students": students},
    )


# =========================
# STUDENTS BY ACTIVITY
# =========================

@login_required
def students_by_activity(request, fold, activity):
    students = STUDENT_ACTIVITY_DATA.get(fold, {}).get(activity, [])

    return render(
        request,
        "student/dashboard/students/students_by_activity.html",
        {
            "fold": fold.capitalize(),
            "activity": activity.capitalize(),
            "students": students,
        },
    )


# =========================
# ACTIVITY PARTICIPATION
# =========================

@login_required
def activity_participation(request):
    participation = [
        {"name": "Physical", "count": 120, "color": "#3b82f6"},
        {"name": "Aesthetic", "count": 90, "color": "#ec4899"},
        {"name": "Practical", "count": 75, "color": "#10b981"},
        {"name": "Moral", "count": 60, "color": "#f59e0b"},
        {"name": "Intellectual", "count": 100, "color": "#8b5cf6"},
    ]

    return render(
        request,
        "student/dashboard/students/activity_participation.html",
        {"participation": participation},
    )



@login_required
def faculty_all(request):
    return render(
        request,
        "student/dashboard/faculty/faculty_all.html",
        {"faculty": FACULTY_DATA},
    )


@login_required
def faculty_by_fold(request, fold):
    filtered = [f for f in FACULTY_DATA if f["fold"] == fold]

    return render(
        request,
        "student/dashboard/faculty/faculty_by_fold.html",
        {
            "fold": fold.capitalize(),
            "faculty": filtered,
        },
    )


@login_required
def faculty_assign(request):
    return render(
        request,
        "student/dashboard/faculty/faculty_assign.html"
    )


@login_required
def faculty_workload(request):
    workload = [
        {"name": "Dr. Neha Sharma", "activities": 3},
        {"name": "Prof. Anjali Mehta", "activities": 2},
        {"name": "Ms. Kavita Joshi", "activities": 4},
    ]

    return render(
        request,
        "student/dashboard/faculty/faculty_workload.html",
        {"workload": workload},
    )
