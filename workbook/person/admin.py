from django.contrib import admin

from .models import *



class PersonAdmin(admin.ModelAdmin):
	# model = Person
	# fields = (('family_name', 'name'), 'father_name',)
	list_display = ('family_name', 'name', 'father_name', 'phone_number_1', 'adress')
	list_display_links = ('family_name',)
	search_fields = ('name', 'family_name', 'adress')



admin.site.register(Adress)
admin.site.register(Organization)
# admin.site.register(Person)

admin.site.register(Person, PersonAdmin)