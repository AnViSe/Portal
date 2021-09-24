class RefTableMixin(object):
    # url_list = ''
    # field_list = []
    template_name = 'references/ref_list.html'
    action_field = {"name": '_', "title": "Операции"}

    # def get_url(self, model=None):
    #     if model:
    #         return f'{str(model.__name__).lower()}-list'
    #     else:
    #         return self.url_list

    # def get_columns(self, model=None):
    #     if model:
    #         model_fields = model._meta.get_fields(include_parents=False, include_hidden=False)
    #         fields = []
    #         for field in model_fields:
    #             fields.append({"name": field.name, "title": field.verbose_name})
    #         return fields
    #     else:
    #         # self.field_list.append({"name": None, "title": "Actions"})
    #         return self.field_list

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['route_list_api'] = self.model.Params.route_list_api
    #     context['fields_list'] = self.model.Params.fields_list
    #     return context
