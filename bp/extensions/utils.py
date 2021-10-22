from apps.references.models.base import FlexObject


def limit_content_type(app, model):
    try:
        to_pk = FlexObject.objects.get(object_app=app, object_model=model).pk
    except:
        to_pk = 0
    return {'type_object': to_pk}
