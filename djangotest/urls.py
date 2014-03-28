from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from article.views import HelloTemplate

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^articles/', include('article.urls')),

    #auth urls
    url(r'^accounts/login/$', 'djangotest.views.login'),
    url(r'^accounts/auth/$', 'djangotest.views.auth_view'),
    url(r'^accounts/logout/$', 'djangotest.views.logout'),
    url(r'^accounts/loggedin/$', 'djangotest.views.loggedin'),
    url(r'^accounts/invalid/$', 'djangotest.views.invalid_login'),

    #registration
    url(r'^accounts/register/$', 'djangotest.views.register_user'),
    url(r'^accounts/register_success/$', 'djangotest.views.register_success'),



    #first princeples urls
    url(r'^hello/$', 'article.views.hello', name='hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_class/$', HelloTemplate.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)