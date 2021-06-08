from django.urls import path
from . import views


urlpatterns = [
	path('person/list', views.person_list, name = 'person_list'),
	path('person/create', views.person_create, name = 'person_create'),
	path('person/<int:pk>/detail', views.person_detail, name = 'person_detail'),
	path('person/<int:pk>/update', views.person_update, name = 'person_update'),
	path('person/<int:pk>/delete', views.PersonDelete.as_view(), name = 'person_delete'),

	path('adress/list', views.AdressList.as_view(), name = 'adress_list'),
	path('adress/create', views.AdressCreate.as_view(), name = 'adress_create'),
	path('adress/<int:pk>/detail', views.adress_detail, name = 'adress_detail'),
	path('adress/<int:pk>/update', views.AdressUpdate.as_view(), name = 'adress_update'),
	path('adress/<int:pk>/delete', views.AdressDelete.as_view(), name = 'adress_delete'),
	
	path('organization/list', views.organization_list, name = 'organization_list'),
	path('organization/create', views.OrganizationCreate.as_view(), name = 'organization_create'),
	path('organization/<int:pk>/detail', views.organization_detail, name = 'organization_detail'),
	path('organization/<int:pk>/update', views.OrganizationUpdate.as_view(), name = 'organization_update'),
	path('organization/<int:pk>/delete', views.OrganizationDelete.as_view(), name = 'organization_delete'),
]