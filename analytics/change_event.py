from rest_framework import serializers


class ChangeEventSerializer(serializers.Serializer):
	row = serializers.IntegerField()
	col = serializers.IntegerField()
	pre = serializers.CharField()
	val = serializers.CharField()