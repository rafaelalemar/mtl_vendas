# coding: utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moon_vendas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Este tem que ficar no final, caso contrário não vai achar os outros acima
    url(r'', include('core.urls', namespace='core')),                         ## Aponta para o core.urls
)
