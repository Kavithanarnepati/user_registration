from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST'and request.FILES:
        ufdo=UserForm(request.POST)
        pfdo=ProfileForm(request.POST,request.FILES)

        if ufdo.is_valid() and pfdo.is_valid():
            MUFDO=ufo.save(commit=False)
            pw=ufdo.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfdo.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('Registrion is sucessfull')
        else:
            return HttpResponse('Invalid data')  


    return render(request,'registration.html',d)
