from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.sessions.models import Session
from django.db import models


from apps.account.gravatar import email_to_gravatar
from apps.references.models.employee import Employee
from apps.references.models.subdivision import Subdivision
from core.fields import CreateDateTimeField
from extensions.validators import validate_image, validate_size


def _user_directory_path(instance, filename):
    return f'profiles/{instance.username}/{filename}'


class PersonManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().select_related('employee', 'employee__person', 'subdivision')


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=_user_directory_path,
                               default='avatars/default.png',
                               validators=[validate_image, validate_size],
                               verbose_name='Аватар')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='users',
                                 verbose_name='Сотрудник')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='users',
                                    verbose_name='Подразделение')
    objects = PersonManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def person_name(self):
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


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='sessions',
                             verbose_name='Пользователь')
    session = models.OneToOneField(Session, on_delete=models.CASCADE,
                                   verbose_name='Сессия')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL,
                                    blank=True, null=True,
                                    related_name='+',
                                    verbose_name='Подразделение')
    ipaddress = models.CharField(max_length=15,
                                 verbose_name='IP адрес')
    dt_start = CreateDateTimeField()

    class Meta:
        db_table = 'auth_user_session'
        verbose_name = 'сеанс пользователя'
        verbose_name_plural = 'сеансы пользователей'
