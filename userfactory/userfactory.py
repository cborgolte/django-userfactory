#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from django.contrib.auth.models import User
from .firstnames import FIRSTNAMES
from .lastnames import LASTNAMES


class UserFactory(factory.Factory):

    FACTORY_FOR = User
    DOMAIN = 'users-fakexyz123oo.com'

    first_name = factory.LazyAttribute(lambda a: FIRSTNAMES.next())
    last_name = factory.LazyAttribute(lambda a: LASTNAMES.next())
    username = factory.LazyAttribute(lambda a: (a.first_name + a.last_name)
                                     .encode('ascii', 'ignore')
                                     .replace(' ', '')
                                     .lower()[:30])
    email = factory.LazyAttribute(lambda a: '{0}@{1}'.format(a.username,
                                                             a.DOMAIN))

    @classmethod
    def _prepare(cls, create, **kwargs):
        kwargs.pop('DOMAIN')
        password = kwargs.pop('password', 'secret')
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class StaffUserFactory(UserFactory):
    DOMAIN = 'staff-fakexyz123oo.com'
    is_staff = True


class AdminUserFactory(UserFactory):
    DOMAIN = 'admin-fakexyz123oo.com'
    is_staff = True
    is_superuser = True
