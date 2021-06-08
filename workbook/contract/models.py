from django.db import models
from django.utils import timezone
from person.models import Person, Adress, Organization 
from making.models import Employee

from transliterate import translit, get_available_language_codes


class Contract(models.Model):
	number = models.IntegerField("номер договора", )
	date = models.DateField("дата подписания", default = timezone.now)
	set_execute_date = models.DateField("назначення дата сдачи")
	due_execute_date = models.DateField("действительная дата сдачи",  null = True, blank = True)
	organization = models.ForeignKey(Organization,  on_delete = models.SET_NULL,  null = True, blank = True, verbose_name = 'организация')
	person = models.ForeignKey(Person,  on_delete = models.SET_NULL, verbose_name = 'заказчик', null=True, blank = True)
	employee = models.ForeignKey(Employee,  on_delete = models.SET_NULL, verbose_name = 'заказ принял', null=True, blank = True)
	adress = models.ForeignKey(Adress,  on_delete = models.SET_NULL, verbose_name = 'адрес', null=True, blank = True)
	note = models.CharField("примечание", max_length=128, null=True, blank = True)

	def __str__(self):
		return f"№{self.number} от {self.date}"

	class Meta:
		ordering = ['number', 'date']
		# unique_together = ['number', 'date']



class Product(models.Model):

	def user_directory_path(instance, filename):
		return f'product/icons/{instance.id}_{translit(instance.name, reversed=True)}.jpg'
	
	name = models.CharField("наименование", max_length=128)
	count = models.IntegerField("количество", )
	price = models.IntegerField("общая стоимость", )
	contract = models.ForeignKey(Contract,  on_delete = models.SET_NULL, null=True, blank = True, verbose_name = 'договор')
	note = models.CharField("примечание", max_length=128, null=True, blank = True)
	image = models.ImageField("эскиз", upload_to=user_directory_path, null=True, blank = True)

	def __str__(self):
		return f"{self.name} {self.count}"

	class Meta:
		unique_together = ['name', 'contract',]
		ordering = ['contract',]


class Payment(models.Model):
	CASH = 1
	CARD = 2
	BILL = 3	
	FORM_PAYMENT_CHOICES = [
		(CASH, "наличные"),
		(CARD, "на карту"),
		(BILL, "по счету"),
	]
	YIELD = 1
	TAKE  = 2
	STATUS_PAYMENT_CHOICES = [
		(YIELD, "принято в кассу"),
		(TAKE, "инкассация"),
	]
	date = models.DateField("дата платежа", default = timezone.now)
	contract = models.ForeignKey(Product,  on_delete = models.SET_NULL, null=True, blank = True, verbose_name = 'изделие')
	person = models.ForeignKey(Employee,  on_delete = models.SET_NULL, null=True, blank = True, verbose_name = 'получатель')
	payment = models.IntegerField("сумма платжа",)
	set_payment_date = models.DateField("дата установленная",)
	due_payment_date = models.DateField("дата действительная", blank = True)
	form_payment = models.SmallIntegerField("форма платежа", choices = FORM_PAYMENT_CHOICES, default = 1)
	status = models.SmallIntegerField(choices = STATUS_PAYMENT_CHOICES, default = 1)
	note = models.CharField("примечание", max_length=128, null=True, blank = True)

	def __str__(self):
		return f"{self.date} {self.payment} {self.contract}"

	class Meta:
		# unique_together = ['date', 'contract',]
		ordering = ['date',]


# from .signals import *