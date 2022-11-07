from django.shortcuts import render

# Create your views here.
def renderPosts(request):
    return render(request, 'blog.html')
def postDetail(request):
    return render(request, 'post_detail.html')