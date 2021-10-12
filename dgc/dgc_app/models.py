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
    last10days = 10
    last20days = 20
    last30days = 30
    last60days = 60
    last90days = 90
    last180days = 180
    last240days = 240
    last365days = 365
    days_selects = [
        (last10days, 'Last 10 days'),
        (last20days, 'Last 20 days'),
        (last30days, 'Last 30 days'),
        (last60days, 'Last 60 days'),
        (last90days, 'Last 90 days'),
        (last180days, 'Last 180 days'),
        (last240days, 'Last 240 days'),
        (last365days, 'Last 365 days'),
    ]
    photo = models.ImageField(blank=True)
    admin_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(blank=True)
    role = models.CharField(max_length=100, blank=True)
    mobile_no = models.PositiveBigIntegerField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    alt_mobile_no = models.PositiveBigIntegerField(blank=True)
    aadhar_no = models.PositiveBigIntegerField(blank=True)
    aadhar_image = models.ImageField(blank=True)
    email_id = models.EmailField(blank=True)
    status = models.CharField(max_length=50, choices=['verified', 'unverified'], default='unverified')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    show_visitors = models.CharField(max_length=50, choices=['yes', 'No'], default='No')
    visitors_selected_block = models.CharField(max_length=100, default="block-1")
    visitors_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    show_tickets = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    tickets_selected_block = models.CharField(max_length=100, default="block-1")
    tickets_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    show_event= models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    event_selected_block = models.CharField(max_length=100, default="block-1")
    event_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    show_amenties = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    show_elevator = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    show_maintenances = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    maintenances_selected_block = models.CharField(max_length=100, default="block-1")
    maintenances_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    show_attendance = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    attendance_selected_block = models.CharField(max_length=100, default="block-1")
    attendance_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    cctv = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    cctv_selected_days = models.CharField(max_length=100, choices=days_selects, default=last10days)
    cctv_live_or_not = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    show_housevacant = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    housevacant_selected_block = models.CharField(max_length=100, default="block-1")
    show_guesthousevacant = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    guesthousevacant_selected_block = models.CharField(max_length=100, default="block-1")
    show_alert_and_sos = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    alert_and_sos_selected_block = models.CharField(max_length=100, default="block-1")
    show_medical_struck = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    medical_struck_selected_block = models.CharField(max_length=100, default="block-1")
    show_residence_details = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    residence_selected_block = models.CharField(max_length=100, default="block-1")
    show_inventory = models.CharField(max_length=50, choices=['Yes', 'No'], default='No')
    inventory_selected_block = models.CharField(max_length=100, default="block-1")



