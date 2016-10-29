# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Contact,
)

FIELDS = ('firstname', 'lastname', 'phone_number', 'email')

class ContactCreateView(CreateView):
    model = Contact
    fields = FIELDS


class ContactDeleteView(DeleteView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact
    fields = FIELDS


class ContactUpdateView(UpdateView):
    model = Contact
    fields = FIELDS


class ContactListView(ListView):
    model = Contact

