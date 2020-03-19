from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.urls import reverse



def index(request):
    return HttpResponse("Hello, world. You wanna upload something?")


class UploadView(FormView):
    template_name = 'uploader/form.html'
    form_class = UploadFileForm
    success_url = '/success/'

    def get_success_url(self):                           
        return reverse('home')



'''
    if request.method == 'POST':
        print('woop woop i am a dollar')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'uploader/upload.html', {'form': form})
'''