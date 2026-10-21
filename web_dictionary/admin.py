from django.contrib import admin
from .models import ObjectType, ObjectNode, EdgeType, Edge

admin.site.register(ObjectType)
admin.site.register(EdgeType)


@admin.register(ObjectNode)
class ObjectNodeAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "object_type")

    search_fields = ("name",)

    list_filter = ("object_type",)


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ("uuid", "edge_type", "source_node", "target_node")

    list_filter = ("edge_type",)
