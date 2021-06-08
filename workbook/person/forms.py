from django import forms
from .models import Person, Adress, Organization
from core.forms import BaseForm

from django.forms import Textarea, TextInput, Select
from django.forms import modelform_factory, ModelForm
from django.contrib.admin import ModelAdmin


class PersonForm(ModelForm):   
    class Meta:
        model = Person
        fields = "__all__"



# class PersonForm(forms.ModelForm):

# 	class Meta:
# 		model = Person
# 		fields = ['family_name', 'name', 'father_name',
# 			'phone_number_1', 'phone_number_2', 'adress']

# # фабричная функция для создания новой формы или дополнения существующей формы 
# PersonForm = modelform_factory(Person, form = PersonForm, 
# 	widgets = {'adress': Select(attrs = {'class': 'related-widget-wrapper'}) })




AdressForm = modelform_factory(Adress, fields = '__all__')

# class AdressForm(BaseForm):

# 	class Meta(BaseForm.Meta):
# 		model = Adress


class OrganizationForm(BaseForm):

    class Meta(BaseForm.Meta):
        model = Organization
