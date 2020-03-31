from django.shortcuts import render
from django.utils import timezone
from  .models import Post, FizykaPost, InfaPost
from itertools import chain



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_infa(request):
    infa = InfaPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': infa})

def post_listt_Fiza(request):
    fiza = FizykaPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': fiza})