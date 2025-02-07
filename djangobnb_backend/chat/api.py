from django.http import JsonResponse

from rest_framework.decorators import api_view

from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer

from useraccount.models import User


@api_view(['GET'])
def conversations_list(request):
    conversations = Conversation.objects.prefetch_related('users').filter(users=request.user)
    serializer = ConversationListSerializer(conversations, many=True)

    print("API Response:", serializer.data)  # Debugging
    return JsonResponse(serializer.data, safe=False)
