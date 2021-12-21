from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter

from new_app.models import Question
from new_app.serializers import QuestionDetailSerializer


class QuestionsView(ListCreateAPIView):
    """
    This class is used to list and create question and choice detail
    """
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['question_text', 'choices__choice_text']
    