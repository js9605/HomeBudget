from django.db import models
from django.contrib.auth.models import User

class Earning(models.Model):
    CATEGORY_CHOICES = [
        ('SALARY', 'Salary'),
        ('FREELANCE', 'Freelance'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category}: {self.amount} on {self.date}"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('BILLS', 'Bills'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category}: {self.amount} on {self.date}"

class BankAccount(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def update_balance(self, earnings, expenses):
        self.balance += sum([e.amount for e in earnings]) - sum([e.amount for e in expenses])
        self.save()

    def __str__(self):
        return f"Current Balance: {self.balance}"
