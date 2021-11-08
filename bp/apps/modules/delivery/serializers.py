from rest_framework import serializers

from apps.modules.delivery.models import Mailing


class MailingSerializer(serializers.ModelSerializer):
    """Список почтовых отправлений"""

    person = serializers.StringRelatedField(source='person.name_lfm',
                                            default=None,
                                            label='Получатель')
    address = serializers.StringRelatedField(source='address.name_adds_full',
                                             default=None,
                                             label='Адрес доставки')
    phone = serializers.StringRelatedField(source='phone.phone_number',
                                           default=None,
                                           label='Номер телефона')

    class Meta:
        model = Mailing
        fields = ['id', 'barcode', 'person', 'address', 'phone', 'notice_number']
        read_only_fields = fields
