# -*- coding: utf-8 -*-

from django.db import models
from drip.models import Drip, SentDrip, QuerySetRule
from model_utils.models import TimeStampedModel


class Contact(TimeStampedModel):
    pass


class Drip(Drip):
    pass


class SentDrip(SentDrip):
    pass


class QuerySetRule(QuerySetRule):
    pass
