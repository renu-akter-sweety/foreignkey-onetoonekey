from django.contrib import admin
from django.urls import path
from myapp.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', basepage, name="baseurl"),            
    path('departmentpage/', Departmentpage, name="departmentpageurl"),
    path('employee/', employeepage, name="employeeurl"),            
    path('basicinfo/', basicinfopage, name="basicinfourl"),  # ✅ Fixed
]
