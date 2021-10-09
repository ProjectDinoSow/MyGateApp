from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from models import *

# Create your views here.
class master_login(viewsets.ViewSet):
    def master_create(self):
        pass

    def master_update(self):
        pass

    def master_del(self):
        pass

class apartment_create(viewsets.ViewSet):
    def app_create(self):
        pass

    def app_views(self):
        pass

    def app_update(self):
        pass

    def app_del(self):
        pass

class admin_register(viewsets.ViewSet):
    def admin_create(self):
        pass

    def admin_views(self):
        pass

    def admin_update(self):
        pass

    def admin_del(self):
        pass

