from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from django.shortcuts import reverse
from . import forms
from . import models
# Create your views here.
def index(request):

    if request.method == "POST":
        form = forms.EmployeerForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('app:show'))

            except:
                print(form.errors)
    else:
        form = forms.EmployeerForm()
    return render(request,'employeer.html',{'form':form})
    
def show(request):
    employeers = models.Employeer.objects.all()
    return render(request,'show.html',{'employeers':employeers})

def update(request,id):

    employeer = models.Employeer.objects.get(id=id)

    if request.method == "POST":
        form = forms.EmployeerForm(request.POST,request.FILES,instance = employeer)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse("app:show"))
            except:
                print(form.errors)
    else:
        form = forms.EmployeerForm(instance = employeer)
        return render(request,"update.html",{'form':form})

def delete(request,id):
    employeer = models.Employeer.objects.get(id=id)
    employeer.delete()
    return HttpResponseRedirect(reverse("app:show"))
