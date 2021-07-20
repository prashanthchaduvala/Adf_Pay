from .models import *
from .serializers import *
from rest_framework.permissions import (AllowAny)
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import os
from django.http import Http404
# import request
from django.conf import settings
from rest_framework import status, generics, mixins
import re
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView



class ManageNewsMediaAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = ManageNewsMedia.objects.all()
    serializer_class = ManageNewsMediaSerializer
    def get_object(self, id):
        try:
            return ManageNewsMedia.objects.get(action_on_id=id)
        except ManageNewsMediaSerializer.DoesNotExist:
            raise Http404

    def get(self, request,id=None, *args, **kwargs):
        if id:
            id_obj = self.get_object(id)
            serializer = ManageNewsMediaSerializer(id_obj)
            return Response(serializer.data)
        else:
            alldata = ManageNewsMedia.objects.all()
            serializer = ManageNewsMediaSerializer(alldata, many=True)
            return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ManageNewsMediaSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,id=None, *args, **kwargs):
        agent_type = self.get_object(id)
        serializer = ManageNewsMediaSerializer(agent_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # body_data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None, *args, **kwargs):
        try:
            ManageNewsMedia.objects.filter(action_on_id=id).delete()
            message = {"success": "sucessfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)