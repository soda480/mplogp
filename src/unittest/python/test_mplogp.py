#   -*- coding: utf-8 -*-
import unittest
from mock import patch
# from mock import call
# from mock import Mock
# from mock import MagicMock
import logging

from mplogp.mplogp import main
from mplogp.mplogp import configure_logging
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
    @patch('mplogp.mplogp.configure_logging')
    def test__main_Should_CallExpected_When_Called(self, *patches):
        main()

    @patch('mplogp.mplogp.sys.argv', ['arg1', 'arg2'])
    @patch('mplogp.mplogp.logging.FileHandler')
    def test_configure_logging_Should_CallExpected_When_CalledWithoutName(self, filehandler_patch, *patches):
        configure_logging()
        filehandler_patch.assert_called_once_with('arg1.log')

    @patch('mplogp.mplogp.logging.FileHandler')
    def test_configure_logging_Should_CallExpected_When_CalledWithName(self, filehandler_patch, *patches):
        configure_logging(name='mylog')
        filehandler_patch.assert_called_once_with('mylog.log')

    @patch('mplogp.mplogp.argparse.ArgumentParser')
    def test__get_parser_Should_ReturnExpected_When_Called(self, argumentparser_patch, *patches):
        result = get_parser()
        self.assertEqual(result, argumentparser_patch.return_value)
