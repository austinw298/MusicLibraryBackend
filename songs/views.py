from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import MusicSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = MusicSerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#don't forget when you delete a song the ID doesnt move down, currently when getting
#song by ID, 
#the third song in the list, "Good Days", has ID of 4 not 3.

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
