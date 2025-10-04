from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    
    department_name=models.CharField(null=True, max_length=100)
    def __str__(self):
        return self.department_name
    

   
       
       
class EmployeeModel(models.Model):
    
    DESIGNATION_TYPE={
        
        ('manager','manager'),
        ('ceo','ceo'),
        ('admin','admin'),
        ('staff','staff'),
    }
    
    
    employee_name=models.CharField(null=True, max_length=500)
    employee_idno=models.IntegerField(null=True)
    department=models.ForeignKey( DepartmentModel, on_delete=models.SET_NULL,null=True,related_name="employee_department")
    designation=models.CharField( choices=DESIGNATION_TYPE,null=True, max_length=50)
    salary=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.employee_name
    
 
class BasicInfoModel(models.Model):
     
    employee=models.OneToOneField( EmployeeModel, on_delete=models.CASCADE,related_name="employee_info")
    gender=models.CharField(null=True, max_length=50)
    email=models.EmailField(null=True, max_length=254)
    contact=models.CharField(null=True, max_length=15)
    address=models.TextField(null=True)
    def __str__(self):
        return self.employee.employee_name
     
     
 
   
 
 