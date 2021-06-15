from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, TemplateView
from . import forms
from .models import Emp, Emp_Profile
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('<h1>Hello</h1>')


emp_id = 0


def user_logout(request):
    logout(request)
    return redirect('/login')


def register(request):
    fg = forms.Emp_form()
    fg1 = forms.Emp_prof_from()
    global emp_id
    if request.method == 'POST':
        form = forms.Emp_form(request.POST)
        pr_form = forms.Emp_prof_from(request.POST, request.FILES)
        # print('hi')
        print(form.is_valid(), pr_form.is_valid())
        print(form.errors)
        if form.is_valid() and pr_form.is_valid():
            # user = form.save()
            emp_name = form.cleaned_data['emp_name']
            emp_email = form.cleaned_data['emp_email']
            emp_password = form.cleaned_data['emp_password']
            if (len(Emp.objects.all()) == 0):
                emp_id = 1000
            else:
                e = Emp.objects.all()
                emp_id = e[len(e) - 1].emp_id + 1

            Emp(emp_id=emp_id, emp_name=emp_name,
                emp_email=emp_email, emp_password=emp_password).save()
            empObj = Emp.objects.get(emp_id=emp_id)
            fb_url = pr_form.cleaned_data['fb_url']
            lk_url = pr_form.cleaned_data['lk_url']

            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']

            Emp_Profile(emp_pro_id=empObj, fb_url=fb_url,
                        lk_url=lk_url, profile_pic=profile_pic).save()

            return redirect('/thankyou')
        else:
            return HttpResponse('ERROR')

    return render(request, 'Emp/Signup.html', {'form': fg, 'form1': fg1})


def prolink(request):
    ids = Emp.objects.all()
    id1 = Emp_Profile.objects.all()
    d = {}
    l1 = []
    l = []
    for id in ids:
        idT = id.emp_id
        idD = Emp_Profile.objects.get(emp_pro_id=idT)
        profPic = idD.profile_pic
        l.append([idT, profPic])
    d['id'] = l
    return render(request, 'Emp/gg.html', d)


def displayDet(request, myid):
    a1 = Emp.objects.get(emp_id=myid)
    emp_password = a1.emp_password
    emp_email = a1.emp_email
    emp_name = a1.emp_name
    a2 = Emp_Profile.objects.get(emp_pro_id=a1)
    profilePic = a2.profile_pic
    fburl = a2.fb_url
    lkurl = a2.lk_url
    d1 = {
        'pwd': emp_password,
        'email': emp_email,
        'name': emp_name,
        'profilePic': profilePic,
        'fburl': fburl,
        'lkurl': lkurl
    }

    return render(request, 'Emp/displayDet.html', d1)


def thankyou(request):
    d = {
        'emp_id': emp_id
    }
    return render(request, 'Emp/Thankyou.html', d)


def login1(request):
    lg = forms.login1()
    next = request.GET.get('next')
    form = forms.login1(request.POST)
    if request.method == "POST" and form.is_valid():
        Email = form.cleaned_data['email']
        Password = form.cleaned_data['password']
        print('Email :' + Email)
        print('Password :' + Password)
        if Emp.objects.filter(emp_email=Email, emp_password=Password).exists():

            obj = Emp.objects.filter(emp_email=Email, emp_password=Password)[0]
            empid = obj.emp_id
            if(next):
                return redirect(next)
            return redirect('/id/'+str(empid) + '')

        else:
            raise forms.ValidationError("User does not exist")

    return render(request, 'Emp/login.html', {'form': lg})
