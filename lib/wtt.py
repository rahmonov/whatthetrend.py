import json

from bs4 import BeautifulSoup
import requests

from lib.conf import BASE_API_URL, YAHOO_API_BASE_URI, YAHOO_CLIENT_ID


class WhatTheTrend:
    def _get_json(self, url, params=None):
        response = requests.get(url, params=params)

        if response.ok:
            return True, requests.get(url, params=params).json()

        return False, response.status_code

    def _get_text(self, url, params=None):
        response = requests.get(url, params=params)

        if response.ok:
            print(requests.get(url, params=params).text)
            return True, requests.get(url, params=params).text

        return False, response.status_code

    def get_trends(self):
        trends_url = '{base}/trends.json'.format(base=BASE_API_URL)
        ok, response = self._get_json(trends_url)

        if ok:
            return response['trends']

        return json.dumps({
            'message': 'Something went wrong. Please, try again later',
             'status': response
        })

    def get_woeid_by_name(self, name):
        places_url = "{0}/places.q({1})".format(YAHOO_API_BASE_URI, name)
        ok, response = self._get_text(places_url, {'appid': YAHOO_CLIENT_ID})

        if not ok:
            return json.dumps({
                'message': 'Something went wrong. Please, try again later',
                'status': response
            })

        soup = BeautifulSoup(response)
        return soup.woeid.text


