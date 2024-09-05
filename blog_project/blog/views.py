from django.shortcuts import render

# Create your views here.
def BlogListView(request):
    return render(request,'blog/blog_list.html', {})