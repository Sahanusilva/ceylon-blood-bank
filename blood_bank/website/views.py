from django.shortcuts import render

def index(response):
    return render(response, 'website/index.html', {'nbar': 'index'} )

def about(response):
    return render(response, 'website/about.html', {'nbar': 'about'} )

def contact(response):
    return render(response, 'website/contact.html', {'nbar': 'contact'} )

def preregister(response):
    return render(response, 'website/preregister.html')

def requestblood(response):
    return render(response, 'website/request-blood.html')

# def signin(response):
#     return render(response, 'website/sign-in.html')
    
def signup(response):
    return render(response, 'website/sign-up.html')