from rest_framework import serializers
from .models import Member, Product, ProductLike, Notification, Order, Contact

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'email', 'password', 'phone_number', 'picture_url', 'address', 'city', 'country', 'latitude', 'longitude', 'registered_time', 'status', 'products')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'member_id', 'name', 'picture_url', 'description', 'phone_number', 'weight', 'unit', 'quantity', 'pickup_time', 'lifespan', 'likes', 'requests', 'address', 'city', 'country', 'latitude', 'longitude', 'registered_time', 'is_like', 'orders', 'status', 'member_name', 'member_photo', 'lifespan_status', 'transaction_status')

class ProductLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_id', 'member_id', 'liked_time')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'receiver_id', 'message', 'sender_id', 'sender_name', 'sender_photo', 'sender_phone', 'date_time', 'option', 'order_id')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'member_id', 'product_id', 'phone_number', 'address', 'latitude', 'longitude', 'date_time', 'status')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'receiver_id', 'message', 'sender_id', 'sender_name', 'sender_photo', 'sender_phone', 'date_time', 'role', 'product_id', 'product_photo', 'option')





















































