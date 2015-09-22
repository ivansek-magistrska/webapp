from swampdragon import route_handler
from backend.models import Log, Configuration
from swampdragon.route_handler import ModelPubRouter, ModelRouter
from backend.serializers import LogSerializer

class LogRouter(ModelRouter):
    serializer_class = LogSerializer
    model = Log
    route_name = 'log-route'

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        self.configuration_id = kwargs['id']
        objects = self.model.objects.filter(configuration__id=kwargs['id'])
        return objects

route_handler.register(LogRouter)
