from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser , Customer , GroupCustomer
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                 "email", "first_name", "last_name","password1" , "password2" ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("اطلاعات شخصی", {"fields": (
        "first_name", "last_name", "phone", 'job_title', 'gender')}),
        ("مجوزها", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("تاریخ‌های مهم", {"fields": ("last_login", "date_joined")}),
       
    )
    list_display = ('email' , 'first_name' , 'last_name' , )
    list_filter = ('email',)
    search_fields = ("email",)
    ordering = ('email',)


admin.site.register(Customer)
admin.site.register(GroupCustomer)