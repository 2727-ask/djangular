from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.parent = validated_data.get('body', instance.parent)
        instance.save()
        return instance