from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib.auth.models import Permission
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _

from wagtailcrm import urls
from wagtail.wagtailadmin.menu import MenuItem
from wagtail.wagtailcore import hooks


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^crm/', include(urls, app_name='wagtailcrm', namespace='wagtailcrm')),
    ]


class CrmMenuItem(MenuItem):
    def is_shown(self, request):
        return True
        # return (
        #     request.user.has_perm('wagtailcrm.add_contact') or
        #     request.user.has_perm('wagtailcrm.change_contact') or
        #     request.user.has_perm('wagtailcrm.delete_contact')
        # )


@hooks.register('register_settings_menu_item')
def register_crm_menu_item():
    return CrmMenuItem(
        _('Contacts'),
        urlresolvers.reverse('wagtailcrm:index'),
        classnames='icon icon-pick', order=1000
    )
