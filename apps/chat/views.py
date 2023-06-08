from rest_framework.response import Response
from rest_framework import viewsets, status, permissions

from .models import Message
from .serializers import MessageSerializer
from .gpt import gpt3_generate


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        question = serializer.validated_data['question']
        answer = gpt3_generate(question)
        self.save_messages(question, answer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def save_messages(self, question, answer):
        questions = Message.objects.create(question=question)
        answers = Message.objects.create(answer=answer)

        return questions, answers
