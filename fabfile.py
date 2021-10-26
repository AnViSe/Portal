# -*- coding: UTF-8 -*-
# pip install fabric3
# https://adw0rd.com/2012/8/14/python-fabric/
# https://github.com/fabtools/fabtools
# https://jenyay.net/Programming/Fabric
import os
from pathlib import Path

from fabric.api import run, env, task, prefix, cd, sudo

from utils import load_env

get_env = os.environ.get

BASE_DIR = Path(__file__).resolve().parent

load_env(BASE_DIR / 'bp/config/.env')


def production_env():
    print(BASE_DIR)
    env.user = get_env('UNIX_USER')
    env.password = get_env('UNIX_PASS')
    # env.shell = 'sh -c'
    env.host_string = get_env('UNIX_HOST')
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


@task
def pip_install(package=None):
    """Установка пакета по имени"""
    if package:
        production_env()
        with prefix(env.venv_activate):
            run(f'pip3 install {package}')
    else:
        raise ValueError('Укажите имя пакета')


@task
def pip_update(package=None):
    """Обновление пакета по имени"""
    if package:
        production_env()
        with prefix(env.venv_activate):
            run(f'pip3 install -U {package}')
    else:
        raise ValueError('Укажите имя пакета')


@task
def pip_uninstall(package=None):
    """Удаление пакета по имени"""
    if package:
        production_env()
        with prefix(env.venv_activate):
            run(f'pip3 uninstall {package}')
    else:
        raise ValueError('Укажите имя пакета')


@task
def git_update(reload=True):
    """Обновление репозитория с перезагрузкой gunicorn"""
    production_env()
    with cd(env.portal_root):
        run('git pull')
        if reload:
            sudo('systemctl daemon-reload')
            sudo('systemctl restart gunicorn')
