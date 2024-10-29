from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    amount = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=True)
    

class Lender(models.Model):
    lender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='lender')
    phone_no = models.IntegerField(max_length=13)
    address = models.TextField()
    account = models.ForeignKey(Account , on_delete=models.CASCADE , related_name='account_owned')


class Borrower(models.Model):
    borrower= models.ForeignKey(User , on_delete=models.CASCADE , related_name='borrower')
    contact_info = models.IntegerField(max_length=13)
    address = models.TextField()

 
class Loan(models.Model):
    status_choices = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=status_choices)


class LoanReturned(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    return_date = models.DateField()

    
    


