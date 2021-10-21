from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from rest_framework import viewsets, request, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import master_user, app_details, admin_details
from .serializers import master_serializer, admin_serializer, apartment_serializer
import json
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class master_login(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_protect
    def master_create(self):
        try:
            data = {}
            serializer = master_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                token = Token.objects.get_or_create(master_user=serializer)[0].key
                data["message"] = "user registered successfully"
                data["emp_emailid"] = serializer.emp_emailid
                data["emp_name"] = serializer.emp_name
                data["token"] = token
                return Response(status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
        except IntegrityError as e:
            account = master_user.objects.get(username='')
            account.delete()
            raise ValidationError({"400": f'{str(e)}'})

        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})


    def master_views(self, request):
        master = master_user.objects.all()
        serializer = master_serializer(master, many=True)
        token = Token.objects.get_or_create(master_user=serializer)[0].key
        return Response(serializer, status=status.HTTP_200_OK)

    @api_view(["POST"])
    @csrf_protect
    def login_masteruser(request):
        data = {}
        reqBody = json.loads(request.body)
        email1 = reqBody['emp_emailid']
        print(email1)
        password = reqBody['password']
        try:
            Account = master_user.objects.get(emp_emailid=email1)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})
        token = Token.objects.get_or_create(master_user=Account)[0].key
        print(token)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})
        if Account:
            if Account.is_active:
                print(request.master_user)
                login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.email
                Res = {"data": data, "token": token}
                return Response(Res)
            else:
                raise ValidationError({"400": f'Account not active'})
        else:
            raise ValidationError({"400": f'Account doesnt exist'})

    @api_view(["GET"])
    def logout_masteruser(request):
        request.user.auth_token.delete()
        logout(request)
        return Response('User Logged out successfully')

    @csrf_protect
    def master_update(self, request, pk=None):
        master_edit = master_user.objects.get(emp_id=pk)
        serializer = master_serializer(instance=master_edit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @csrf_protect
    def master_del(self, request, pk=None):
        master_delete = master_user.objects.get(emp_id=pk)
        master_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class apartment_create(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_protect
    def app_create(self, request):
        serializer = apartment_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def app_views(self, request):
        apartments = app_details.objects.all()
        serializer = apartment_serializer(apartments, many=True)
        return Response(serializer.data)

    def specify_app_views(self, request, pk=None):
        apartments = app_details.objects.get(apartment_id=pk)
        serializer = apartment_serializer(apartments)
        return Response(serializer.data)

    @csrf_protect
    def app_update(self, request, pk=None):
        apartment_edit = app_details.objects.get(apartment_id=pk)
        serializer = apartment_serializer(instance=apartment_edit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @csrf_protect
    def app_del(self, request, pk=None):
        apartment_delete = app_details.objects.get(apartment_id=pk)
        apartment_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class admin_register(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_protect
    def admin_create(self, request):
        serializer = admin_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def admin_views(self, request):
        admins = admin_details.objects.all()
        serializer = admin_serializer(admins, many=True)
        return Response(serializer.data)

    def specify_admin_views(self, request, pk=None):
        admins = admin_details.objects.get(admin_name=pk)
        serializer = apartment_serializer(admins)
        return Response(serializer.data)

    @csrf_protect
    def admin_update(self, request, pk=None):
        admin_edit = admin_details.objects.get(admin_name=pk)
        serializer = admin_serializer(instance=admin_edit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @csrf_protect
    def admin_del(self, request, pk=None):
        admin_delete = admin_details.objects.get(admin_name=pk)
        admin_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
# master login reference
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
'''

