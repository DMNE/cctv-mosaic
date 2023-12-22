import logging

logger = logging.getLogger(__name__)

import argparse

parser = argparse.ArgumentParser(
    description = 'Make mosaic of cameras. Correct mosaic size: 1, 2, 4, 6, 8, 9, 12.', 
    add_help = True, 
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    '-v',
    '--version',
    action = 'version',
    version = 'CCTV Mosaic Maker 1.0.1'
)

parser.add_argument(
    '-m',
    '--mosaic',
    choices = ['1', '2', '4', '6', '8', '9', '12'],
    default = '6',
    help = 'Choose number of cameras in mosaic.',
    type = str,
)

parser.add_argument(
    '-c', 
    '--config', 
    default = './config/config.ini',
    type = str, 
    help = 'Change config location.',
)

args = parser.parse_args()
logger.debug(args)