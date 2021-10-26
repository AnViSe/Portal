from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from apps.account.gravatar import email_to_gravatar
from apps.references.models.employee import Employee
from apps.references.models.subdivision import Subdivision
from extensions.validators import validate_image, validate_size


def _user_directory_path(instance, filename):
    return f'profiles/{instance.username}/{filename}'


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=_user_directory_path,
                               default='avatars/default.png',
                               validators=[validate_image, validate_size],
                               verbose_name='Аватар')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Сотрудник')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='Подразделение')

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def person_name(self):
        return self.get_person_name()

    def get_person_name(self):
        if self.employee and self.employee.person:
            return self.employee.person.name_lfm
        else:
            return self.get_username()

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url') and self.avatar_exists():
            # print('Аватар есть: ', self.avatar.url)
            return self.avatar.url
        else:
            email = self.email if self.pk else "default.user@example.com"
            # email = value_without_invalid_marker(email)
            # print('Аватара нет: ', email)
            return email_to_gravatar(email, settings.DEFAULT_AVATAR_URL)

    def avatar_exists(self):
        return self.avatar and self.avatar.storage.exists(self.avatar.name)


@receiver(post_save, sender=CustomUser)
def user_save(sender, instance, created, **kwargs):
    if not created:
        cache.delete(f'user_perms_{instance.id}')


@receiver(pre_delete, sender=CustomUser)
def user_delete(sender, instance, **kwargs):
    cache.delete(f'user_perms_{instance.id}')
