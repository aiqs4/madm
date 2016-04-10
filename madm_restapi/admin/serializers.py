# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User

from rest_framework import serializers
#from rest_framework_recursive.fields import RecursiveField

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

