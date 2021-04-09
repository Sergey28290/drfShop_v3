from rest_framework import serializers
from .models import Collections
import collections


class CollectionsSerializer(serializers.ModelSerializer):
    """ Collection serializer """

    class Meta:
        model = Collections
        fields = "__all__"

    def create(self, validated_data):
        """ Collection create method """

        return super().create(validated_data)

    def validate(self, data):
        """ Collections validate method """

        if self.context['request'].user.is_superuser:
            return data
        else:
            raise serializers.ValidationError("You can not create because you are not a superuser")

    def update(self, instance, validated_data):
        """ Collections update method """

        return super().update(instance, validated_data)
