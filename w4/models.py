from django.db import models

# Shop's model


class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.JSONField(encoder=None, decoder=None, null=True)

class Cart(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.PROTECT, null=False)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    expired_in = models.IntegerField(default=60, null=False)

class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    categories = models.ManyToManyField("shop.ProductCategory")

    #1.2
    # def __str__(self):
    #     return "PRODUCT ID: "+str(self.id)+", DESCRIPTION: "+self.description+"\n"

    #1.3, 1.4 
    def __str__(self):
        return "PRODUCT ID: "+str(self.id)+", NAME: "+self.name+", PRICE: "+str(self.price)+"\n"



class CartItem(models.Model):
    cart = models.ForeignKey("shop.Cart", on_delete=models.PROTECT, null=False)
    product = models.ForeignKey("shop.Product", on_delete=models.PROTECT, null=False)
    amount = models.IntegerField(default=1, null=False)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=False)

class Order(models.Model):
    customer= models.ForeignKey("shop.Customer", on_delete=models.PROTECT, null=False)
    order_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    remark = models.TextField(null=True)

    def __str__(self):
        return "ORDER ID:"+str(self.id)+", DATE: "+str(self.order_date)+", PRICE: "+str(self.payment.price)+"\n"
    #from shop.models import *
    #Order.objects.filter(order_date__month=5)

class OrderItem(models.Model):
    order= models.ForeignKey("shop.Order", on_delete=models.PROTECT, null=False)
    product= models.ForeignKey("shop.Product", on_delete=models.PROTECT, null=False)
    amount = models.IntegerField(default=1, null=False)

class Payment(models.Model):
    order= models.OneToOneField("shop.Order", on_delete=models.PROTECT, null=False)
    payment_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class PaymentItem(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.PROTECT, null=False)
    order_item = models.OneToOneField("shop.OrderItem", on_delete=models.PROTECT, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class PaymentMethod(models.Model):

    qr = 'QR'
    credit = 'CR'

    CHOICES = {
        qr: 'QR',
        credit: 'CREDIT'
    }

    payment = models.ForeignKey("shop.Payment", on_delete=models.PROTECT, null=False)
    method = models.CharField(choices= CHOICES, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
