from rest_framework import serializers
from .models import master_user, app_details, admin_details

class master_serializer(serializers.ModelSerializer):
    class Meta:
        model = app_details
        fields = "__all__"

class apartment_serializer(serializers.ModelSerializer):
    class Meta:
        model = app_details
        fields = "__all__"

class admin_serializer(serializers.ModelSerializer):
    class Meta:
        model = admin_details
        fields = "__all__"


