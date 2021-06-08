from django.urls import path
from . import views


urlpatterns = [
	path('contract/list', views.ContractList.as_view(), name = 'contract_list'),
	path('contract/create', views.ContractCreate.as_view(), name = 'contract_create'),
	path('contract/<int:pk>/detail', views.ContractDetail.as_view(), name = 'contract_detail'),
	path('contract/<int:pk>/delete', views.ContractDelete.as_view(), name = 'contract_delete'),
	path('contract/<int:pk>/update', views.ContractUpdate.as_view(), name = 'contract_update'),

	path('product/list', views.ProductList.as_view(), name = 'product_list'),
	path('product/create', views.ProductCreate.as_view(), name = 'product_create'),
	path('product/<int:pk>/detail', views.ProductDetail.as_view(), name = 'product_detail'),
	path('product/<int:pk>/delete', views.ProductDelete.as_view(), name = 'product_delete'),
	path('product/<int:pk>/update', views.ProductUpdate.as_view(), name = 'product_update'),

	path('payment/list', views.PaymentList.as_view(), name = 'payment_list'),
	path('payment/create', views.PaymentCreate.as_view(), name = 'payment_create'),
	path('payment/<int:pk>/detail', views.PaymentDetail.as_view(), name = 'payment_detail'),
	path('payment/<int:pk>/delete', views.PaymentDelete.as_view(), name = 'payment_delete'),
	path('payment/<int:pk>/update', views.PaymentUpdate.as_view(), name = 'payment_update'),
]