from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CollaborateRequestForm

def collaborate_view(request):
    if request.method == "POST":
        form = CollaborateRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Collaboration request received! I endeavor to respond within 2 working days.")
            return redirect('collaborate_success')  # Redirect to success page
    else:
        form = CollaborateRequestForm()  # Create an empty form

    return render(request, 'contact/collaborate.html', {'form': form})

def collaborate_success(request):
    return render(request, 'contact/collaborate_success.html')