from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from apps.modules.delivery.models import Mailing
from core.widgets import AddressWidget, PersonWidget, PhoneWidget


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['barcode', 'person', 'address', 'phone']
        widgets = {
            'barcode': forms.TextInput(attrs={'autofocus': True}),
            'person': PersonWidget,
            'address': AddressWidget,
            'phone':  PhoneWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('barcode', css_class='form-group col-md-4 mb-0'),
                Column('person', css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('address', css_class='form-group col-md-8 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
            ),
            Submit('submit', 'Сохранить')
        )
