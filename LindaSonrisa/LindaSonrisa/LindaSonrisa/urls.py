from django.contrib import admin
#add re_pat, include
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # home app mainly for testing
    re_path('', include('applications.home.urls')),
    # users app Create access to different modules
    re_path('', include('applications.users.urls')),
]
