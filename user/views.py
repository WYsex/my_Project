from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'user/base.html',locals())

def index(request):
    return render(request,'user/index.html',locals())

def about(request):
    return render(request,'user/about.html',locals())

def Contact(request):
    return render(request,'user/contact.html',locals())

def propertyGgrid(request):
    return render(request,'user/property-grid.html',locals())

def propertySingle(request):
    return render(request,'user/property-single.html',locals())

def blogGrid(request):
    return render(request,'user/blog-grid.html',locals())

def blogSingle(request):
    return render(request,'user/blog-single.html',locals())

def agentsGrid(request):
    return render(request,'user/agents-grid.html',locals())

def agentSingle(request):
    return render(request,'user/agent-single.html',locals())