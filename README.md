Ex02 Django ORM Web Application
## Date: 14/11/2024 

## AIM
To develop a Django application to store and retrieve data from a Bank database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![New Project 19  2E923AA](https://github.com/user-attachments/assets/f639e8c6-d27b-4c5a-b84c-2e055f7c4e0b)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 customers.

## PROGRAM
```
from django.contrib import admin
from .models import BankLoan,BankAdmin
admin.site.register(BankLoan,BankAdmin)

from django.db import models
from django.contrib import admin
class BankLoan (models.Model):
    Loan_id=models.IntegerField()
    Loan_type=models.CharField(max_length=30)
    Loan_amt=models.CharField(max_length=40)
    Customer_acno=models.IntegerField(primary_key=True)
    Cust_name=models.CharField(max_length=50)

class BankAdmin(admin.ModelAdmin):
    list_display=('Loan_id','Loan_type','Loan_amt','Customer_acno','Cust_name')
```


## OUTPUT
![Screenshot 2024-11-15 081958](https://github.com/user-attachments/assets/aff5247e-b4d3-47bb-a4cc-079434559ef8)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
