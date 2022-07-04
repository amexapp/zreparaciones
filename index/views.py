from django import forms
from django.db.models.fields import files
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


def Home(request):
        return render(request, 'pages/index.html')