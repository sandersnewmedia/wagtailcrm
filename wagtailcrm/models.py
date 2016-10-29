# -*- coding: utf-8 -*-
import os, json, requests

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


class Contact(models.Model):
    """
    Base contact model
    """
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, default='')
    about = models.TextField(default='', blank=True, null=True)
    content_id = models.CharField(max_length=2, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_contacted = models.DateTimeField(null=True)
    last_modified = models.DateTimeField(null=True)


    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('wagtailcrm:contact_detail', kwargs={'pk': str(self.id)})

    def notify(self):
        if settings.HUBSPOT_ENABLED:
            email = settings.FROM_EMAIL
            reply_email = settings.FROM_EMAIL
            message = u''
            for field in Contact._meta.get_fields():
                message += u'{}: {}<br />'.format(field, self.__dict__.get(field.name))
            send_mail(u'Contact Inquiry', message, email, [reply_email], fail_silently=True, html_message=message)

    def create_in_hubspot(self):
        url = u"https://api.hubapi.com/contacts/v1/contact/?hapikey={}".format(settings.HUBSPOT_API_KEY)
        payload = {
            'properties': [
                {
                    'property': 'firstname',
                    'value': self.firstname
                },
                {
                    'property': 'lastname',
                    'value': self.lastname
                },
                {
                    'property': 'email',
                    'value': self.email
                },
                {
                    'property': 'phone',
                    'value': self.phone_number
                }
            ]
        }
        response = requests.post(url, data=json.dumps(payload)) # TODO: add exception handling


@receiver(post_save, sender=Contact)
def created_contact(sender, instance, created, **kwargs):
    if created:
        instance.notify()
        instance.create_in_hubspot()
