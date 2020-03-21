from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You wanna view a dpkg/status file?")

def files(request):
    return HttpResponse('This view is for the list of files')

def index_of_file(request, file_id):
    return HttpResponse('This view is for an index of a file, in this case a file with an id of ' + file_id)

def packages(request, file_id, package_id):
    return HttpResponse('This view is for packages within a var/lib/dpkg/status file, for a package named ' + package_id + ' in a file with an id ' + file_id)