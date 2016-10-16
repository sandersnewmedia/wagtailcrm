# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	contact,
)


class contactCreateView(CreateView):

    model = contact


class contactDeleteView(DeleteView):

    model = contact


class contactDetailView(DetailView):

    model = contact


class contactUpdateView(UpdateView):

    model = contact


class contactListView(ListView):

    model = contact

