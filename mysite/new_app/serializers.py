from rest_framework import serializers
from new_app.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    """
    This class is used to create choice modelserializer instances
    """
    class Meta:
        model = Choice
        fields = '__all__'
    

class QuestionDetailSerializer(serializers.ModelSerializer):
    """
    This class is used to create question and choices modelserializer instances
    """
    choices = ChoiceSerializer(many = True)
    
    class Meta:
        model = Question
        fields =['id', 'question_text', 'pub_date', 'choices']

    def create(self, validated_data):
        choices = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        choice_dict = [Choice(**choice_dict,question=question) for choice_dict in choices]
        Choice.objects.bulk_create(choice_dict)
        return question
