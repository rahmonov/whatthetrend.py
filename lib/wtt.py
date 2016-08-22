import requests
from requests import Response

BASE_API_URL = "http://api.whatthetrend.com/api/v2"


class WhatTheTrend:
    def _get(self, url, params=None):
        return requests.get(url, params=params)

    def get_trends(self):
        trends_url = '{base}/trends.json'.format(base=BASE_API_URL)
        return self._get(trends_url).json()['trends']
