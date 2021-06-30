from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('index.urls', 'index'), namespace='index')),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]
