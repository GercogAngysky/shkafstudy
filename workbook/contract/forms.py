from django import forms
from .models import Contract, Product, Payment
from core.forms import BaseForm
from django.forms import modelform_factory


class ContractForm(BaseForm):

	class Meta(BaseForm.Meta):
		model = Contract



class ProductForm(BaseForm):

	class Meta(BaseForm.Meta):
		model = Product


class PaymentForm(BaseForm):

	class Meta:
		model = Payment
		exclude = ['status']

	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	field = self.fields['status']
	# 	field.widget.attrs['class'] = 'for-admin'
