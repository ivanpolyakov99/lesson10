from django.utils import timezone

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.serializers import TestSerializer, TestDetailsSerializer, \
    TestResultSerializer
from testing.models import Test, TestResult


class TestListCreateAPI(generics.ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return TestDetailsSerializer


class TestDetailsAPI(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = TestDetailsSerializer

    def get_object(self):
        return get_object_or_404(Test, id=self.kwargs['id'])


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=['POST'], detail=True)
    def start_test(self, request, pk=None):
        test = self.get_object()
        result = TestResult.objects.filter(
            test=test,
            user=request.user,
            end_at__isnull=True
        ).first()
        status = 200
        if not result:
            result = TestResult.objects.create(
                test=test,
                user=request.user,
                start_at=timezone.now()
            )
            status = 201
        return JsonResponse(TestResultSerializer(result).data, status=status)

    @action(methods=['POST'], detail=True)
    def end_test(self, request, pk=None):
        test = self.get_object()
        result = get_object_or_404(
            TestResult,
            test=test,
            user=request.user,
            end_at__isnull=True
        )
        result.end_at = timezone.now()
        result.save()
        return JsonResponse(TestResultSerializer(result).data, status=200)

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return TestDetailsSerializer
        return self.serializer_class

    def get_object(self):
        return get_object_or_404(Test, id=self.kwargs['pk'])

