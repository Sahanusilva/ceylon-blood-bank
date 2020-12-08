from django.contrib import admin
from website.models import Blood_donor
from website.models import Blood_recipient
from website.models import Event
from website.models import Message
from website.models import City

admin.site.register(Blood_donor)
admin.site.register(Blood_recipient)
admin.site.register(Event)
admin.site.register(Message)
admin.site.register(City)