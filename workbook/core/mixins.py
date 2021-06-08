

class CleanImageMixin:
	''' удаление изображения при удалении записи или ее обнавлении '''
	def clean_up(self, condition=True):
		object = self.get_object()
		if object.image and condition:
			object.image.delete()

