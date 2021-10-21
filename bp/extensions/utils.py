from django.contrib.contenttypes.models import ContentType


def limit_content_type(app, model):
    try:
        content_type = ContentType.objects.get_by_natural_key(app, model).pk
    except:
        content_type = 0
    return {'content_type': content_type}
