from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.gravatar import email_to_gravatar
from extensions.validators import validate_image, validate_size


def user_directory_path(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'


class CustomUser(AbstractUser):
    pass

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='пользователь')
    avatar = models.ImageField(upload_to=user_directory_path,
                               default='avatars/default.png',
                               validators=[validate_image, validate_size],
                               verbose_name='аватар')

    class Meta:
        db_table = 'auth_user_profile'
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return self.user.username

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url') and self.avatar_exists():
            return self.avatar.url
        else:
            email = self.user.email if self.user_id else "default.user@example.com"
            # email = value_without_invalid_marker(email)
            return email_to_gravatar(email, settings.DEFAULT_AVATAR_URL)

    def avatar_exists(self):
        return self.avatar and self.avatar.storage.exists(self.avatar.name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
