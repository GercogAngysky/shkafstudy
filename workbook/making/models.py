from django.db import models
from django.conf import settings


class Employee(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING)
	position = models.CharField("должность", max_length=30)
	responsibility = models.CharField("обязанности", max_length=30)
	score = models.IntegerField("баллы", null=True)

	def __str__(self):
		return f"{self.user}"

	class Meta:
		verbose_name = 'Employee'