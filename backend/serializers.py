from swampdragon.serializers.model_serializer import ModelSerializer

class LogSerializer(ModelSerializer):
    class Meta:
        model = 'backend.Log'
        publish_fields = ('message')
        base_channel = 'log'

    @classmethod
    def get_base_channel(cls):
        super(LogSerializer, cls).get_base_channel()
