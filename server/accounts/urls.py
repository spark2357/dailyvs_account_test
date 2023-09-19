from django.urls import path, include ,re_path
from django.views.generic import TemplateView
from .views import page

app_name = "accounts"

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('goodmansangbeen', page),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]