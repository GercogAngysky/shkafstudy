from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete
from django.db import IntegrityError
from .models import Contract, Product

from PIL import Image



@receiver(pre_save, sender = Contract)
def unique_together_year_contract_num(instance, **kwargs):
	year = instance.date.year
	num = instance.number
	if Contract.objects.filter(number = num, date__year = year).exclude(pk = instance.pk).exists():
		raise IntegrityError("такой номер договора, в этом году, уже существует")


@receiver(pre_delete, sender = Product)
def image_delete(instance, **kwargs):
	if instance.image:
		instance.image.delete(False)

@receiver(pre_save, sender = Product)
def image_update(instance, **kwargs):
	if instance.pk:
		old_instance = Product.objects.get(pk=instance.pk)
		old_img = old_instance.image
		new_img = instance.image
		if old_img and ((not new_img) or old_img != new_img):
			old_img.delete(False)

@receiver(post_save, sender = Product)
def image_resize(instance, **kwargs):
	image = instance.image
	size = 200
	if image:
		with Image.open(image) as img:
			w, h = img.size
			if size not in (w, h):
				width  = int(size*w/h) if w<h else size
				height = int(size*h/w) if w>h else size
				file = image.path
				img.resize((width, height), reducing_gap = 4).save(file, 'JPEG')

