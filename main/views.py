#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from main.forms import RegisterForm


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main/index.html', context)


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main/profile.html', context)


def regist(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'main/regist.html', context)


@require_POST
def regist_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('main/index')

    context = {
        'form': form,
    }
    return render(request, 'main/regist.html', context)
