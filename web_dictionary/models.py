import uuid
from django.core.exceptions import ValidationError
from django.db import models
from .utils import get_properties, validate_properties


class ObjectType(models.Model):
    name = models.CharField(
        primary_key=True, max_length=79, editable=False, unique=True
    )


class ObjectNode(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    object_type = models.ForeignKey(ObjectType, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    properties = models.JSONField()

    def get_properties(self):
        return get_properties(self.properties, self.object_type.schema)


class EdgeType(models.Model):
    name = models.CharField(
        primary_key=True, max_length=79, editable=False, unique=True
    )
    directed = models.BooleanField(default=True)


class Edge(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    edge_type = models.ForeignKey(EdgeType, on_delete=models.PROTECT)
    source_node = models.ForeignKey(
        ObjectNode, on_delete=models.CASCADE, related_name="out_rels"
    )
    target_node = models.ForeignKey(
        ObjectNode, on_delete=models.CASCADE, related_name="in_rels"
    )
    properties = models.JSONField()
