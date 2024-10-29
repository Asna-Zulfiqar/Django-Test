from django.contrib import admin
from .models import Account , Lender , Borrower , Loan , LoanReturned


admin.site.register(Account)
admin.site.register(Lender)
admin.site.register(Borrower)
admin.site.register(Loan)
admin.site.register(LoanReturned)