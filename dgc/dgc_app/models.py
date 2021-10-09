from django.db import models

# Create your models here.
class master_user(models.Model):
    emp_id = models.PositiveIntegerField(primary_key=True, unique=True)
    emp_name = models.CharField(max_length=100)
    emp_emailid = models.EmailField()
    password = models.CharField(max_length=100)


class app_details(models.Model):
    apartment_id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    apartment_name = models.CharField(max_length=100)
    apartment_code = models.IntegerField(unique=True)
    apartment_mail = models.EmailField()
    apartment_phn = models.BigIntegerField()
    apartment_descriptions = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=250)
    no_of_block = models.PositiveIntegerField()
    no_of_flats = models.PositiveIntegerField()
    no_of_elevator = models.PositiveIntegerField()
    no_of_incharge = models.PositiveIntegerField()


class admin_details(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    role = models.CharField(max_length=100)
    mobile_no = models.PositiveBigIntegerField()
    address = models.CharField(max_length=250)
    alt_mobile_no = models.PositiveBigIntegerField()
    aadhar_no = models.PositiveBigIntegerField()
    aadhar_image = models.ImageField()
    email_id = models.EmailField()
    status = models.Choices(['verified', 'unverified'])
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

"""
class permission_for_admin(models.Model):
    last10days = 10
    last30days = 30
    last60days = 60
    last90days = 90
    last180days = 180
    last240days = 240
    last365days = 365
    days_selects = [
        (last10days, 'Last 10 days'),
        (last30days, 'Last 30 days'),
        (last60days, 'Last 60 days'),
        (last90days, 'Last 90 days'),
        (last180days, 'Last 180 days'),
        (last240days, 'Last 240 days'),
        (last365days, 'Last 365 days'),
    ]
    show_visitors = models.CharField(max_length=50, choices=[True, False], default=False)
    visitors_selected_block = models.CharField(max_length=100, default="block-1")
    visitors_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    show_event= models.CharField(max_length=50, choices=[True, False], default=False)
    event_selected_block = models.CharField(max_length=100, default="block-1")
    event_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    elevator = models.CharField(max_length=50, choices=[True, False], default=False)
    cctv = models.CharField(max_length=50, choices=[True, False], default=False)
    cctv_selected_block = models.CharField(max_length=100, default="block-1")
    cctv_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    cctv_live_or_not = models.CharField(max_length=50, choices=[True, False], default=True)
"""
