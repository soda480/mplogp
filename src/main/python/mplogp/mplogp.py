#   -*- coding: utf-8 -*-
import os
import sys
import logging
import argparse


logger = logging.getLogger(__name__)


def get_parser():
    """ return argument parser
    """
    parser = argparse.ArgumentParser(
        description='A log parser for parsing logs generated from multi-processing based tools')
    parser.add_argument(
        '--log',
        dest='log',
        type=str,
        required=True,
        help='Location of the logfile to parse')
    return parser


def configure_logging(name=None):
    """ configure logging
    """
    if not name:
        name = os.path.basename(sys.argv[0])
    rootLogger = logging.getLogger()
    # must be set to this level so handlers can filter from this level
    rootLogger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f'{name}.log')
    file_formatter = logging.Formatter("%(asctime)s %(processName)s [%(funcName)s] %(levelname)s %(message)s")
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    rootLogger.addHandler(file_handler)


def main():
    """ main function
    """
    args = get_parser().parse_args()
    configure_logging()
    logger.debug(args)


if __name__ == '__main__':  # pragma: no cover
    main()
