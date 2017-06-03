from rest_framework import serializers
from rainbow.models import story


class storySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = story
        fields = ('url', 'title', 'story', 'createdTime')
