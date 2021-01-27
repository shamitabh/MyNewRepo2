from django.test import TestCase
from django.urls import reverse
from .models import Shortcode
from mixer.backend.django import mixer


class TestShortCode(TestCase):
    set_shortcode_url = reverse('set_code')

    def test_shortcode_assignment_without_url(self):
        """verify url is a mandatory field for assigning shortcodes"""
        response = self.client.post(self.set_shortcode_url, data={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['url'][0], 'This field is required.')

    def test_shortcode_assignment_with_invalid_url(self):
        """verify url should be valid"""
        payload = {
            "url": "htsadsdasdsd",
            "shortcode": "SSA232"
        }
        response = self.client.post(self.set_shortcode_url, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['url'][0],
                         'Url is not present.')

    def test_shortcode_assignment_without_shortcode(self):
        """verify shortcode is not mandatory"""
        payload = {
            "url": "https://google.com",
        }
        response = self.client.post(self.set_shortcode_url, data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Shortcode.objects.get(url=payload['url']).shortcode)

    def test_shortcode_assignment_with_shortcode_with_length_less_than_6(self):
        """verify shorcode shouold have length equal to 6"""
        payload = {
            "url": "https://google.com",
            "shortcode": "qwe"
        }
        response = self.client.post(self.set_shortcode_url, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['shortcode'][0],
                         'Code length should be equal to 6.')

    def test_shortcode_assignment_with_existing_shortcode(self):
        """verify existing shortcode cannot be used for assigning new urls"""
        url = mixer.blend(Shortcode)

        payload = {
            "url": "https://google.com",
            "shortcode": url.shortcode
        }
        response = self.client.post(self.set_shortcode_url, data=payload)
        self.assertEqual(response.data['shortcode'][0],
                         'shortcode with this shortcode already exists.')

    def test_shortcode_assignment_with_valid_data(self):
        """verify shortcode assignment with valid data"""
        payload = {
            "url": "https://google.com",
            "shortcode": "223AAS"
        }
        response = self.client.post(self.set_shortcode_url, data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Shortcode.objects.get(
            url=payload['url']).shortcode, payload['shortcode'])

    def test_stats(self):
        """verify stats are returned for a valid shortcode"""
        url_obj = mixer.blend(Shortcode)
        url = reverse('get_stats', kwargs={'code': url_obj.shortcode})
        response = self.client.get(url)
        self.assertTrue(response.data['lastRedirect'])
        self.assertTrue(response.data['created_at'])
        self.assertEqual(response.data['redirectCount'], url_obj.redirectCount)
