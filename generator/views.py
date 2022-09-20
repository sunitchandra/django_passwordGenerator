import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('Hello World from django..!!')
    return render(request, 'generator/home.html')

def password(request):
    length =  int(request.GET.get("dd_length"))
    characters = list("abcdefghijklmnopqrstuvwxyz")
    
    if request.GET.get("chkbx_uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("chkbx_specialchars"):
        characters.extend(list('!@#$%^&*()_+-=/.,<>;"":}{][\|'))

    if request.GET.get("chkbx_numbers"):
        characters.extend(list("0123456789"))

    thepassword = ""

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"generatedPass":thepassword })

def about(request):
    return render(request, "generator/about.html")

"""
def eggs(request):
    
    return HttpResponse('''
    <html>
        <head>
            <title>Eggs</title>
        </head>
    </head>
    <body>
        <h1>Eggs are Awesome...!!!</h1>
    </body>
    </html>
    '''
    )
    
    return render(request, "generator/eggs.html", {"text": "Eat Eggs Daily :) "})
"""