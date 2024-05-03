from django.shortcuts import render,redirect
from .models import Produit,Commande,Client
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def blog(request):
    return render(request,'pages/blog.html')

def blogi(request):
    return render(request,'pages/blogi.html')

def cart(request):
    return render(request,'pages/cart.html')

def checkout(request):
    return render(request,'pages/checkout.html')




def checkout_c(request):
     if request.method == 'POST':
        name = request.POST.get('lastname')
        prenom = request.POST.get('firstname')
        email = request.POST.get('emailaddress')
        paypal = request.POST.get('postcodezip')
        ville = request.POST.get('country')
        adresse = request.POST.get('streetaddress')
        # Create a new patient entry in the database using the Patient model
        #client = Client(name=name, prenom=prenom,email=email,paypal=paypal,ville=ville,adresse=adresse)
        #client.save()
        client = Client.objects.create(name=name, prenom=prenom,email=email,paypal=paypal,ville=ville,adresse=adresse)
        client.save()
        return HttpResponse("Data successfully inserted!")
     else:
         return HttpResponse("Data successfully inserted!")

   
        


     





def contact(request):
    return render(request,'pages/contact.html')

def product(request):
    return render(request,'pages/product.html')

def shop(request):
    return render(request,'pages/shop.html',{'produit':Produit.objects.all()})



