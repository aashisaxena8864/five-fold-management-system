from django.apps import AppConfig


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ffms.student'

    def ready(self):
        import ffms.student.views  # 👈 REQUIRED
