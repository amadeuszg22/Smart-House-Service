from django.contrib.auth.models import User, Group
from rest_framework import serializers
from configpanel.models import configweather, configdev
from django.utils import timezone

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class configweatherSerializer(serializers.Serializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    web = serializers.CharField(required=True, allow_blank=False, max_length=20)
    country = serializers.CharField(required=True, allow_blank=False, max_length=20)
    city = serializers.CharField(required=True, allow_blank=False, max_length=20)
    cityg = serializers.CharField(required=True, allow_blank=False, max_length=20)

    created_date = serializers.DateTimeField(
        default=timezone.now)
    published_date = serializers.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __str__(self):
     #   return self.web

    def create(self, validated_data):
        """
		Create and return a new `weather cahnnel conffigurations` instance, given the validated data.
		"""
        return configweather.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
		Update and return an existing `weather cahnnel conffigurations` instance, given the validated data.
		"""
        instance.web = validated_data.get('web', instance.web)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.cityg = validated_data.get('cityg', instance.cityg)
        instance.save()
        return instance

class configdevSerializer(serializers.Serializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(required=True, allow_blank=False, max_length=20)
    location = serializers.CharField(required=True, allow_blank=False, max_length=20)
    type = serializers.CharField(required=True, allow_blank=False, max_length=20)
    model = serializers.CharField(required=True, allow_blank=False, max_length=20)
    ip = serializers.CharField(required=True, allow_blank=False, max_length=20)

    created_date = serializers.DateTimeField(
        default=timezone.now)
    published_date = serializers.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __str__(self):
     #   return self.web

    def create(self, validated_data):
        """
		Create and return a new `weather cahnnel conffigurations` instance, given the validated data.
		"""
        return configdev.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
		Update and return an existing `weather cahnnel conffigurations` instance, given the validated data.
		"""
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.type = validated_data.get('type', instance.type)
        instance.model = validated_data.get('model', instance.model)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.save()
        return instance
