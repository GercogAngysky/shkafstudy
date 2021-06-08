from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm
from config.decorators import login_required


def post_list(request):
	post = Post.objects.all()
	context = {"object_list": post}
	return render(request, "post/post_list.html", context)

@login_required
def post_detail(request, pk):
    object = get_object_or_404(Post, pk = pk)
    data = {field.verbose_name: getattr(object, field.name) for field in object._meta.fields}.items()
    urlpaths = {
                'urlpath_update': 'post_update',
                'urlpath_delete': 'post_delete',
                }
    return render(request, 'home/base_detail.html', {'object': object, 'data': data, **urlpaths})

@login_required
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('post_list')
    # initial={'city':'Ноябрьск',}

@login_required
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'home/base_form.html'
    success_url = reverse_lazy('post_list')

@login_required
class PostDelete(DeleteView):
    model = Post
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('post_list')

