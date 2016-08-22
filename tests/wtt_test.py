import unittest
from unittest.mock import patch

from lib.wtt import WhatTheTrend, BASE_API_URL


class WTTTestCase(unittest.TestCase):
    def setUp(self):
        self.wtt = WhatTheTrend()

    def test_get_trends(self):
        trends = self.wtt.get_trends()

        self.assertTrue(isinstance(trends, list))
        self.assertGreater(len(trends), 0)

    @patch('requests.get')
    def test_requests_get(self, request_mock):
        trends_url = '{base}/trends.json'.format(base=BASE_API_URL)

        self.wtt._get(trends_url)

        request_mock.assert_called_with(trends_url, params=None)

if __name__ == '__main__':
    unittest.main()
