from datetime import datetime
from random import randint

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)

class RandomNumber(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        num = randint

        return HttpResponse(num(0, 999))

