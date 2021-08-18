from django.http import JsonResponse
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {key: serializer.data[key] for key in serializer.data.keys() if key != 'password'}
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
