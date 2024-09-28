from rest_framework.serializers import ModelSerializer
from .models import Processor, VideoCard


class ProcessorSerializer(ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'


class VideoCardSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        fields = '__all__'
