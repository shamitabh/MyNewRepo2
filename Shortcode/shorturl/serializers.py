from rest_framework import serializers
from .models import Shortcode


class SetShortcodeSerializer(serializers.ModelSerializer):
    """serializer class for setting shortcode for url"""
    class Meta:
        model = Shortcode
        fields = ('url', 'shortcode')

    def validate_shortcode(self, attr):
        """validate code length"""
        if len(attr) and len(attr) < 6:
            raise serializers.ValidationError(
                ["Code length should be equal to 6."])
        return attr


class GetShortcodeSerializer(serializers.ModelSerializer):
    """serializer class for getting shortcode for url"""
    class Meta:
        model = Shortcode
        fields = ('shortcode',)


class GetShortcodeStatsSerializer(serializers.ModelSerializer):
    """serializer class for getting stats of a shortcode"""
    class Meta:
        model = Shortcode
        fields = ('created_at', 'lastRedirect', 'redirectCount')
