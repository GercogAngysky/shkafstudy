from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from config.decorators import login_required
from .forms import ContractForm, ProductForm, PaymentForm
from .models import Contract, Product, Payment

from django.contrib import admin
from person.models import Person

from django.contrib.admin.widgets import RelatedFieldWidgetWrapper


@login_required
class ContractList(ListView):
    model = Contract
    template_name = 'home/base_list.html'
    def get_context_data(self, **kwargs):
        object_list = super().get_context_data(**kwargs)
        object_list['urlpath'] = 'contract_detail'
        return object_list

@login_required
class ContractDetail(DetailView):
    model = Contract
    template_name = 'home/base_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context['object']
        data = {field.verbose_name: getattr(obj, field.name) for field in obj._meta.fields}.items()
        context['data'] = data
        context['urlpath_update'] = 'contract_update'
        context['urlpath_delete'] = 'contract_delete'
        context['app_name'] = 'contract'
        return context

# @login_required
# class ContractDetail(DetailView):
#     model = Contract
#     template_name = 'contract/contract_detail.html'
#     def get_context_data(self, **kwargs):
#         object_list = super().get_context_data(**kwargs)
#         object_list['urlpath_update'] = 'contract_update'
#         object_list['urlpath_delete'] = 'contract_delete'
#         return object_list


@login_required
class ContractCreate(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('contract_list')

    def get_form(self, *args, **kwargs):
        form = super(ContractCreate, self).get_form(self.form_class)
        rel_model = form.Meta.model

        print(rel_model)
        print(dir(rel_model._meta.get_field('person')))

        rel = rel_model._meta.get_field('person').remote_field
        # irel = rel_model._meta.get_field('adress').rel
        form.fields['person'].widget = RelatedFieldWidgetWrapper(form.fields['person'].widget, rel, admin.site, can_add_related=True, can_change_related=True)
        # form.fields['adress'].widget = RelatedFieldWidgetWrapper(form.fields['adress'].widget, irel, admin.site, can_add_related=True, can_change_related=True)
        return form 

@login_required
class ContractUpdate(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('contract_list')

@login_required
class ContractDelete(DeleteView):
    model = Contract
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('contract_list')


@login_required
class ProductList(ListView):
    model = Product
    template_name = 'home/base_list.html'
    def get_context_data(self, **kwargs):
        object_list = super().get_context_data(**kwargs)
        object_list['urlpath'] = 'product_detail'
        return object_list

@login_required
class ProductDetail(DetailView):
    model = Product
    template_name = 'home/base_detail.html'
    def get_context_data(self, **kwargs):
        object_list = super().get_context_data(**kwargs)
        obj = object_list['object']
        data = {field.verbose_name: getattr(obj, field.name) for field in obj._meta.fields}.items()
        object_list['data'] = data
        object_list['urlpath_update'] = 'product_update'
        object_list['urlpath_delete'] = 'product_delete'
        return object_list

@login_required
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('product_list')

@login_required
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('product_list')
    # def post(self, request, *args, **kwargs):
    #     self.clean_up(condition = (request.FILES or request.POST.get('image-clear')))
    #     return super().post(request, *args, **kwargs)

@login_required
class ProductDelete(DeleteView):
    model = Product
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('product_list')
    # def delete(self, request, **kwargs):
    #     self.clean_up()
    #     return super().delete(self)



@login_required
class PaymentList(ListView):
    model = Payment
    template_name = 'home/base_list.html'
    def get_context_data(self, **kwargs):
        object_list = super().get_context_data(**kwargs)
        object_list['urlpath'] = 'payment_detail'
        return object_list

@login_required
class PaymentDetail(DetailView):
    model = Payment
    template_name = 'home/base_detail.html'
    def get_context_data(self, **kwargs):
        object_list = super().get_context_data(**kwargs)
        obj = object_list['object']
        data = {field.verbose_name: getattr(obj, field.name) for field in obj._meta.fields}.items()
        object_list['data'] = data
        object_list['urlpath_update'] = 'payment_update'
        object_list['urlpath_delete'] = 'payment_delete'
        return object_list

@login_required
class PaymentCreate(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('payment_list')

@login_required
class PaymentUpdate(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('payment_list')

@login_required
class PaymentDelete(DeleteView):
    model = Payment
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('payment_list')
