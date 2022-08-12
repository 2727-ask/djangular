from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category, BlogPost, User, Profile

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_title = validated_data.get(
            'blog_title', instance.blog_title)
        instance.blog_desc = validated_data.get(
            'blog_desc', instance.blog_desc)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance



   

class SignUpUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self,validated_data):
        print("Validated Data is",validated_data)
        user = User(
            username=validated_data.get('username')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
