# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

#import re
from django.contrib.auth.models import User
#from django.template import Template
#from django.template.context import Context

from rest_framework.viewsets import ModelViewSet

#from cms.middleware.page import CurrentPageMiddleware

from .serializers import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

