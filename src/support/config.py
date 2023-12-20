import logging

logger = logging.getLogger(__name__)

import configparser
import socket

local_host_name = socket.gethostname()
local_ip = socket.gethostbyname(socket.gethostname())

from src.support.starter import args

config_ini = args.config

config = configparser.ConfigParser()
config.read(config_ini)

default_config = config['DEFAULT']
vs_config = config['vs']
flussonic_config = config['flussonic']
mosaic = config['mosaic.size']

mosaic_size = default_config['mosaic_size']

logger.debug(config)