from rest_framework import serializers

from wagtailcrm.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
