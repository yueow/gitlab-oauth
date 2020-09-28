from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from core import views


app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('logout', LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
