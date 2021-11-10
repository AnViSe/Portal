import logging

from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import Group
from django.contrib.sessions.models import Session
from django.core.cache import cache
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from apps.account.models import CustomUser, UserSession
from extensions.utils import get_client_ip

logger = logging.getLogger('django')


@receiver(post_save, sender=CustomUser)
def user_save(sender, instance, created, **kwargs):
    if not created:
        cache.delete(f'perms_user_{instance.id}')


@receiver(pre_delete, sender=CustomUser)
def user_delete(sender, instance, **kwargs):
    cache.delete(f'perms_user_{instance.id}')


@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    logger.warning(f'Вход пользователя: {user.username}')
    # Удаляем другие сессии
    Session.objects.filter(usersession__user=user).delete()

    # Сохраняем текущую сессию
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user,
        subdivision=user.subdivision,
        session=Session.objects.get(pk=request.session.session_key),
        ipaddress=get_client_ip(request),
    )


@receiver(user_signed_up)
def append_to_def_group(sender, user, request, **kwargs):
    """При регистрации пользователя добавляем его в группу 1 (Обычный пользователь)"""
    logger.warning(f'Регистрация пользователя: {user.username}')
    try:
        group = Group.objects.get(pk=1)
        user.groups.add(group)
    except Group.DoesNotExist:
        pass
