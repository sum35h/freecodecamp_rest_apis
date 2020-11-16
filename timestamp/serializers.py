from rest_framework import serializers

class TimestampSerializer(serializers.Serializer):
   unix = serializers.IntegerField()
   utc = serializers.CharField()