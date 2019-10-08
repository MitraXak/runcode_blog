from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'maket.html')

def article(request, id=None):
	return render(request, 'article/article.html')

