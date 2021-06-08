from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
from .models import Person, Adress, Organization
from .forms import PersonForm, AdressForm, OrganizationForm
from django.http import HttpResponse

from config.decorators import login_required


menu = ['PERSON', 'ADRESS', 'ORGANIZATION']


def home_list(request):
    context = {'name': 'домашняя страница'}
    print(request.user)
    # print(request.user.is_authenticated)
    print(request.user.groups.all())
    # print(request.user.groups.filter(name ='designer').exists())
    return render(request, 'home/home_list.html', context)

def person_list(request):
    person = Person.objects.all()
    context = {'person_list': person}
    return render(request, 'person/person_list.html', context)

def person_detail(request, pk):
    #person = Person.objects.get(pk = pk)
    person = get_object_or_404(Person, pk = pk)
    return render(request, 'person/person_detail.html', {'person': person})

@login_required
def person_create(request):
	if request.method == "POST":
		form = PersonForm(request.POST)
		if form.is_valid():
		    person = form.save(commit=False)
		    person.save()
		    return redirect('person_list')
		return redirect('person_list')
	else:
		form = PersonForm(initial = {'email' : ''})
		return render(request, 'person/person_form.html', {'form': form})

@login_required
def person_update(request, pk):
	person = get_object_or_404(Person, pk = pk)
	if request.method == "POST":
		form = PersonForm(request.POST, instance = person)
		if form.is_valid():
		    person = form.save(commit=False)
		    person.save()
		    return redirect('person_list')
	else:
		form = PersonForm(instance = person)
		return render(request, 'person/person_form.html', {'form': form})


@login_required
class PersonDelete(DeleteView):
    model = Person
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('person_list')




@login_required
class AdressList(ListView):
    model = Adress
    template_name = 'home/base_list.html'
    def get_context_data(self, **kwargs):
        object_list = super().get_context_data(**kwargs)
        object_list['urlpath'] = 'adress_detail'
        return object_list

@login_required
def adress_detail(request, pk):
    object = get_object_or_404(Adress, pk = pk)
    data = {field.verbose_name: getattr(object, field.name) for field in object._meta.fields}.items()
    urlpaths = {
                'urlpath_update': 'adress_update',
                'urlpath_delete': 'adress_delete',
                }
    return render(request, 'home/base_detail.html', {'object': object, 'data': data, **urlpaths})

@login_required
class AdressCreate(CreateView):
    model = Adress
    form_class = AdressForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('adress_list')
    # initial={'city':'Ноябрьск',}

@login_required
class AdressUpdate(UpdateView):
    model = Adress
    form_class = AdressForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('adress_list')

@login_required
class AdressDelete(DeleteView):
    model = Adress
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('adress_list')




@login_required
def organization_list(request):
    objects = Organization.objects.all()
    context = {'object_list': objects}
    context['urlpath'] = 'organization_detail'
    return render(request, 'home/base_list.html', context)


@login_required
def organization_detail(request, pk):
    object = get_object_or_404(Organization, pk = pk)
    data = {field.verbose_name: getattr(object, field.name) for field in object._meta.fields}.items()
    urlpaths = {
                'urlpath_update': 'organization_update',
                'urlpath_delete': 'organization_delete',
                }
    return render(request, 'home/base_detail.html', {'object': object, 'data': data, **urlpaths})

@login_required
class OrganizationCreate(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'home/base_form.html'
    success_url = 'list'
    # initial={'name':'ООО',}

@login_required
class OrganizationUpdate(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('organization_list')

@login_required
class OrganizationDelete(DeleteView):
    model = Organization
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('organization_list')




@login_required
def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')