# -*- coding: UTF-8 -*-
# pip install fabric3
# https://adw0rd.com/2012/8/14/python-fabric/
# https://github.com/fabtools/fabtools
# https://jenyay.net/Programming/Fabric
import os

from dotenv import load_dotenv
from fabric.api import run, env, task, prefix, cd, sudo


def production_env():
    load_dotenv()
    env.user = os.environ.get('UNIX_USER')
    env.password = os.environ.get('UNIX_PASS')
    # env.shell = 'sh -c'
    env.host_string = os.environ.get('UNIX_HOST')
    # Путь до каталога с проектами (на сервере)
    env.portal_root = '/var/www/sites/portal'
    # Путь до каталога проекта (на сервере)
    env.project_root = '/var/www/sites/portal/bp'
    # Путь до python (на сервере)
    env.python = '/var/www/sites/venv/bin/python'
    # Активация виртуального окружения
    env.venv_activate = 'source /var/www/sites/venv/bin/activate'


def backup():
    print('Run backup...')
    print('Ok')


@task
def runls():
    production_env()
    run('ls')


@task
def pip_list():
    """Просмотр установленных пакетов в проекте"""
    production_env()
    with prefix(env.venv_activate):
        run('pip3 list')
        run('deactivate')


# fab pip_install:'Django'
@task
def pip_install(package=None):
    """Установка пакета по имени"""
    if package:
        production_env()
        with prefix(env.venv_activate):
            run(f'pip3 install {package}')
            run('deactivate')
    else:
        raise ValueError('Укажите имя пакета')


@task
def pip_update(package=None):
    """Обновление пакета по имени"""
    if package:
        production_env()
        with prefix(env.venv_activate):
            run(f'pip3 install -U {package}')
            run('deactivate')
    else:
        raise ValueError('Укажите имя пакета')


@task
def pip_uninstall(package=None):
    """Удаление пакета по имени"""
    if package:
        production_env()
        with prefix(env.venv_activate):
            run(f'pip3 uninstall {package}')
            run('deactivate')
    else:
        raise ValueError('Укажите имя пакета')


@task
def git_update(reload=True, migrate=False):
    """Обновление репозитория
     Выполнение миграций
     Перезагрузка gunicorn"""
    production_env()
    with cd(env.portal_root):
        run('git pull')
    if migrate:
        with cd(env.project_root):
            with prefix(env.venv_activate):
                run('python3 manage.py migrate')
                run('deactivate')
    if reload:
        sudo('systemctl daemon-reload')
        sudo('systemctl restart gunicorn')
