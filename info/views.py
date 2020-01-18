from django.http import HttpResponse


from info.models import Txn
from rest_framework import viewsets
from info.serializers import TxnSerializer

class TxnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Txn.objects.all().order_by('-created_at')
    serializer_class = TxnSerializer


