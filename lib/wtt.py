import json

from bs4 import BeautifulSoup
import requests

from lib.conf import BASE_API_URL, YAHOO_API_BASE_URI, YAHOO_CLIENT_ID, \
    BASE_API_URL_V1
from lib.responses import JSONResponse

LOCATION_CODES = {
    'earth': 19,
    'country': 12,
    'region': 8,
    'state': 8,
    'town': 7
}


class WhatTheTrend:
    def _get_json(self, url, params=None):
        response = requests.get(url, params=params)

        if response.ok:
            return True, requests.get(url, params=params).json()

        return False, response.status_code

    def _get_text(self, url, params=None):
        response = requests.get(url, params=params)

        if response.ok:
            return True, requests.get(url, params=params).text

        return False, response.status_code

    def _get_woeid_by_name(self, name):
        places_url = "{0}/places.q({1})".format(YAHOO_API_BASE_URI, name)
        ok, response = self._get_text(places_url, {'appid': YAHOO_CLIENT_ID})

        if not ok:
            return json.dumps({
                'message': 'Something went wrong. Please, try again later',
                'status': response
            })

        soup = BeautifulSoup(response)
        return soup.woeid.text

    def _get_location_code(self, location):
        location = location.lower()

        if location in LOCATION_CODES.keys():
            return LOCATION_CODES[location]

        if 'state' in location or 'region' in location:
            return LOCATION_CODES['state']

        raise AttributeError("Wrong location type")

    def get_trends(self, around=None):
        woeid = None
        if around:
            woeid = self._get_woeid_by_name(around)

        trends_url = '{base}/trends.json?woeid={id}'.format(base=BASE_API_URL,
                                                            id=woeid)
        ok, response = self._get_json(trends_url)

        if ok:
            return JSONResponse(ok=ok, data=response['trends'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_active_trends(self):
        active_trends_url = '{base}/trends/active.json'.format(
            base=BASE_API_URL)

        ok, response = self._get_json(active_trends_url)

        if ok:
            return JSONResponse(ok=ok, data=response['trends'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_spammy_trends(self):
        spammy_trends_url = '{base}/trends/active.json'.format(
            base=BASE_API_URL)

        ok, response = self._get_json(spammy_trends_url)

        if ok:
            return JSONResponse(ok=ok, data=response['trends'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_trends_by_location(self, location='earth'):
        location_code = self._get_location_code(location)
        location_trends_url = '{base}/trends/locations/top.json?place_type_code={code}'.format(
            base=BASE_API_URL, code=location_code)

        ok, response = self._get_json(location_trends_url)

        if ok:
            return JSONResponse(ok=ok, data=response['trends'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_categories(self):
        categories_url = '{base}/categories.json'.format(base=BASE_API_URL)

        ok, response = self._get_json(categories_url)

        if ok:
            return JSONResponse(ok=ok, data=response['categories'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_trendy_locations(self):
        trendy_locations_url = '{base}/locations/current.json'.format(
            base=BASE_API_URL)

        ok, response = self._get_json(trendy_locations_url)

        if ok:
            return JSONResponse(ok=ok, data=response['locations'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_locations(self):
        all_locations_url = '{base}/locations/all.json'.format(
            base=BASE_API_URL)

        ok, response = self._get_json(all_locations_url)

        if ok:
            return JSONResponse(ok=ok, data=response['locations'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def search_trend(self, q):
        if not q:
            return list()

        search_url = '{base}/trend/search'.format(base=BASE_API_URL_V1)

        ok, response = self._get_text(search_url, params={'q': q})

        if ok:
            return JSONResponse(
                ok=ok, data=list(map(str.strip, response.split('\n'))))

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def extended_search_trend(self, q, count=10):
        if not q:
            return list()

        search_url = '{base}/trend/search_extended/json'.format(
            base=BASE_API_URL_V1)

        ok, response = self._get_json(
            search_url, params={'q': q, 'count': count})

        if ok:
            return JSONResponse(ok=ok, data=response['api']['trends']["trend"])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)

    def get_trend_by_id(self, id, versions=-1):
        if not id:
            raise ValueError("Provide a valid id.")

        trend_url = '{base}/trend/getById/{id}/json'.format(
            base=BASE_API_URL_V1, id=id)

        ok, response = self._get_json(trend_url, params={'versions': versions})

        if ok:
            return JSONResponse(ok=ok, data=response['api']['trend'])

        return JSONResponse(
            message='Something went wrong. Please, try again later',
            status=response)
