from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .forms import (
    RegistrationForm,
    EditProfileForm,
    ProfileForm,
    MessageForm,
    CampaignForm,
    RequestForm,
    UpdateCampaignForm,
    UpdateRecipientForm,
)
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from website.models import Message, Event, Blood_recipient, Blood_donor
from django.contrib import messages

def index(request):
    campaign = Event.objects.order_by('datetime')
    campaigns = Event.objects.order_by('-datetime')[:3]
    
    args = {'campaign': campaign, 'campaigns': campaigns, 'nbar': 'index'}
    return render(request, 'website/index.html', args )

def about(request):
    return render(request, 'website/about.html', {'nbar': 'about'} )

def contact(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            return redirect('contact')

        else:
            args = {'message_form': message_form}
            return render(request, 'website/contact.html', args)

    else:
        message_form = MessageForm()

        args = {'message_form': message_form, 'nbar': 'contact'}
        return render(request, 'website/contact.html', args)

def preregister(response):
    return render(response, 'website/preregister.html')

def signup(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            profile_form = ProfileForm(request.POST)

            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('sign-in')

            else:
                form = RegistrationForm()
                profile_form = ProfileForm()
                args = {'form': form, 'profile_form': profile_form} 
                return render(request, 'website/sign-up.html', args)
        
        else:
            form = RegistrationForm()
            profile_form = ProfileForm()
            args = {'form': form, 'profile_form': profile_form} 
            return render(request, 'website/sign-up.html', args)

def campaign(request):
    campaign = Event.objects.all()
    args = {'campaign': campaign}
    return render(request, 'website/campaign.html', args)

def v_campaign(request, id):
    campaign = Event.objects.get(id=id)
    campaign_latest = Event.objects.order_by('-datetime')[:3]
    args = {'campaign':campaign, 'campaign_latest': campaign_latest}
    return render(request, 'website/v_campaign.html', args)

def request_form(request):
    if request.method == 'POST':
        request_blood = RequestForm(request.POST)
        if request_blood.is_valid():
            request_blood.save()
            return redirect('index')

        else:
            args = {'request_blood': request_blood}
            return render(request, 'website/request-blood.html', args)

    else:
        request_blood = RequestForm()
        args = {'request_blood': request_blood}
        return render(request, 'website/request-blood.html', args)

@login_required
def profile(request):
    args = {'user': request.user, 'nbar': 'profile'}
    return render(request, 'website/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
        else:
            args = {'form': form}
            return render(request, 'website/edit.html', args)

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'website/edit.html',args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'website/change_password.html',args)

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    if request.method == 'GET':
        message = Message.objects.all()

        args = {'message': message, 'nbar': 'dashboard'}
        return render(request, 'website/dashboard.html', args)

@user_passes_test(lambda u: u.is_superuser)
def message(request):

    if request.method == 'GET':
        message = Message.objects.all()
        args = {'message': message}
        return render(request, 'website/message.html', args)

@user_passes_test(lambda u: u.is_superuser)
def delete_message(request, id):
    message = Message.objects.get(id=id)
    if request.method == 'POST':
        message.delete()
        return redirect('message')

    args = {'item': message}
    return render(request, 'website/delete_message.html', args)

@user_passes_test(lambda u: u.is_superuser)
def view_message(request, id):
    message =  Message.objects.get(id=id)
    args = {'message': message} 
    return render(request, 'website/view_message.html', args)

@user_passes_test(lambda u: u.is_superuser)
def view_campaign(requst):
    campaign = Event.objects.all()

    args = {'campaign': campaign}
    return render(requst, 'website/admin-campaign.html', args)

@user_passes_test(lambda u: u.is_superuser)
def add_campaign(request):
    if request.method == 'POST':
        campaign_form = CampaignForm(request.POST, request.FILES)
        if campaign_form.is_valid():
            campaign_form.save()
            return redirect ('../')

        else:
            args = {'campaign_form': campaign_form}
            return render(request, 'website/add-campaign.html', args)

    else:
        campaign_form = CampaignForm()
        args = {'campaign_form': campaign_form}
        return render(request, 'website/add-campaign.html', args)

@user_passes_test(lambda u: u.is_superuser)
def delete_campaign(request, id):
    campaign = Event.objects.get(id=id)
    if request.method == 'POST':
        campaign.delete()
        return redirect('admin-campaign')

    args = {'campaign': campaign}
    return render(request, 'website/delete_campaign.html', args)

@user_passes_test(lambda u: u.is_superuser)
def need_blood(request):
    needblood = Blood_recipient.objects.all()

    args = {'needblood': needblood}
    return render(request, 'website/need_blood.html', args)

@user_passes_test(lambda u: u.is_superuser)
def edit_recipient(request, id):

    args = {}

    recipient = Blood_recipient.objects.get(id=id)
    form = UpdateRecipientForm(instance=recipient)

    if request.method == 'POST':
        form = UpdateRecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            form.save()
            return redirect('../../')
            
        
        else:
            args = {'form': form}
            return render(request, 'website/edit_recipient.html', args)

    else:
        form = UpdateRecipientForm(instance=recipient)
        args = {'form': form}
        return render(request, 'website/edit_recipient.html',args)

@user_passes_test(lambda u: u.is_superuser)
def delete_recipient(request, id):
    recipient = Blood_recipient.objects.get(id=id)
    if request.method == 'POST':
        recipient.delete()
        return redirect('../../')

    args = {'recipient': recipient}
    return render(request, 'website/delete_recipient.html', args)


@user_passes_test(lambda u: u.is_superuser)
def edit_campaign(request, id):
    args = {}

    campaign = Event.objects.get(id=id)
    form = UpdateCampaignForm(instance=campaign)

    if request.method == 'POST':
        form = UpdateCampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('../../')
            
        
        else:
            args = {'form': form}
            return render(request, 'website/edit-campaign.html', args)

    else:
        form = UpdateCampaignForm(instance=campaign)
        args = {'form': form}
        return render(request, 'website/edit-campaign.html',args)


@user_passes_test(lambda u: u.is_superuser)
def blood_donor(request):

    donor = User.objects.all().exclude(is_superuser=True)
    args = {'donor': donor}
    return render(request, 'website/blood_donor.html', args)

@user_passes_test(lambda u: u.is_superuser)
def view_donor(request, id):
    donor = User.objects.exclude(is_superuser=True).get(id=id)
    args = {'donor': donor} 
    return render(request, 'website/view_donor.html', args)