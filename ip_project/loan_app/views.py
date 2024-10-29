from django.shortcuts import render , redirect
from .forms import LenderSignupForm , BorrowerSignupForm
from django.contrib.auth.models import Group 
from django.contrib.auth import login as auth_login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'POST':
        if 'author-btn' in request.POST:
            form = LenderSignupForm(request.POST)
            group_name = 'Lenders' 
            lender_form = form  
            borrower_form = BorrowerSignupForm() 
        else:
            form = BorrowerSignupForm(request.POST)
            group_name = 'Borrowers' 
            lender_form = form  
            borrower_form = LenderSignupForm()

        if form.is_valid():
            user = form.save(commit=False)
            user.save() 
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            return redirect('login_view')  
    else:
        
        lender_form = LenderSignupForm()
        borrower_form = BorrowerSignupForm()

    
    return render(request, 'sign_in.html', {
        'lender_form': lender_form,
        'borrower_form': borrower_form,
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.groups.filter(name='Lenders').exists():
                return redirect('lender_dashboard')  
            elif user.groups.filter(name='Borrowers').exists():
                return redirect('borrower_dashboard')
            else:
                return redirect('home')
        else:
            error_message = "Username or Password is Invalid"
            return render(request, 'login.html', {'form': form, 'error': error_message})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def lender_dashboard(request):
    return render(request , 'lender_view.html')

@login_required
def borrower_dashboard(request):
    return render(request , 'borrower_view.html')