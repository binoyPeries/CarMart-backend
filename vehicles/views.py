from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Vehicle
from .serializers import VehicleSerializer


# @parser_classes((FormParser,))
class VehicleListView(ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)

    def get_queryset(self):
        return self.queryset.all()
