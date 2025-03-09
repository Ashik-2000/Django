from django.shortcuts import render
from django.http import HttpResponse
from .models import Aiquest
from .serializers import AiquestSerializers
from rest_framework.renderers import JSONRenderer

# Queryset
def aiquest_info(request):
    #complex data
    ai = Aiquest.objects.all()
    # convert to dict
    serializer = AiquestSerializers(ai, many=True)
    # convert the dict to JSON
    json_data = JSONRenderer().render(serializer.data)
    # show in frontend
    return HttpResponse(json_data, content_type='application/json')

# Instance
def aiquest_instance(request, pk):
    #complex data
    ai = Aiquest.objects.get(id=pk)
    # convert to dict
    serializer = AiquestSerializers(ai)
    # convert the dict to JSON
    json_data = JSONRenderer().render(serializer.data)
    # show in frontend
    return HttpResponse(json_data, content_type='application/json')