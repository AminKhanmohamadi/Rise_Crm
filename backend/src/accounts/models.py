from django.contrib.auth.models import AbstractUser , BaseUserManager , PermissionsMixin
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None , **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser ,PermissionsMixin):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    username = None

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=30 , null=True , blank=True)
    job_title = models.CharField(max_length=50 , null=True , blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    def __str__(self):
        return self.email


class GroupCustomer(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Customer(models.Model):
    CURRENCY_CHOICES = [
        ('IRR', 'Iranian Rial'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('USD', 'US Dollar'),
        ('JPY', 'Japanese Yen'),
        ('CAD', 'Canadian Dollar'),
        ('CHF', 'Swiss Franc'),
        ('AUD', 'Australian Dollar'),
        ('NZD', 'New Zealand Dollar'),
    ]

    TYPE_CHOICES = [
        ('Person', 'Person'),
        ('Organization', 'Organization'),
    ]

    owner = models.OneToOneField(CustomUser, on_delete=models.PROTECT, related_name='customer')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Person')
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    tax_number = models.CharField(max_length=50, blank=True, null=True)
    group = models.ManyToManyField(GroupCustomer, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='USD')
    is_payment_disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.owner.email})"