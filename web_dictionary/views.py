from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import DetailView, ListView
from .models import ObjectNode

# Create your views here.


class EntryView(ListView):
    model = ObjectNode
    template_name = "entry/entry.html"
    context_object_name = "entries"

    def get_queryset(self):
        name = self.kwargs.get("name")
        return ObjectNode.objects.filter(name=name)


def search(request):
    if "query" not in request.GET or not request.GET.get("query").strip():
        return HttpResponseBadRequest(
            "The 'query' search parameter is missing."
        )

    query = request.GET.get("query", "")
    entries = ObjectNode.objects.filter(name__icontains=query)

    context = {
        "entries": entries,
        "query": query,
    }

    return render(request, "search_result.html", context)
