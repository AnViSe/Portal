# -*- coding: UTF-8 -*-
# pip install fabric3
# https://adw0rd.com/2012/8/14/python-fabric/
# https://github.com/fabtools/fabtools
# https://jenyay.net/Programming/Fabric

from fabric.api import run, env, task, prefix


# env.roledefs['production'] = ['adm_www@172.16.190.221:22']


def production_env():
    env.user = 'adm_www'
    env.password = 'www_adm'
    # env.shell = 'sh -c'
    env.host_string = '172.16.190.221'
    # Путь до каталога проекта (на сервере)
    env.project_root = '/home/adm_www/sites/portal/bp'
    # Путь до python (на сервере)
    env.python = '/home/adm_www/sites/venv/bin/python'
    # Активация виртуального окружения
    env.venv_activate = 'source /home/adm_www/sites/venv/bin/activate'


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
