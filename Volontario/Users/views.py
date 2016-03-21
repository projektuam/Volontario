from Users.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import redirect 
from django.shortcuts import render, get_object_or_404

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            tel=form.cleaned_data['tel'],
            indeks=form.cleaned_data['indeks']
            )
            return redirect('Event.views.event_list')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )

#############################################################################################################
def user_logout(request):

    logout(request)

   
    return redirect('Event.views.event_list')
#############################################################################
def user_account(request):
    current_user= request.user

    user=get_object_or_404(User,id=current_user.id)
    
    return render(request, 'users/account.html', { 'user': user } )

def setting_account(request,usr):
    cur_user = get_object_or_404(User,id=usr)
    users = User.objects.all
    return render(request, 'users/list.html',{'users' : users, 'cur_user':cur_user})



def user_list(request):
    users = User.objects.all

    return render(request, 'users/list.html', {'users' : users})

def user_edit(request, usr):
    user = get_object_or_404(User,id=usr)
    users = User.objects.all
    cur_user = request.user
    if request.method == "POST":
        form = UpdateProfileForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save(update_fields=['first_name','last_name','email','tel','indeks','is_staff','is_active'])
            
            return render(request, 'users/list.html',{'users' : users, 'cur_user':cur_user})
    else:
        form = UpdateProfileForm(instance=user)
    return render(request, 'users/user_edit.html', {'form': form})
def user_remove(request,usr):
    user = get_object_or_404(User,id=usr)
    users = User.objects.all
    user.delete()
    return render(request, 'users/list.html',{'users' : users})
