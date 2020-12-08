from website.viewsets import Blood_donorViewset
from website.viewsets import Blood_recipientViewset
from website.viewsets import EventViewset
from website.viewsets import MessageViewset
from website.viewsets import CityViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blood_donor',Blood_donorViewset)
router.register('blood_recipient',Blood_recipientViewset)
router.register('event',EventViewset)
router.register('message',MessageViewset)
router.register('city',CityViewset)