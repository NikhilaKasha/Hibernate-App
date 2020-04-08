from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.urls import get_callable

urlpatterns = [
    path('', TemplateView.as_view(template_name='app2/home.html'), name='home'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('app2/', include('app2.urls')),
    path('app2/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    # path('logout/', home, {'next_page': settings.LOGOUT_REDIRECT_URL},
    # name='logout'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LoginView.as_view(), name='logout'),

    # re_path(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    # re_path(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),


]

