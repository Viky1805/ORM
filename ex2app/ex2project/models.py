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
