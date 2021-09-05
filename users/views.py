from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success!')
            return reverse_lazy('/login')
        else:
            messages.error(request, 'Register error')
    else:
        form = UserRegistrationForm()
    return render(request, template_name='users/registration.html', context={"form": form})
