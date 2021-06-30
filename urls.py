from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(
        '',
        include(('oc_lettings_site.urls', 'oc_lettings_site'), namespace='oc_lettings_site')
    ),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]
