from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from destination.models import Destination
from .serializers import IncomingDataSerializer, DestinationSerializer
from .tasks import send_data_to_destinations

class IncomingDataView(APIView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = IncomingDataSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            token = request.headers.get('CL-X-TOKEN')
            try:
                account = CustomUser.objects.get(token=token)
            except CustomUser.DoesNotExist:
                return Response({"message": "Invalid App Secret Token"}, status=status.HTTP_400_BAD_REQUEST)

            destinations = account.destinations.all()
            serialized_destinations = DestinationSerializer(destinations, many=True).data
            send_data_to_destinations.delay(data, serialized_destinations)
            return Response({"message": "Data received and sent to destinations"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)