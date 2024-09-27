from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    fruits = ['Mango', 'Apple', 'Oranges']
    brands = ['Google', 'DELL', 'Microsoft']
    # Create an empty dictionary
    content = {}
    content['fruits'] = fruits
    content['brands'] = brands
    content['title'] = 'Home'
    return render(request, 'home/home.html', content)

def contact(request):
    content = {}
    content['message_data'] = None
    content['title'] = 'Contact'
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message_text = request.POST['message_text']

        content['message_data'] = f"Name: {name}. Email: {email}. Message: {message_text}"
    return render(request, 'home/contact.html', content)

def about(request):
    content = {}
    content['title'] = 'About'
    return render(request, 'home/about.html', content)