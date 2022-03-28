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

        self.api_key = settings.CARFAX_KEY

        self.carfax_example_vin = 'WAUDG74F25N111998'
        self.vin = data['vin']
        if 'email' in data:
            self.email = data['email']

    def get_report(self,):
        r = requests.get(self.report_url.format(self.vin, self.api_key, 'carfax', 'en'))
        if r.status_code == 200:
            result = json.loads(r.text)
            self.code = result['report']['report']
            decoded_result = base64.b64decode(self.code)
            self.finish = decoded_result.decode('utf-8')
            
            import pdfkit
            try:
                pdfkit.from_string(self.finish, 'result.pdf')
            except Exception as e:
                print(e)


            if self.code:
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
        import requests
        with open('result.pdf', 'rb') as f:
            content = base64.b64encode(f.read()).decode('utf-8')

        print(type(content))

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Postmark-Server-Token": settings.POSTMARK_API_KEY
        }

        data = {
            "From": settings.POSTMARK_SENDER,
            "To": self.email,
            "Subject": 'Carfax report',
            "HtmlBody": 'Here is your report 2',
            "Attachments": [
                {
                    "Name": "report.pdf",
                    "Content": content,
                    "ContentType": "application/pdf"
                }
            ]
        }
        URL = 'https://api.postmarkapp.com/email'
        r = requests.post(URL, headers=headers, data=json.dumps(data))
        print(r.status_code, r.text)
