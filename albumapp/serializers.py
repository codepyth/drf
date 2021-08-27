from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'file']

    # def create(self, validated_data):
    #     image = validated_data.pop('file')
    #     name = validated_data.pop('name')
    #     for img in image:
    #         photo = Album.objects.create(
    #             name=name,
    #             file=img, **validated_data)
    #     return photo


# def create(self, validated_data):
#         items = validated_data.pop('order_items')
#         order = Order.objects.create(**validated_data)

#         products = [li['product'] for li in items]
#         quantities = [li['quantity'] for li in items]
#         prices = [li['price'] for li in items]
#         discounts = [li['discount'] for li in items]
#         sub_totals = [li['sub_total'] for li in items]
#         for index in range(len(products)):
#             OrderDetails.objects.create(order=order,
#                                         product=products[index],
#                                         quantity=quantities[index],
#                                         price=prices[index],
#                                         discount=discounts[index],
#                                         sub_total=sub_totals[index],
#                                         )
#         return order
