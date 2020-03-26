# Миксины
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, reguest, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(reguest, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, reguest):
        form = self.model_form()
        return render(reguest, self.template, context={"form": form})

    def post(self, reguest):
        bound_form = self.model_form(reguest.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(reguest, self.template, context={"form": bound_form})



