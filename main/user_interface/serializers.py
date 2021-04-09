from rest_framework import serializers
from .models import Product, Review, Custom
from rest_framework.response import Response
import collections


class ProductSerializer(serializers.ModelSerializer):
    """ Product serializer """

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        """ Product create method """

        return super().create(validated_data)

    def update(self, instance, validated_data):
        """ Product update method """

        instance.title = validated_data.get('title', instance.title)
        instance.decs = validated_data.get('decs', instance.decs)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def validate(self, data):
        """ Product validate method """

        if self.context['request'].user.is_superuser:
            return data
        else:
            raise serializers.ValidationError("You can not create because you are not a superuser")


class ReviewSerializer(serializers.ModelSerializer):
    """ Review serializer """

    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        """ Review create method """

        while True:
            try:
                Review.objects.filter(user=self.context['request'].user)[0]
                break
            except:
                validated_data['user'] = self.context['request'].user
                return super().create(validated_data)

        raise serializers.ValidationError("You can not create because you are already have review")

    def update(self, instance, validated_data):
        """ Review update method """

        if self.context['request'].user == validated_data['user']:
            print('yes')
            instance.text = validated_data.get('text', instance.text)
            instance.mark = validated_data.get('mark', instance.mark)
            instance.save()
        else:
            raise serializers.ValidationError("You can not create because it isn't your product")

        return instance

    def validate(self, data):
        """ Review validate method """

        if self.context['request'].user.is_authenticated:
            return data
        else:
            raise serializers.ValidationError("You can not create because you are not authenticated")


class CustomSerializer(serializers.ModelSerializer):
    """ Custom serializer """

    class Meta:
        model = Custom
        fields = "__all__"

    def get_fields(self):
        """ Custom method for getting info """

        if super().get_fields()['user'] == self.context['request'].user:
            return collections.OrderedDict()
        if self.context['request'].user.is_superuser:
            return super().get_fields()
        else:
            return collections.OrderedDict()

    def create(self, validated_data):
        """ Custom create method """

        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        """ Custom validate method """

        if self.context['request'].user.is_authenticated:
            return data
        else:
            raise serializers.ValidationError("You can not create because you are not authenticated")

    def update(self, instance, validated_data):
        """ Custom update method """

        if self.context['request'].user.is_superuser:
            instance.status = validated_data.get('status', instance.status)
            instance.save()
        else:
            raise serializers.ValidationError("You can not create because your aren't a superuser")

        return instance
