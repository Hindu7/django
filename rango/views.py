from django.http import HttpResponse

from django.shortcuts import render
from rango.models import Category

#def index(requests):
#    return HttpResponse("Welcome")

'''def index(request):
    context_dict = {'boldmessage': "This tutorial created by Hindu"}
    return render(request, 'rango/about.html', context=context_dict)'''

def index(request):
    category_list = Category.objects.order_by('-likes')[:]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def about(requests):
        html="<a href ='/rango/'>About</a>"
        return HttpResponse("Welcome123"+html )

# Create your views here.
