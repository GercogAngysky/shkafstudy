from django.apps import AppConfig


class ContractConfig(AppConfig):
	name = 'contract'

	def ready(self):
		from . import signals

