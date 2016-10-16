# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^contact/~create/$",
        view=views.contactCreateView.as_view(),
        name='contact_create',
    ),
    url(
        regex="^contact/(?P<pk>\d+)/~delete/$",
        view=views.contactDeleteView.as_view(),
        name='contact_delete',
    ),
    url(
        regex="^contact/(?P<pk>\d+)/$",
        view=views.contactDetailView.as_view(),
        name='contact_detail',
    ),
    url(
        regex="^contact/(?P<pk>\d+)/~update/$",
        view=views.contactUpdateView.as_view(),
        name='contact_update',
    ),
    url(
        regex="^contact/$",
        view=views.contactListView.as_view(),
        name='contact_list',
    ),
	]
