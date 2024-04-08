import http
import unittest
from functools import partial

from sanic_prometheus.metrics import _convert_status_to_int


class TestConvertStatusToInt(unittest.TestCase):
    def test__convert_status_to_int(self):
        assert _convert_status_to_int(200) == 200
        assert _convert_status_to_int(http.HTTPStatus.OK) == 200
        assert _convert_status_to_int("200") == 200

        assert _convert_status_to_int("abc") == 0
        assert _convert_status_to_int(None) == 0
        assert _convert_status_to_int(["1"]) == 0

