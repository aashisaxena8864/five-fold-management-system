from .models import AuditLog


class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Log only meaningful requests
        if request.method in ['GET', 'POST']:
            user = request.user if request.user.is_authenticated else None

            role = 'ANONYMOUS'
            if user:
                if user.is_superuser:
                    role = 'ADMIN'
                elif user.is_staff:
                    role = 'FACULTY'
                else:
                    role = 'STUDENT'

            AuditLog.objects.create(
                user=user,
                role=role,
                action='VIEW',
                path=request.path,
                method=request.method,
                ip_address=request.META.get('REMOTE_ADDR'),
            )

        return response
