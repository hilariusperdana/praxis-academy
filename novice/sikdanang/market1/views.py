from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.
from .models import RegBrg
from .handler import handle_uploaded_file

def home_screen(req):
    register = RegBrg.objects.all()
    return render(req, 'market/index.html', {
        'data': register,
    })

def hapus(req, id):
    dt = RegBrg.objects.get(id=id)
    dt.delete()
    return redirect('/market/')

def upload_file(req):
    if req.method == 'POST':
        form = UploadFileForm(req.POST, req.FILES)
        if form.is_valid():
            handle_uploaded_file(req.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(req, 'upload.html', {'form': form})