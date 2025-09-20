from django.conf import settings

def gym_settings(request):
    return {
        "GYM_NAME": settings.GYM_NAME
    }