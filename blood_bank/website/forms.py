from django import forms
from django.contrib.auth.models import User
from  .models import Blood_donor, Message, Event, Blood_recipient
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

import datetime

CITY_CHOICES = (
    ('Akkaraipattu', 'Akkaraipattu'),
    ('Ambalangoda', 'Ambalangoda'),
    ('Ampara', 'Ampara'),
    ('Anuradhapura', 'Anuradhapura'),
    ('Avissawella', 'Avissawella'),
    ('Badulla', 'Badulla'),
    ('Balangoda', 'Balangoda'),
    ('Bandarawela', 'Bandarawela'),
    ('Battaramulla', 'Battaramulla'),
    ('Batticaloa', 'Batticaloa'),
    ('Beruwala', 'Beruwala'),
    ('Boralesgamuwa', 'Boralesgamuwa'),
    ('Chavakachcheri', 'Chavakachcheri'),
    ('Chilaw', 'Chilaw'),
    ('Colombo', 'Colombo'),
    ('Dambulla', 'Dambulla'),
    ('Dehiwala', 'Dehiwala'),
    ('Embilipitiya', 'Embilipitiya'),
    ('Eravur', 'Eravur'),
    ('Galle', 'Galle'),
    ('Gampaha', 'Gampaha'),
    ('Gampola', 'Gampola'),
    ('Hambantota', 'Hambantota'),
    ('Haputale', 'Haputale'),
    ('Hatton-Dickoya', 'Hatton-Dickoya'),
    ('Hikkaduwa', 'Hikkaduwa'),
    ('Horana', 'Horana'),
    ('Ja-Ela', 'Ja-Ela'),
    ('Jaffna', 'Jaffna'),
    ('Kadugannawa', 'Kadugannawa'),
    ('Kaduwela', 'Kaduwela'),
    ('Kalmunai', 'Kalmunai'),
    ('Kalutara', 'Kalutara'),
    ('Kandy', 'Kandy'),
    ('Kattankudi', 'Kattankudi'),
    ('Katunayake', 'Katunayake'),
    ('Kegalle', 'Kegalle'),
    ('Kesbewa', 'Kesbewa'),
    ('Kilinochchi', 'Kilinochchi'),
    ('Kinniya', 'Kinniya'),
    ('Kolonnawa', 'Kolonnawa'),
    ('Kuliyapitiya', 'Kuliyapitiya'),
    ('Kurunegala', 'Kurunegala'),
    ('Mabole', 'Mabole'),
    ('Maharagama', 'Maharagama'),
    ('Mannar', 'Mannar'),
    ('Matale', 'Matale'),
    ('Matara', 'Matara'),
    ('Minuwangoda', 'Minuwangoda'),
    ('Moneragala', 'Moneragala'),
    ('Moratuwa', 'Moratuwa'),
    ('Mount Lavinia', 'Mount Lavinia'),
    ('Mullaitivu', 'Mullaitivu'),
    ('Nawalapitiya', 'Nawalapitiya'),
    ('Negombo', 'Negombo'),
    ('Nugegoda', 'Nugegoda'),
    ('Nuwara Eliya', 'Nuwara Eliya'),
    ('Panadura', 'Panadura'),
    ('Peliyagoda', 'Peliyagoda'),
    ('Piliyandala', 'Piliyandala'),
    ('Point Pedro' , 'Point Pedro'),
    ('Polonnaruwa', 'Polonnaruwa'),
    ('Puttalam', 'Puttalam'),
    ('Ratnapura', 'Ratnapura'),
    ('Sainthamarathu', 'Sainthamarathu'),
    ('Seeduwa', 'Seeduwa'),
    ('Seethawakapura', 'Seethawakapura'),
    ('Sri Jayawardenepura Kotte', 'Sri Jayawardenepura Kotte'),
    ('Tangalle', 'Tangalle'),
    ('Thalawakele', 'Thalawakele'),
    ('Trincomalee', 'Trincomalee'),
    ('Valvettithurai', 'Valvettithurai'),
    ('Vavuniya', 'Vavuniya'),
    ('Wattala', 'Wattala'),
    ('Wattegama', 'Wattegama'),
    ('Weligama', 'Weligama'),
    )

Gender = (
    ('male', 'Male'),
    ('female', 'Female'),
)

BIRTH_YEAR_CHOICES =  [*range(1955, datetime.date.today().year+1, 1)] 

def current_year():
    return datetime.date.today().year

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save() 
            return user

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Gender', choices=Gender, widget=forms.RadioSelect, required=True)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), initial=datetime.date.today, required=True)
    nic = forms.CharField(max_length=12, required=True)
    city = forms.ChoiceField(choices=CITY_CHOICES, initial='Colombo', required=True)
    
    class Meta:
        model= Blood_donor
        fields = (
            'gender',
            'dob',
            'nic',
            'city',
        )

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
        'email',
        'first_name',
        'last_name',
        'password'
        )

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = (
            'fullname',
            'phone',
            'email',
            'subject',
            'message'
        )

    def save(self, commit=True):
        message = super(MessageForm, self).save(commit=False)
        message.fullname = self.cleaned_data['fullname']
        message.last_name = self.cleaned_data['phone']
        message.email = self.cleaned_data['email']
        message.subject = self.cleaned_data['subject']
        message.message = self.cleaned_data['message']

        if commit:
            message.save() 
            return message

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'event_name',
            'datetime',
            'venue',
            'img',
            'details',
            'description'
        )

    def save(self, commit=True):
        campaign = super(CampaignForm, self).save(commit=False)
        campaign.event_name = self.cleaned_data['event_name']
        campaign.datetime = self.cleaned_data['datetime']
        campaign.venue = self.cleaned_data['venue']
        campaign.img = self.cleaned_data['img']
        campaign.details = self.cleaned_data['details']
        campaign.description = self.cleaned_data['description']

        if commit:
            campaign.save()
            return campaign

class UpdateCampaignForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'event_name',
            'datetime',
            'venue',
            'img',
            'details',
            'description'
        )

    def save(self, commit=True):
        updatecampaign = super(UpdateCampaignForm, self).save(commit=False)
        updatecampaign.event_name = self.cleaned_data['event_name']
        updatecampaign.datetime = self.cleaned_data['datetime']
        updatecampaign.venue = self.cleaned_data['venue']
        updatecampaign.details = self.cleaned_data['details']
        updatecampaign.description = self.cleaned_data['description']

        if self.cleaned_data['img']:
            updatecampaign.img = self.cleaned_data['img']


        if commit:
            updatecampaign.save()
            return updatecampaign

DICISION_CHOICES = (
('pending', 'Pending'),
('completed', 'Completed'),
)

class UpdateRecipientForm(forms.ModelForm):
    patient_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    required_blood_group = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    units = forms.CharField (widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    hospital_name = forms.CharField (widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    hospital_address = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    doctor_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    when_required = forms.DateTimeField (widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    reason_for_blood = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}))
    status = forms.ChoiceField(choices=DICISION_CHOICES, required=True)

    class Meta:
        model = Blood_recipient
        fields = (
            'patient_name',
            'gender',
            'required_blood_group',
            'units',
            'hospital_name',
            'hospital_address',
            'city',
            'doctor_name',
            'when_required',
            'phone',
            'email',
            'reason_for_blood',
            'completed_date',
            'status',
        )
    
    def save(self, commit=True):
        updaterequired = super(UpdateRecipientForm, self).save(commit=False)

        updaterequired.completed_date = self.cleaned_data['completed_date']
        updaterequired.status = self.cleaned_data['status']

        if commit:
            updaterequired.save()
            return updaterequired
            

BLOOD_CHOICES = (
('Select blood group', 'Select blood group'),
('A+', 'A+'),
('A-', 'A-'),
('B+', 'B+'),
('B-', 'B-'),
('O+', 'O+'),
('O-', 'O-'),
('AB+', 'AB+'),
('AB-', 'AB-'),
)

UNITS_CHOICES = (
('Required units', 'Required units'),
('1', '1'),
('2', '2'),
('4', '4'),
('5', '5'),
('6', '6'),
('7', '7'),
('8', '8'),
('9', '9'),
)

class RequestForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender, widget=forms.RadioSelect, required=True)
    units = forms.ChoiceField( choices=UNITS_CHOICES, required=True)
    required_blood_group = forms.ChoiceField(choices=BLOOD_CHOICES, required=True)
    city = forms.ChoiceField(choices=CITY_CHOICES, required=True, initial='Colombo')

    class Meta:
        model = Blood_recipient
        fields = (
            'patient_name',
            'gender',
            'required_blood_group',
            'units',
            'hospital_name',
            'hospital_address',
            'city',
            'doctor_name',
            'when_required',
            'phone',
            'email',
            'reason_for_blood'
        )

    def save(self, commit=True):
        required = super(RequestForm, self).save(commit=False)
        required.patient_name = self.cleaned_data['patient_name']
        required.gender = self.cleaned_data['gender']
        required.required_blood_group = self.cleaned_data['required_blood_group']
        required.units = self.cleaned_data['units']
        required.hospital_name = self.cleaned_data['hospital_name']
        required.hospital_address = self.cleaned_data['hospital_address']
        required.city = self.cleaned_data['city']
        required.doctor_name = self.cleaned_data['doctor_name']
        required.when_required = self.cleaned_data['when_required']
        required.phone = self.cleaned_data['phone']
        required.email = self.cleaned_data['email']
        required.reason_for_blood = self.cleaned_data['reason_for_blood']

        if commit:
            required.save()
            return required

