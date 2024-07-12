from django.db import models

# Shop's model

#one to one ยัง งงๆไม่รู้ว่าเเค่ postgres ไม่รองรับการเเสดงเเบบ one one ไหม

class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.JSONField(encoder=None, decoder=None, null=True)

class Cart(models.Model):
    customer_id = models.ForeignKey("shop.Customer", on_delete=models.PROTECT, null=False)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    expired_in = models.IntegerField(default=60, null=False)

class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    categories = models.ManyToManyField("shop.ProductCategory")

class CartItem(models.Model):
    cart_id = models.ForeignKey("shop.Cart", on_delete=models.PROTECT, null=False)
    product_id = models.ForeignKey("shop.Product", on_delete=models.PROTECT, null=False)
    amount = models.IntegerField(default=1, null=False)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=False)

class Order(models.Model):
    customer_id = models.ForeignKey("shop.Customer", on_delete=models.PROTECT, null=False)
    order_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    remark = models.TextField(null=True)

class OrderItem(models.Model):
    order_id = models.ForeignKey("shop.Order", on_delete=models.PROTECT, null=False)
    product_id = models.ForeignKey("shop.Product", on_delete=models.PROTECT, null=False)
    amount = models.IntegerField(default=1, null=False)

class Payment(models.Model):
    order_id = models.OneToOneField("shop.Order", on_delete=models.PROTECT, null=False)
    payment_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class PaymentItem(models.Model):
    payment_id = models.ForeignKey("shop.Payment", on_delete=models.PROTECT, null=False)
    order_item_id = models.OneToOneField("shop.OrderItem", on_delete=models.PROTECT, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class PaymentMethod(models.Model):

    CHOICES = (
        ('qr', 'QR'),
        ('credit', 'CREDIT'),
    )
    payment_id = models.ForeignKey("shop.Payment", on_delete=models.PROTECT, null=False)
    method = models.CharField(choices= CHOICES,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)