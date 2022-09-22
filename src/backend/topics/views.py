from rest_framework import (viewsets, permissions,
                            pagination, status)
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .models import TopicTag, Topic


class Paginator(pagination.PageNumberPagination):
    page_size = 30


class TopicTagViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = TopicTag.objects.all()
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'slug')

    def get_serializer_class(self):
        if self.action.lower() in ('create', 'partial_update', 'update', 'delete'):
            return serializers.TopicTagCreateSerializer
        else:
            return serializers.TopicTagSerializer


class TopicViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Topic.objects.all().order_by('?')
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'slug', 'tags')
    pagination_class = Paginator


    def get_serializer_class(self):
        if self.action.lower() in ('create', 'partial_update', 'update', 'delete'):
            return serializers.TopicCreateSerializer
        else:
            return serializers.TopicSerializer

    @action(detail=True, methods=['post'], url_path='join')
    def join_topic(self, request, pk):
        topic = self.get_object()

        if not topic.members.contains(request.user):
            topic.members.add(request.user)

        else:
            topic.members.remove(request.user)

        return Response(status=status.HTTP_200_OK)
