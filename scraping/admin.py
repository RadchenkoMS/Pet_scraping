from django.contrib import admin

from scraping.models import City,Symptom,Application

admin.site.register(City)
admin.site.register(Symptom)
admin.site.register(Application)
