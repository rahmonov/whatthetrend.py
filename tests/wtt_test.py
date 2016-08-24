import json
import unittest
from unittest.mock import patch

from lib.conf import BASE_API_URL, YAHOO_API_BASE_URI, YAHOO_CLIENT_ID
from lib.wtt import WhatTheTrend


class WTTTestCase(unittest.TestCase):
    def setUp(self):
        self.wtt = WhatTheTrend()

    @patch('requests.get')
    def test_requests_get_json(self, request_mock):
        trends_url = '{base}/trends.json'.format(base=BASE_API_URL)

        self.wtt._get_json(trends_url)

        request_mock.assert_called_with(trends_url, params=None)

    @patch('requests.get')
    def test_requests_get_text(self, request_mock):
        place_url = "{0}/places.q({1})".format(YAHOO_API_BASE_URI, "new york")

        self.wtt._get_text(place_url)

        request_mock.assert_called_with(place_url, params=None)

    @patch('lib.wtt.WhatTheTrend._get_json')
    def test_get_trends(self, mock_get):
        with open('tests/fixtures/trends.json', 'r') as file:
            trends_json = json.loads(file.read())

        mock_get.return_value = (True, trends_json)

        trends = self.wtt.get_trends()

        self.assertGreater(len(trends), 0)
        self.assertEqual(trends[0]['name'], '#FelizMartes')
        self.assertEqual(trends[1]['name'], '#traingate')

        mock_get.assert_called_with(
            '{base}/trends.json?woeid=None'.format(base=BASE_API_URL))

    @patch('lib.wtt.WhatTheTrend._get_text')
    def test_get_yahoo_woeid_by_name(self, mock_get_text):
        with open('tests/fixtures/opera_house.xml', 'r') as file:
            opera_house_xml = file.read()

        with open('tests/fixtures/niagara.xml', 'r') as file:
            niagara_xml = file.read()

        mock_get_text.return_value = (True, opera_house_xml)

        opera_house_woeid = self.wtt._get_woeid_by_name('Sydney Opera House')
        self.assertEqual(opera_house_woeid, '28717584')
        mock_get_text.assert_called_with(
            "{0}/places.q({1})".format(YAHOO_API_BASE_URI, 'Sydney Opera House'),
            {'appid': YAHOO_CLIENT_ID})

        mock_get_text.return_value = (True, niagara_xml)

        niagara_falls_woeid = self.wtt._get_woeid_by_name('niagara falls')
        self.assertEqual(niagara_falls_woeid, '28299078')
        mock_get_text.assert_called_with(
            "{0}/places.q({1})".format(YAHOO_API_BASE_URI, 'niagara falls'),
            {'appid': YAHOO_CLIENT_ID})

    def test_get_location_code(self):
        country_code = self.wtt._get_location_code('Country')
        region_code = self.wtt._get_location_code('region')
        state_code = self.wtt._get_location_code('state')
        state_region_code = self.wtt._get_location_code('region/state')

        self.assertEqual(country_code, 12)
        self.assertEqual(region_code, 8)
        self.assertEqual(state_code, 8)
        self.assertEqual(state_region_code, 8)

        with self.assertRaises(AttributeError):
            self.wtt._get_location_code('unknown')

if __name__ == '__main__':
    unittest.main()
