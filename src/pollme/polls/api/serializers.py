
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from ..models import Question, Choice

class QuestionListSerializer(ModelSerializer):
    """
    This serializer serializes the Question model
    It includes a field "choices" that will serialize all the
        choices for a question
    """
    choices = SerializerMethodField()

    def get_choices(self, obj):
        choices = obj.choice_set.all()
        return ChoiceSerializer(choices, many=True).data

    def create(self, validated_data):
        """
        Creates and return a new `question` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)

    class Meta:
        model = Question
        fields = ["id", "text", "pub_date", "choices"]

class ChoiceSerializer(ModelSerializer):
    """
    This serializes the Choice model
    """

    def create(self, validated_data):
        """
        Creates and returns a new `choice` instance, given the validated data.
        """
        return Choice.objects.create(**validated_data)

    class Meta:
        model = Choice
        fields = ["choice_text", "votes"]
