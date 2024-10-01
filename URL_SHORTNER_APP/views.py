from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import string
import random
from .models import Url  # Ensure your model is imported

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def index(request):
    short_url = None  # Initialize short_url to None to pass to the template
    error = None  # Initialize error message to None

    if request.method == "POST":
        original_url = request.POST.get('long_url')  # Ensure this matches your form input name

        if original_url:
            # Check if the URL already exists in the database
            new_url, created = Url.objects.get_or_create(original_url=original_url)

            if created:
                # Generate the shortened URL only if it’s a new entry
                new_url.short_url = generate_short_url()
                new_url.save()  # Save the short URL to the database

            # Build the full shortened URL including the domain
            short_url = request.build_absolute_uri(f'/{new_url.short_url}/')
        else:
            error = 'Please provide a valid URL.'

    return render(request,'shortener/index.html', {'short_url': short_url, 'error': error})

def redirect_url(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    return redirect(url.original_url)
