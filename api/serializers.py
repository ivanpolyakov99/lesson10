from rest_framework import serializers

from testing.models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id', 'name'
        )


class TestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'level')
