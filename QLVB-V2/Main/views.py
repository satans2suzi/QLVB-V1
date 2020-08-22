from django.shortcuts import render, HttpResponse
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        template_name = "Main/index.html"
        return render(request, template_name=template_name)
