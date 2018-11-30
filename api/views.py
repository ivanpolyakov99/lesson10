from rest_framework import generics
from rest_framework.generics import get_object_or_404

from api.serializers import TestSerializer, TestDetailsSerializer
from testing.models import Test


class TestListCreateAPI(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return TestDetailsSerializer


class TestDetailsAPI(generics.RetrieveAPIView):
    serializer_class = TestDetailsSerializer

    def get_object(self):
        return get_object_or_404(Test, id=self.kwargs['id'])
