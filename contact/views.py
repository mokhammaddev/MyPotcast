from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    form = ContactForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ContactForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.name = request.user.profile.full_name
                obj.save()
                return redirect('.')
        else:
            form = ContactForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'mypotcast/contact.html', ctx)


# form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if request.user.is_authenticated:
#             obj = form.save(commit=False)
#             obj.name_id = request.user.id
#             obj.save()
#         if form.is_valid():
#             form.save()