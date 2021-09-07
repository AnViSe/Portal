from django.db.backends.oracle import base
# https://github.com/manelclos/django-oracle-backend


class DatabaseWrapper(base.DatabaseWrapper):
    data_types = base.DatabaseWrapper.data_types.copy()
    data_types.update({
        'CharField': 'VARCHAR2(%(max_length)s CHAR)',
        'CommaSeparatedIntegerField': 'VARCHAR2(%(max_length)s CHAR)',
        'FileField': 'VARCHAR2(%(max_length)s CHAR)',
        'FilePathField': 'VARCHAR2(%(max_length)s CHAR)',
        'IPAddressField': 'VARCHAR2(15 CHAR)',
        'GenericIPAddressField': 'VARCHAR2(39 CHAR)',
        'SlugField': 'VARCHAR2(%(max_length)s CHAR)',
        'TextField': 'CLOB',
        'URLField': 'VARCHAR2(%(max_length)s CHAR)',
        'UUIDField': 'VARCHAR2(32 CHAR)',
    })
