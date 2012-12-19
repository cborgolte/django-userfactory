django-userfactory
==================


Using [factory_boy](https://github.com/rbarrois/factory_boy) to create User instances.

Provides users with different name attributes per call.
Factories exist for general user, staff user and admins.

Example:

```python
from userfactory.userfactory import UserFactory, StaffUserFactory, AdminUserFactory
user = UserFactory()
print user.__dict__

{'_state': <django.db.models.base.ModelState at 0x22b0910>,
 'date_joined': datetime.datetime(2012, 12, 19, 23, 4, 50, 238757, tzinfo=<UTC>),
 'email': 'lorellereiners@users-fakexyz123oo.com',
 'first_name': u'Lorelle',
 'id': 8,
 'is_active': True,
 'is_staff': False,
 'is_superuser': False,
 'last_login': datetime.datetime(2012, 12, 19, 23, 4, 50, 238685, tzinfo=<UTC>),
 'last_name': u'Reiners',
 'password': 'pbkdf2_sha256$10000$DLtc4vBFEsZY$5K53yZkVihNkADtY39JJVyKwfM8tNpZX2d6lSZgHt3k=',
 'username': 'lorellereiners'}
```
