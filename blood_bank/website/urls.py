from django.conf.urls import url
from django.urls import include
from . import views
# from django.contrib.auth import login
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^campaigns/$', views.campaign, name='campaign'),
    url(r'^campaign/(?P<id>\d+)/$', views.v_campaign, name='campaign_id'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^dashboard/blood_donor/$', views.blood_donor, name='blood_donor'),
    url(r'^dashboard/blood_donor/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/blood_donor/(?P<id>\d+)/$', views.view_donor, name='donor_id'),
    url(r'^dashboard/message/$', views.message, name='message'),
    url(r'^dashboard/message/(?P<id>\d+)/$', views.view_message, name='message_id'),
    url(r'^dashboard/message/delete/(?P<id>\d+)/$', views.delete_message, name='delete_message'),
    url(r'^dashboard/need_blood/$', views.need_blood, name='need_blood'),
    url(r'^dashboard/need_blood/edit_recipient/(?P<id>\d+)/$', views.edit_recipient, name='edit_recipient'),
    url(r'^dashboard/need_blood/delete_recipient/(?P<id>\d+)/$', views.delete_recipient, name='delete_recipient'),
    url(r'^dashboard/view-campaign/$', views.view_campaign, name='admin-campaign'),
    url(r'^dashboard/view-campaign/delete/(?P<id>\d+)/$', views.delete_campaign, name='delete_campaign'),
    url(r'^dashboard/view-campaign/add-campaign/$', views.add_campaign, name='add_campaign'),
    url(r'^dashboard/view-campaign/edit-campaign/(?P<id>\d+)/$', views.edit_campaign, name='edit_campaign'),
    url(r'^preregister/$', views.preregister, name='preregister'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^request-blood/$', views.request_form, name='request-blood'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='website/reset-password.html'), name='reset-password'),
    url(r'^reset-password/done$', PasswordResetDoneView.as_view(), name='reset_password_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    url(r'^sign-in/$', LoginView.as_view(template_name='website/sign-in.html'), name='sign-in'),
    url(r'^sign-out/$', LogoutView.as_view(template_name='website/sign-out.html'), name='sign-out'),
    url(r'^sign-up/$', views.signup, name='sign-up'),
]

