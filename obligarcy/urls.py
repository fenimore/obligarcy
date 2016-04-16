from django.conf.urls import url
from . import views
from django.conf.urls.static import static, settings


urlpatterns = [
    # ex: /oblicarcy/
    url(r'^$', views.index, name='index'),
    url(r'^firehose/$', views.firehose, name='firehose'),


    url(r'^profile/$', views.profile),
    # ex: /obligarcy/user/5/
    url(r'^user/([0-9]+)/$', views.show_prof, name='user'),
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^update/$', views.update_profile, name='update'),
    # ex: /obligarcy/user
    #url(r'^user/$', views.profile, name='profile'),

    # ex: /oblicarcy/submissions/5/
    url(r'^submission/([0-9a-z]+)/$', views.show_sub, name='submission'),
    url(r'^submit/([0-9a-z]+)/([0-9]+)/$', views.submit, name='submit'),
    url(r'^upload/([0-9a-z]+)/([0-9]+)/$', views.submit_upload, name='upload'),

#    url(r'^submit/([0-9a-z]+)/([0-9]+)/$', views.submit, name='submit'),

    # ex: /oblicarcy/contracts/5/
    url(r'^contract/([0-9a-z]+)/$', views.show_con, name='contract'),
    url(r'^challenge/$', views.challenge, name='challenge'),
    url(r'^sign/([0-9a-z]+)/$', views.sign_con, name='sign'),
    url(r'^active/([0-9]+)/$', views.show_active, name='active'),

    # ex: /oblicarcy/login/
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
