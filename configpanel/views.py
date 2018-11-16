from django.shortcuts import render, get_object_or_404
from .models import configweather,configdev
from django.utils import timezone
from .forms import channelform,devform
from django.shortcuts import redirect

# Create your views here.
def config_list(request):
    webs = configweather.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    devs = configdev.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'configpanel/config_list.html', {'webs': webs, 'devs': devs})

def config_new(request):
    if request.method == "POST":
        form = channelform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('config_list')
    else:
        form = channelform()
        type = "ch"
    return render(request, 'configpanel/config_edit.html', {'form': form, 'type': type})

def config_new_dev(request):
    if request.method == "POST":
        form = devform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('config_list')
    else:
        form = devform()
        type = "devform"
    return render(request, 'configpanel/config_edit.html', {'form': form,'type': type})

def config_edit(request, pk):
    post = get_object_or_404(configweather, pk=pk)
    type = "ch"
    if request.method == "POST":
        form = channelform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('config_list')
    else:
        form = channelform(instance=post)
    return render(request, 'configpanel/config_edit.html', {'form': form, 'type': type})

def config_edit_dev(request, pk):
    post = get_object_or_404(configdev, pk=pk)
    type = "devform"
    if request.method == "POST":
        form = devform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('config_list')
    else:
        form = devform(instance=post)
    return render(request, 'configpanel/config_edit.html', {'form': form, 'type': type})


def config_del(request, pk):
    post = get_object_or_404(configweather, pk=pk)
    form = channelform(instance=post)
    post = form.save(commit=False)
    post.author = request.user
    post.published_date = timezone.now()
    post.delete()
    return redirect('config_list')

def config_del_dev(request, pk):
    post = get_object_or_404(configdev, pk=pk)
    form = devform(instance=post)
    post = form.save(commit=False)
    post.author = request.user
    post.published_date = timezone.now()
    post.delete()
    return redirect('config_list')
