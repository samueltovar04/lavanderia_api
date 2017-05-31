from rest_framework import views, serializers, generics, filters, permissions, status, mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from perfiles.serializers import *
from .models import *
from perfiles.serializers import *
from ordenes.serializers import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apirest import *
import datetime
import json
from django.shortcuts import HttpResponse

class PermissionMixin(object):
    permission_classes = (permissions.IsAuthenticated,)

class GenericMixin(PermissionMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        self.object = self.get_object_or_none()
        serializer = self.get_serializer(self.object, data=request.DATA,files=request.FILES, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            self.pre_save(serializer.object)
        except ValidationError as err:
            return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)
        if self.object is None:
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        self.object = serializer.save(force_update=True)
        self.post_save(self.object, created=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        fields = tuple([str(x.name) for x in self.queryset.model._meta.fields])
        for key,value in self.request.query_params.dict().items():
            key_split = key.split('__')[0]
            if key_split in fields:
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                filter.update({key:value})
        try:
            filtered_object = queryset.filter(**filter)
        except eval("%s.DoesNotExist"%(self.__class__.__name__[:-3],)):
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        except:
            filtered_object = queryset
        serializer = eval("%sSerializer(filtered_object, many=True)"%(self.__class__.__name__[:-3],))
        return Response(serializer.data)

    def retrieve(self, request, pk):
        print  self.queryset.model
        try:
            queryset = self.get_queryset().get(pk=pk)
        except eval("%s.DoesNotExist"%(self.__class__.__name__[:-3],)):
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        serializer = eval("%sSerializer(queryset)"%(self.__class__.__name__[:-3],))
        return Response(serializer.data)
