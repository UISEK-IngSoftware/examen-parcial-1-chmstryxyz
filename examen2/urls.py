from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls', namespace='movies')),
    path('', RedirectView.as_view(url='movies/', permanent=False)),
]