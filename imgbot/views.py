from django.shortcuts import render, redirect
from django.http import JsonResponse
# import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt  # Handle CSRF protection


# Create your views here.
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        image = request.FILES.get('image')  # Access uploaded image
        if image:
            chat = Chat(user=request.user, image=image, created_at=timezone.now())
            chat.save()

            # Process the image using appropriate libraries (e.g., Pillow)
            # ... (your image processing logic here)

            # Generate AI chatbot response based on image content (replace with your implementation)
            response = "This is a response based on the uploaded image."
            chat.response = response
            chat.save()

            return JsonResponse({'message': 'Image uploaded successfully!', 'response': response})
        else:
            return JsonResponse({'error': 'Please upload an image.'})

    return render(request, 'chatbot.html', {'chats': chats})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')