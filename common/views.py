from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class Hello(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        hello = """<h1>Hello, world</h1>"""

        return HttpResponse(hello)

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')