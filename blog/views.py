from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from models import Blog, Comment
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.

class indexView(generic.ListView):
    template_name='blog/index.html'
    context_object_name='blogs'
    
    def get_queryset(self):
        return Blog.objects.order_by('-posted_date')[:3]
        
class archiveView(generic.ListView):
    template_name='blog/archive.html'
    context_object_name='blogs'
    
    def get_queryset(self):
        return Blog.objects.order_by('-posted_date')
    
class detailView(generic.DetailView): 
    model=Blog
    template_name='blog/detail.html'
    
def post(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        _post = Blog.comment_set.get(pk=request.POST['comment'])
    except (KeyError, comment.DoesNotExist):
        return render(request, 'blog/detail.html', {
            'comment':comment,
            'error_message': "Invalid input",
        })
    else:
        _post.save()
        return HttpResponseRedirect(reverse('index', args=(blog.id)))
