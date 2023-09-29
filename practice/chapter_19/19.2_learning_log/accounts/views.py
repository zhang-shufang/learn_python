from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Show empty register form.
        form = UserCreationForm()
    else:
        # Process the filled from.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Let user login automatically and redirect to main page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Show empty form or indicate form invalid
    context = {'form': form}
    return render(request, 'registration/register.html', context)