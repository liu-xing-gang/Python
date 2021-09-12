# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Moment
from .models import UserProfile, UserProfileAdmin



# Register your models here.
admin.site.register(Moment)
# admin.site.register(UserProfile, UserProfileAdmin)