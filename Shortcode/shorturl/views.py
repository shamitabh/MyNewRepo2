from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import SetShortcodeSerializer, GetShortcodeSerializer, GetShortcodeStatsSerializer
from .models import Shortcode
import string
import requests
from django.shortcuts import get_object_or_404


def verify_code(code):
    """validate correctness of API code"""
    if len(code) < 6:
        return False
    else:
        ref = string.ascii_lowercase + \
            string.ascii_uppercase + string.digits + string.punctuation[26]
        for i in code:
            if i not in ref:
                return False
    return True


def verify_url(url):
    """validate existence of url"""
    try:
        requests.get(url)
    except:
        return False
    else:
        return True


class ShortCodeAPIView(generics.GenericAPIView):
    """class based API view for setting shortcode for urls"""
    serializer_class = SetShortcodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if data.get('shortcode'):
            if Shortcode.objects.filter(shortcode=data.get('shortcode')).exists():
                return Response({"shortcode": ["Shortcode already exists."]}, status=status.HTTP_409_CONFLICT)
            elif not verify_code(data.get('shortcode')):
                return Response({"shortcode": ["Provided shortcode is invalid."]}, status=status.HTTP_412_PRECONDITION_FAILED)
        if not verify_url(data.get('url')):
            return Response({"url": ["Url is not present."]}, status=status.HTTP_400_BAD_REQUEST)
        url = serializer.save()
        return Response(GetShortcodeSerializer(url).data, status=status.HTTP_201_CREATED)


class GetShortcodeStatsAPIView(generics.GenericAPIView):
    """class based API view for getting stats of a shortcode"""
    serializer_class = GetShortcodeStatsSerializer

    def get(self, request, code, *args, **kwargs):
        # url_exists = Shortcode.objects.filter(shortcode=code).exists()
        url = get_object_or_404(Shortcode, shortcode=code)
        serializer = self.get_serializer(instance=url)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GoToUrlAPIView(APIView):
    """class based API view for redirecting to the url of a valid code"""

    def get(self, request, code):
        url_obj = get_object_or_404(Shortcode, shortcode=code)
        url_obj.redirectCount += 1
        url_obj.save()
        return Response({}, status=status.HTTP_302_FOUND, headers={'Location': url_obj.url})
