from rest_framework import serializers
from api.models import Books
from api.models import Reviews

class BookSerializer(serializers.Serializer):
     id=serializers.IntegerField(read_only=True)
     name=serializers.CharField()
     author=serializers.CharField()
     price=serializers.IntegerField()
     publisher=serializers.CharField()
     qty=serializers.IntegerField()

     def create(self, validated_data):
          return Books.objects.create(**validated_data)

     def update(self, instance, validated_data):
          instance.name=validated_data.get("name")
          instance.author = validated_data.get("author")
          instance.price = validated_data.get("price")
          instance.publisher = validated_data.get("publisher")
          instance.qty = validated_data.get("qty")
          instance.save()
          return instance


     # field level validation
     def validate_price(self, value):
          if value not in range(50,5000):
               raise serializers.ValidationError("invalid price")
          return value

     def validate(self, value):
          if value not in range(1,5000):
               raise serializers.ValidationError("invalid qty")
          return value


     # object level validation

     # def validate(self, data):
     #      price=data.get("price")
     #      qty=data.get("qty")
     #     if qty not in range(1,5000):
     #          raise serializers.ValidationError("invalid error")
     #     if price not in range(50,1000):
     #          raise  serializers.ValidationError("invalid price")
     #     return data
     #









# class BookModelSerializer(serializers.ModelSerializer):
#      id=serializers.IntegerField(read_only=True)
#      class Meta:
#           model=Books
#           fields="__all__"
#

class ReviewSerializer(serializers.ModelSerializer):
     created_date=serializers.CharField(read_only=True)
     class meta:
          model=Reviews
          fields="__all__"
          # exclude=("created_date",)
