from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    picture_url = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    registered_time = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    products = models.CharField(max_length=11)
    fcm_token = models.CharField(max_length=2000)


class Product(models.Model):
    member_id = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    picture_url = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=30)
    weight = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20)
    pickup_time = models.CharField(max_length=200)
    lifespan = models.CharField(max_length=20)
    likes = models.CharField(max_length=20)
    requests = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    registered_time = models.CharField(max_length=50)
    is_like = models.CharField(max_length=20)
    orders = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    member_name = models.CharField(max_length=50)
    member_photo = models.CharField(max_length=1000)
    lifespan_status = models.CharField(max_length=20)
    transaction_status = models.CharField(max_length=20)


class ProductLike(models.Model):
    product_id = models.CharField(max_length=11)
    member_id = models.CharField(max_length=11)
    liked_time = models.CharField(max_length=50)


class Notification(models.Model):
    receiver_id = models.CharField(max_length=11)
    message = models.CharField(max_length=1000)
    sender_id = models.CharField(max_length=11)
    sender_name = models.CharField(max_length=50)
    sender_photo = models.CharField(max_length=1000)
    sender_phone = models.CharField(max_length=50)
    date_time = models.CharField(max_length=100)
    option = models.CharField(max_length=50)
    order_id = models.CharField(max_length=11)


class Order(models.Model):
    member_id = models.CharField(max_length=11)
    product_id = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date_time = models.CharField(max_length=100)
    status = models.CharField(max_length=20)


class Feedback(models.Model):
    member_id = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    picture_url = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    feedback = models.CharField(max_length=2000)
    date_time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class Ambassador(models.Model):
    member_id = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    picture_url = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
    date_time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class Transaction(models.Model):
    product_id = models.CharField(max_length=11)
    member_id = models.CharField(max_length=11)
    date_time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class Account(models.Model):
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)


class Contact(models.Model):
    receiver_id = models.CharField(max_length=11)
    message = models.CharField(max_length=1000)
    sender_id = models.CharField(max_length=11)
    sender_name = models.CharField(max_length=50)
    sender_photo = models.CharField(max_length=1000)
    sender_phone = models.CharField(max_length=50)
    date_time = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    product_id = models.CharField(max_length=11)
    product_photo = models.CharField(max_length=1000)
    option = models.CharField(max_length=20)




class Mm(models.Model):
    value = models.CharField(max_length=45)


































