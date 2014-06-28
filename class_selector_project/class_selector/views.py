from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from class_selector.models import Major, Class

major_list = Major.objects.all()
context_dict = {'majors': major_list}

# Create your views here.
def index(request):
    context = RequestContext(request)
    for major in major_list:
        major.url = major.major_name.replace(' ', '_')
        if "'" in major.url:
            major.url = major.url.replace("'", "")
        if "," in major.url:
            major.url = major.url.replace(",", "")
    return render_to_response('class_selector/index.html', context_dict, context)

def major(request, major_name_url):
    context = RequestContext (request)
    major_name = major_name_url.replace('_', ' ')
    if 'Womens' in major_name:
        major_name = major_name.replace('Womens', 'Women\'s,')
    context_dict = {'major_name': major_name, 'majors': major_list}
    
    try:
        major = Major.objects.get(major_name = major_name)
        classes = Class.objects.filter(major = major)
        context_dict['classes'] = classes
        context_dict['major'] = major
    except Major.DoesNotExist:
        pass
    
    return render_to_response('class_selector/major.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('class_selector/about.html', context_dict, context)

def contact(request):
    context = RequestContext(request)
    return render_to_response('class_selector/contact.html', context_dict, context)

#def americanstudies(request):
    #context = RequestContext(request)
    #context_dict = {'major': 'American Studies'}
    #return render_to_response('class_selector/major.html', context_dict, context)

#def anthropology(request):
    #context = RequestContext(request)
    #context_dict = {'major': 'Anthropology'}
    #return render_to_response('class_selector/major.html', context_dict, context)
    