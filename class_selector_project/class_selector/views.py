from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('class_selector/index.html', context)

def americanstudies(request):
    context = RequestContext(request)
    context_dict = {'major': 'American Studies'}
    return render_to_response('class_selector/major.html', context_dict, context)

def anthropology(request):
    context = RequestContext(request)
    context_dict = {'major': 'Anthropology'}
    return render_to_response('class_selector/major.html', context_dict, context)
    