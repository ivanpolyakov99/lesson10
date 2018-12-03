from rest_framework import serializers

from testing.models import Test, TestResult, Question, Answer


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id', 'name'
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'number', 'answers')


class TestDetailsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'level', 'questions')


class TestResultSerializer(serializers.ModelSerializer):
    delta = serializers.SerializerMethodField()

    class Meta:
        model = TestResult
        fields = ('start_at', 'end_at', 'test_id', 'delta')

    def get_delta(self, obj):
        if not obj.end_at:
            return
        delta = obj.end_at - obj.start_at
        return delta.seconds


class UserAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()

    # def validate_answer_id(self, answer_id):
    #     if not Answer.objects.filter(id=answer_id).exists():
    #         raise serializers.ValidationError('Answer not exists')
    #     return answer_id

    def validate(self, attrs):
        if not Answer.objects.filter(
            id=attrs['answer_id'],
            question_id=attrs['question_id']
        ).exists():
            raise serializers.ValidationError('Not exists')
        return attrs

