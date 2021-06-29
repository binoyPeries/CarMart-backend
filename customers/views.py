from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        customer = request.data
        serializer = self.serializer_class(data=customer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
