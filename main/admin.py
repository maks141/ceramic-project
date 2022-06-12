from django.contrib import admin
from django.db import models
from .models import Slider, NumberOrder, Partner, About

admin.site.register(Slider)
admin.site.register(NumberOrder)
admin.site.register(Partner)
admin.site.register(About)

