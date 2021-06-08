from django.db import models
from django.conf import settings
from making.models import Employee

from transliterate import translit, get_available_language_codes

class Post(models.Model):
	def user_directory_path(instance, filename):
		return f"post/{instance.id}_{translit(instance.title, reversed=True)}.jpg"
	author = models.ForeignKey(Employee,  on_delete = models.SET_NULL, verbose_name = 'автор', null=True, blank = False)
	title = models.CharField("заголовок", max_length=128)
	created_date = models.DateField("дата публикации", auto_now_add = True)
	update_date = models.DateField("дата изменения", auto_now = True)
	text = models.TextField()
	photo = models.ImageField("фото", upload_to=user_directory_path, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ["title", "created_date"]
		ordering = ['created_date']
