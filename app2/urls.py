
from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.urls import reverse


app_name = 'app2'
urlpatterns = [
    #path('', views.home, name='home'),
    #re_path(r'^home/$', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('expert_list', views.expert_list, name='expert_list'),
    path('expert/create/', views.expert_new, name='expert_new'),
    path('expert/<int:pk>/edit/', views.expert_edit, name='expert_edit'),
    path('expert/<int:pk>/delete/', views.expert_delete, name='expert_delete'),
    path('expert/<int:pk>/summary/', views.summary, name='summary'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html')),

    # reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('signup/', auth_views.SignupView.as_view(), name='signup'),
    # re_path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # re_path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete')

]


