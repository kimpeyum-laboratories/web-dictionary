import uuid
from django.db import models
from django.utils.text import slugify


class ObjectType(models.Model):
    name = models.CharField(primary_key=True, max_length=79)


class ObjectNode(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    object_type = models.ForeignKey(ObjectType, on_delete=models.PROTECT)
    name = models.CharField(db_index=True, max_length=255)
    properties = models.JSONField(blank=True, default=dict)

    # For web-only
    web_slug = models.SlugField(
        allow_unicode=True, blank=True, max_length=255, null=False
    )

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.casefold()

        if not self.web_slug:
            self.web_slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class EdgeType(models.Model):
    name = models.CharField(
        primary_key=True, max_length=79, editable=False, unique=True
    )
    directed = models.BooleanField(default=True)


class Edge(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    edge_type = models.ForeignKey(EdgeType, on_delete=models.PROTECT)
    source_node = models.ForeignKey(
        ObjectNode, on_delete=models.CASCADE, related_name="out_rels"
    )
    target_node = models.ForeignKey(
        ObjectNode, on_delete=models.CASCADE, related_name="in_rels"
    )
    properties = models.JSONField(blank=True, default=dict)
