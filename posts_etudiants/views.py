from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import SignUpForm, PostForm
from .models import Post

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_posts')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def liste_posts(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(
            Q(titre__icontains=query) | Q(contenu__icontains=query)
        ).order_by('-date_creation')
    else:
        posts = Post.objects.all().order_by('-date_creation')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts_etudiants/post_list.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.save()
            return redirect('liste_posts')
    else:
        form = PostForm()
    return render(request, 'posts_etudiants/post_form.html', {'form': form, 'action': 'Créer'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts_etudiants/post_detail.html', {'post': post})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.auteur:
        return redirect('liste_posts')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('liste_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts_etudiants/post_form.html', {'form': form, 'action': 'Modifier'})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.auteur:
        return redirect('liste_posts')

    if request.method == 'POST':
        post.delete()
        return redirect('liste_posts')
    return render(request, 'posts_etudiants/post_confirm_delete.html', {'post': post})