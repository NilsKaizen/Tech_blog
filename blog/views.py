from blog.forms import NewPostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate as django_auth
from django.contrib.auth.decorators import login_required
from .models import Post, Author
from .forms import NewPostForm
from django.utils import timezone
from django.views.generic import CreateView


class PostView(CreateView):
    post = Post
    exclude= ['date_c', 'author', 'date_p']
    template_name = 'blog/view_post.html'

def home(request):
    posts = Post.objects.filter(draft=False).order_by('-date_p')
    
    
    if request.user.is_authenticated:
        return render(request,'blog/current_blogs.html', {'posts': posts})
    else:
        return render(request, 'blog/home.html', {'posts': posts})

@login_required()
def create_post(request):
    
    author = Author.objects.filter(name=request.user.username)[0]
    form = NewPostForm(author=author)

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        form.author = author

        print(form)

        if form.is_valid(): 
            form.save()
            return redirect('blog:home')
        else: 
            print()
            print(form.errors)
            print('Error Not Valid FORM')
            print()

    else: 
        return render(request, 'blog/create_post.html', {'form': form, 'error': ''})



    # if request.method == 'GET':
    #     return render(request, 'blog/create_post.html')
    # else: 
    #     try: 
    #         try:
    #             request.POST['draft'] 
    #             date_p = None
    #             draft = True
    #         except : 
    #             date_p = timezone.now()
    #             draft = False
    #         post = Post(title=request.POST['title'],
    #                     text=request.POST['text'],
    #                     draft=draft,
    #                     date_p= date_p,
    #                     author=author)
    #         post.save()
    #         return redirect('blog:home')

    #     except ValueError as e:
    #         print(e)
    #         return render(request, 'blog/create_post.html', {'error': "Wrong data inserted in the fields. Try again"})
        

@login_required()
def view_post(request, post_pk):
    try:
        author = Author.objects.filter(name=request.user.username)[0]
        post = get_object_or_404(Post, pk=post_pk, author=author)
    except : 
        post = get_object_or_404(Post, pk=post_pk)
        # TODO: Puede ser que esl error esté aqui

    if request.method == 'POST':
        try:
            try:
                request.POST['draft']
                draft = True
            except:
                draft = False
            
            post.title = request.POST['title']
            post.text = request.POST['text']
            post.draft = draft
            post.date_p = timezone.now()
            post.save()

            return redirect('blog:home')
            
        except ValueError:
            return render(request, 'blog/view_post.html', {'error': "Wrong data inserted in the fields. Try again!"})
    else:
        return render(request, 'blog/view_post.html', {'post': post})

@login_required()
def draft_posts(request):
    author = Author.objects.filter(name=request.user.username)[0]
    posts = Post.objects.filter(draft=True, author= author).order_by('-date_p')
    print(len(posts))
    return render(request, 'blog/current_blogs.html', {'posts': posts, 'len': len(posts)})

# @login_required()
# def delete_post(request, post_pk):
#     if request.method == 'POST':
#         author = Author.objects.filter(name=request.user.username)[0]
#         post = Post.objects.filter(pk=post_pk, author=author)
#         post.delete()
