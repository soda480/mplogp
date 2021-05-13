#   -*- coding: utf-8 -*-
import unittest
from mock import patch
# from mock import call
# from mock import Mock
# from mock import MagicMock
import logging

from mplogp.mplogp import main
from mplogp.mplogp import get_parser


logger = logging.getLogger(__name__)


class TestMplogp(unittest.TestCase):

    def setUp(self):
        """
        """
        pass

    def tearDown(self):
        """
        """
        pass

    @patch('mplogp.mplogp.get_parser')
    @patch('mplogp.mplogp.get_lines')
    @patch('mplogp.mplogp.parse_lines')
    @patch('mplogp.mplogp.write_logs')
    def test__main_Should_CallExpected_When_Called(self, write_logs_patch, *patches):
        main()
        write_logs_patch.assert_called_once()

    @patch('mplogp.mplogp.argparse.ArgumentParser')
    def test__get_parser_Should_ReturnExpected_When_Called(self, argumentparser_patch, *patches):
        result = get_parser()
        self.assertEqual(result, argumentparser_patch.return_value)
