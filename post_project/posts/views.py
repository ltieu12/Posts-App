from django.shortcuts import render

# Create your views here.
def post_page(request):
    return render(request, 'post_page.html')

def posts_list(request):
    return render(request, 'posts_list.html')
