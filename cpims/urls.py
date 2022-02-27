"""
cpims URL Configuration.

Other urls are import
Put here only urls not specific to app
"""
from importlib.resources import path
from django.conf.urls import include, url
from django.contrib import admin
from cpovc_auth import urls as auth_urls
from cpovc_registry import urls as registry_urls
from cpovc_forms import urls as forms_urls
from cpovc_reports import urls as reports_urls
from cpovc_gis import urls as gis_urls
from cpovc_api import urls as api_urls
from cpovc_ovc import urls as ovc_urls
from cpovc_settings import urls as settings_urls
from cpovc_manage import urls as manage_urls
from cpovc_help import urls as help_urls
from notifications import urls as noti_urls
from django.contrib.auth.views import (
    password_reset_done, password_change, password_change_done)
from cpovc_auth.views import password_reset
from django.views.generic import TemplateView
from cpovc_dashboard import urls as dashboard_api_urls
from cpovc_access.forms import StrictPasswordChangeForm


urlpatterns = [

    path('admin/', include(admin.site.urls), name='admin'),
    #path('/', 'cpovc_auth.views.log_in', name='home'),
    path('/', 'cpims.views.home', name='home'),
    path('accounts/request/', 'cpims.views.access', name='access'),
    path('accounts/terms/(?P<id>\d+)/', 'cpovc_access.views.terms',
        name='terms'),
    path('login/', 'cpovc_auth.views.log_in', name='login'),
    path('logout/', 'cpovc_auth.views.log_out', name='logout'),
    path('register/', 'cpovc_auth.views.register', name='register'),
    path('auth/', include(auth_urls)),
    path('registry/', include(registry_urls)),
    path('forms/', include(forms_urls)),
    path('reports/', include(reports_urls)),
    path('gis/', include(gis_urls)),
    path('api/v1/', include(api_urls)),
    path('ovcare/', include(ovc_urls)),
    path('settings/', include(settings_urls)),
    path('manage/', include(manage_urls)),
    path('help/', include(help_urls)),
    path('notifications/', include(noti_urls, namespace='notifications')),
    path('dashboard/(?P<did>[A-Z{2}\Z]+)/$',
        'cpovc_registry.views.dashboard', name='dashboard'),
    path('accounts/login/$', 'cpovc_auth.views.log_in', name='login'),
    path('accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset.html'},
        name='password_reset'),
    path('accounts/password/reset/done/$', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    path('accounts/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        'cpovc_auth.views.reset_confirm', name='password_reset_confirm'),
    path('reset/', 'cpovc_auth.views.reset', name='reset'),
    path('accounts/password/change/$', password_change,
        {'post_change_redirect': '/accounts/password/change/done/',
         'template_name': 'registration/password_change.html',
         'password_change_form': StrictPasswordChangeForm},
        name='password_change'),
    path('accounts/password/change/done/', password_change_done,
        {'template_name': 'registration/password_change_done.html'}),
    path('F57665A859FE7CFCDB6C8935196374AD\.txt$',
        TemplateView.as_view(template_name='comodo.txt',
                             content_type='text/plain')),
    path('d/', 'cpovc_dashboard.views.ovc_dashboard', name='ovc_dashboard'),
    path('d/hivstat/', 'cpovc_dashboard.views.ovc_dashboard_hivstat', name='hivstat_dash'),
    path('d/services/', 'cpovc_dashboard.views.ovc_dashboard_services', name='services_dash'),
    path('d/cm/', 'cpovc_dashboard.views.ovc_dashboard_cm', name='cm_dash'),
    path('api/v2/', include(dashboard_api_urls)),
    path('robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain'))]

handler400 = 'cpims.views.handler_400'
handler404 = 'cpims.views.handler_404'
handler500 = 'cpims.views.handler_500'

admin.site.site_header = 'CPIMS Administration'
admin.site.site_title = 'CPIMS administration'
admin.site.index_title = 'CPIMS admin'
