from django.contrib import admin
from app1.models import Employee

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    # To display the Employee data in tabular format in the admin panel
    list_display = [
        'e_name',
        'e_age',
        'e_sal',
        'e_add',
    ]


admin.site.register(Employee, EmpAdmin)
