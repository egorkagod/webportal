from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('root.urls')),
    path('resume/', include("resume.urls")),
    # path('remote_pc/', include("remote_pc.urls")),
    # path('feeder/', include("feeder.urls")),
]
