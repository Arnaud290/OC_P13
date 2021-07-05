from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path(
        '',
        include(('oc_lettings_site.urls', 'oc_lettings_site'), namespace='oc_lettings_site')
    ),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]
