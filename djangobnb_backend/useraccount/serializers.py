from rest_framework import serializers

from .models import User

class UserDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()  

    class Meta:
        model = User
        fields = ('id', 'name', 'avatar_url')

    def get_name(self, obj):
        return obj.name if obj.name else "Unknown User"  
