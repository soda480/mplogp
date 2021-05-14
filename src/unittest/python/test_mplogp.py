#   -*- coding: utf-8 -*-
import unittest
from mock import patch
from mock import call
# from mock import Mock
from mock import mock_open
# from mock import MagicMock
import logging

from mplogp.mplogp import main
from mplogp.mplogp import get_parser
from mplogp.mplogp import get_lines
from mplogp.mplogp import parse_lines
from mplogp.mplogp import get_timestamp
from mplogp.mplogp import get_alias
from mplogp.mplogp import write_logs


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

    @patch('mplogp.mplogp.open', create=True)
    def test__get_lines_Should_ReturnExpected_When_Called(self, open_patch, *patches):
        open_patch.side_effect = [
            mock_open(read_data='--data--').return_value
        ]
        result = get_lines('program.log')
        expected_result = ['--data--']
        self.assertEqual(result, expected_result)

    def test__parse_lines_Should_ReturnExpected_When_Called(self, *patches):
        lines = [
            '2021-05-14 21:16:54,334 MainProcess line1\n',
            '2021-05-14 21:16:54,334 Process-1 line2\n',
            '2021-05-14 21:16:54,334 Process-1 line3\n',
            '2021-05-14 21:16:54,334 Process-2 line4\n',
            '2021-05-14 21:16:54,334 line5\n',
            '2021-05-14 21:16:54,334 MainProcess line6\n',
            '2021-05-14 21:16:54,334 Process-1 line7\n',
            '2021-05-14 21:16:54,334 Process-2 line8\n'
        ]
        result = parse_lines(lines)
        expected_result = {
            'MainProcess': [
                '2021-05-14 21:16:54,334 MainProcess line1\n',
                '2021-05-14 21:16:54,334 MainProcess line6\n'
            ],
            'Process-1': [
                '2021-05-14 21:16:54,334 Process-1 line2\n',
                '2021-05-14 21:16:54,334 Process-1 line3\n',
                '2021-05-14 21:16:54,334 Process-1 line7\n'
            ],
            'Process-2': [
                '2021-05-14 21:16:54,334 Process-2 line4\n',
                '2021-05-14 21:16:54,334 line5\n',
                '2021-05-14 21:16:54,334 Process-2 line8\n'
            ]
        }
        self.assertEqual(result, expected_result)

    def test__get_timestamp_Should_ReturnExpected_When_NoMatch(self, *patches):
        result = get_timestamp('line2')
        expected_result = ''
        self.assertEqual(result, expected_result)

    def test__get_timestamp_Should_ReturnExpected_When_Match(self, *patches):
        result = get_timestamp('2021-05-14 21:16:54,334 MainProcess line1\n')
        expected_result = '2021-05-14_21-16-54'
        self.assertEqual(result, expected_result)

    def test__get_alias_Should_ReturnExpected_When_Match(self, *patches):
        regex = r'^.*processor id (?P<value>.*)$'
        lines = [
            '2021-05-14 21:16:54,334 Process-1 line2\n',
            '2021-05-14 21:16:54,334 Process-1 processor id 121372\n',
            '2021-05-14 21:16:54,334 Process-1 line4\n',
        ]
        result = get_alias(regex, lines)
        expected_result = '-121372'
        self.assertEqual(result, expected_result)

    def test__get_alias_Should_ReturnExpected_When_NoMatch(self, *patches):
        regex = r'^.*processor id (?P<value>.*)$'
        lines = [
            '2021-05-14 21:16:54,334 Process-1 line2\n',
            '2021-05-14 21:16:54,334 Process-1 line3\n',
            '2021-05-14 21:16:54,334 Process-1 line4\n',
        ]
        result = get_alias(regex, lines)
        expected_result = ''
        self.assertEqual(result, expected_result)

    def test__get_alias_Should_ReturnExpected_When_NoRegex(self, *patches):
        regex = ''
        lines = [
            '2021-05-14 21:16:54,334 Process-1 line2\n',
            '2021-05-14 21:16:54,334 Process-1 line3\n',
            '2021-05-14 21:16:54,334 Process-1 line4\n',
        ]
        result = get_alias(regex, lines)
        expected_result = ''
        self.assertEqual(result, expected_result)

    @patch('mplogp.mplogp.os.path.exists', return_value=False)
    @patch('mplogp.mplogp.open', create=True)
    @patch('mplogp.mplogp.os.makedirs')
    @patch('mplogp.mplogp.get_alias')
    @patch('mplogp.mplogp.get_timestamp')
    def test__write_logs_Should_CallExpected_When_TimestampAndPathDoesNotExist(self, get_timestamp_patch, get_alias_patch, makedirs_patch, open_patch, *patches):
        get_alias_patch.return_value = '-alias'
        get_timestamp_patch.return_value = 'timestamp'
        get_alias.side_effect = ['alias1', 'alias2']
        parsed = {
            'MainProcess': ['line1', 'line2'],
            'Process-1': ['line1', 'line2']
        }
        regex = r'regex'
        write_logs('logs', parsed, regex=regex)
        makedirs_patch.assert_called_once_with('logs/timestamp')
        call1 = call('logs/timestamp/Process-1-alias.log', 'w')
        self.assertTrue(call1 in open_patch.mock_calls)

    @patch('mplogp.mplogp.os.path.exists', return_value=True)
    @patch('mplogp.mplogp.open', create=True)
    @patch('mplogp.mplogp.os.makedirs')
    @patch('mplogp.mplogp.get_alias')
    @patch('mplogp.mplogp.get_timestamp')
    def test__write_logs_Should_CallExpected_When_NoTimestampAndPathExists(self, get_timestamp_patch, get_alias_patch, makedirs_patch, open_patch, *patches):
        get_timestamp_patch.return_value = ''
        get_alias.side_effect = ['alias1', 'alias2']
        parsed = {
            'MainProcess': ['line1', 'line2'],
            'Process-1': ['line1', 'line2']
        }
        regex = r'regex'
        write_logs('logs', parsed, regex=regex)
        makedirs_patch.assert_not_called()
