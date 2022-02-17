import email
import requests
import json
import base64
from django.conf import settings
from postmarker.core import PostmarkClient


class APIRequest:

    def __init__(self, data) -> None:
        self.preview_url = 'https://api.carfax.pro/wp-json/v1/get_report_check/{}'
        self.report_url = 'https://api.carfax.pro/wp-json/v1/get_report_by_wholesaler/{}/{}/{}/{}'

        self.api_key = 'e67ae95b59bd4f637d3ff804da40fe80'

        self.carfax_example_vin = 'WAUDG74F25N111998'
        self.vin = data['vin']
        self.email = data['email']

    def get_report(self,):
        r = requests.get(self.report_url.format(self.vin, self.api_key, 'carfax', 'en'))
        if r.status_code == 200:
            result = json.loads(r.text)
            code = result['report']['report']
            decoded_result = base64.b64decode(code)
            self.finish = decoded_result.decode('utf-8')
            if code:
                self.send_report_on_email()

            return self.finish
        raise AttributeError('Error with request')

    def get_preview_result(self):
        """
        check existing vin num in carfax api
        """
        r = requests.get(self.preview_url.format(self.vin))
        if r.status_code == 200:

            result = json.loads(r.text)
            if result['carfax']:
                return json.dumps(result['carfax'])
            return ''
        raise AttributeError('Error with request')
    

    def send_report_on_email(self,):
        try:
            postmark_client =PostmarkClient(server_token=settings.POSTMARK_API_KEY)
            postmark_client.emails.send(
                From=settings.POSTMARK_SENDER,
                To=self.email,
                Subject='Carfax report',
                HtmlBody=self.finish
            )
        except:
            pass
