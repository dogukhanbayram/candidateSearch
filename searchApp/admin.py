from django.contrib import admin
from .models import frontEndModel, mobileDevModel, fullStackModel

admin.site.register(frontEndModel)
admin.site.register(mobileDevModel)
admin.site.register(fullStackModel)