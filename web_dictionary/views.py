from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic import ListView
from .models import ObjectNode


class EntryView(ListView):
    context_object_name = "entries"
    http_method_names = ["get"]
    model = ObjectNode
    template_name = "entry/entry.html"

    def get_queryset(self):
        name = self.kwargs.get("name")
        return ObjectNode.objects.filter(web_slug=name)


@require_GET
def search(request):
    if "query" not in request.GET or not request.GET.get("query").strip():
        return HttpResponseBadRequest(
            "The 'query' search parameter is missing."
        )

    query = request.GET.get("query", "").strip().casefold()
    results = ObjectNode.objects.filter(name__contains=query)

    context = {
        "results": results,
        "query": query,
    }

    return render(request, "entry/search.html", context)
