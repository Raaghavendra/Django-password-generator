from typing import Generator
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(Request):
    return render(Request,'generator/home.html')

def about(Request):
    return render(Request,'generator/about.html')

def password(Request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    spl_char = list('!@#$%^&*()-_=+')
    l = int(Request.GET.get('l'))
    if(l<6):
        return HttpResponseBadRequest("<h1>Insufficient length for password</h1>")
    u = Request.GET.get('u')
    s = Request.GET.get('s')
    n = Request.GET.get('n')
    gp = ''
    for i in range(l):
        gp += random.choice(characters)
    n1 = -1
    n2 = -1
    gp = list(gp)
    if ( u == "on" ):     
        n1 = random.randint(0,l-1)
        gp[n1] = gp[n1].upper()

    if ( s == "on" ):
        while (True):
            n2 = random.randint(0,l-1)
            if (n2 != n1): break
        sc = random.randint(0,len(spl_char)-1)
        gp[n2] = spl_char[sc]

    if ( n == "on" ):
        while (True):
            n3 = random.randint(0,l-1)
            if (n3 != n1 and n3 != n2): break
        gp[n3] = str(n3)
    gp = ''.join(gp)
    return render(Request, 'generator/password.html', {'password' : gp})