# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    "",
    url(r"^",      include("madm_restapi.menu.urls")),
    url(r'^admin/', include('madm_restapi.admin.urls')),
    url(r"^menu/", include("madm_restapi.menu.urls")),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
