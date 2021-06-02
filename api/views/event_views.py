from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.event import Event
from ..serializers import EventSerializer

class Events(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = EventSerializer

    def get(self, request):
        events = Event.objects.filter(owner=request.user.id)
        data = EventSerializer(events, many=True).data
        return Response({ 'events': data })

    def post(self, request):
        request.data['event']['owner'] = request.user.id
        event = EventSerializer(data=request.data['event'])

        if event.is_valid():
            event.save()
            return Response({ 'event': event.data }, status=status.HTTP_201_CREATED)

        return Response(event.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)

        if not request.user.id == event.owner.id:
            raise PermissionDenied("Unauthorized, you don't own this event")

        data = EventSerializer(event).data
        return Response({ 'event': data })

    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)

        if not request.user.id == event.owner.id:
            raise PermissionDenied("Unauthorized, you don't own this event")

        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        event = get_object_or_404(Event, pk=pk)

        if not request.user.id == event.owner.id:
            raise PermissionDenied("Unauthorized, you don't own this event")

        request.data['event']['owner'] = request.user.id

        data = EventSerializer(event, data=request.data['event'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
