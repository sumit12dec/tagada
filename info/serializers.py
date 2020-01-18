from django.contrib.auth.models import User, Group
from info.models import Txn

from rest_framework import serializers


class TxnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Txn
        fields = ['id', 'amount']





