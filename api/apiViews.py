from api.serializers import storySerializer
from rest_framework import viewsets
from rainbow.models import story


class storyViewSet(viewsets.ModelViewSet):
    queryset = story.objects.all().order_by('-createdTime')
    serializer_class = storySerializer
