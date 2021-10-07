from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.gravatar import email_to_gravatar
from apps.references.models.employee import Employee
from apps.references.models.subdivision import Subdivision
from extensions.validators import validate_image, validate_size


def _user_directory_path(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'


class CustomUser(AbstractUser):
    employee = models.ForeignKey(Employee, verbose_name='сотрудник',
                                 on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='users')
    subdivision = models.ForeignKey(Subdivision, verbose_name='подразделение',
                                    on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='users')
    avatar = models.ImageField(upload_to=_user_directory_path,
                               default='avatars/default.png',
                               validators=[validate_image, validate_size],
                               verbose_name='аватар')

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url') and self.avatar_exists():
            print('Аватар есть: ', self.avatar.url)
            return self.avatar.url
        else:
            email = self.email if self.pk else "default.user@example.com"
            # email = value_without_invalid_marker(email)
            print('Аватара нет: ', email)
            return email_to_gravatar(email, settings.DEFAULT_AVATAR_URL)

    def avatar_exists(self):
        return self.avatar and self.avatar.storage.exists(self.avatar.name)
