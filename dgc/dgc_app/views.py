from rest_framework import viewsets, request, status
from rest_framework.response import Response
from models import *
from serializers import *

# Create your views here.
class master_login(viewsets.ViewSet):
    def master_create(self):
        serializer = master_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def login(self, request):
        if request.method == "POST":
            try:
                masterdetails = master_user.objects.get(emp_name=request.POST['emp_name'], Password=request.POST[
                    'password'])
                #request.session['username'] = master_user.emp_name
                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    def master_update(self, request, pk=None):
        master_edit = master_user.objects.get(emp_id=pk)
        serializer = master_serializer(instance=master_edit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    def master_del(self, request, pk=None):
        master_delete = master_user.objects.get(emp_id=pk)
        master_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class apartment_create(viewsets.ViewSet):
    def app_create(self, request):
        serializer = apartment_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def app_views(self, request):
        apartments = app_details.objects.all()
        serializer = apartment_serializer(apartments, many=True)
        return Response(serializer.data)

    def app_update(self, request, pk=None):
        apartment_edit = app_details.objects.get(apartment_id=pk)
        serializer = apartment_serializer(instance=apartment_edit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    def app_del(self, request, pk=None):
        apartment_delete = app_details.objects.get(apartment_id=pk)
        apartment_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class admin_register(viewsets.ViewSet):
    def admin_create(self, request):
        serializer = admin_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def admin_views(self, request):
        admins = admin_details.objects.all()
        serializer = admin_serializer(admins, many=True)
        return Response(serializer.data)

    def admin_update(self, request, pk=None):
        admin_edit = admin_details.objects.get(admin_name=pk)
        serializer = admin_serializer(instance=admin_edit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    def admin_del(self, request, pk=None):
        admin_delete = admin_details.objects.get(admin_name=pk)
        admin_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
