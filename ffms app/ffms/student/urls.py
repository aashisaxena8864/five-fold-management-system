from django.urls import path
from . import views

app_name = "student"   # ✅ ONLY ONE app_name

urlpatterns = [

    # ================= DASHBOARD =================
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),

    # ================= STUDENTS =================
    path("dashboard/students/", views.students_all, name="admin_students"),
    path(
        "dashboard/students/<str:fold>/<str:activity>/",
        views.students_by_activity,
        name="students_by_activity"
    ),
    path(
        "dashboard/students/participation/",
        views.activity_participation,
        name="activity_participation"
    ),

    # ================= FACULTY =================
    path("dashboard/faculty/", views.faculty_all, name="admin_faculty"),
    path("dashboard/faculty/assign/", views.faculty_assign, name="faculty_assign"),
    path("dashboard/faculty/workload/", views.faculty_workload, name="faculty_workload"),
    path("dashboard/faculty/<str:fold>/", views.faculty_by_fold, name="faculty_by_fold"),

    # ================= RESOURCE REQUESTS =================
    path("dashboard/resource-requests/", views.resource_requests, name="resource_requests"),

    # ================= FEEDBACK =================
    path("feedback/", views.feedback_home, name="feedback"),
    path("feedback/<str:fold>/", views.feedback_by_fold, name="feedback_by_fold"),
    path(
        "feedback/<str:fold>/<int:activity_id>/",
        views.feedback_detail,
        name="feedback_detail"
    ),

    # ================= NOTIFICATIONS =================
    path("notifications/", views.notification_hub, name="notifications"),
    path("notifications/compose/", views.notifications_compose, name="notifications_compose"),
    path("notifications/drafts/", views.notifications_drafts, name="notifications_drafts"),
    path("notifications/sent/", views.notifications_sent, name="notifications_sent"),
]
