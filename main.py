from time import sleep
import signal

import logging
import logging.config
import logging.handlers

from src.support.config import default_config, mosaic

logging_file = default_config['logging']

logging.config.fileConfig(logging_file, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.debug('--- server start ---')

from src.support.starter import args
from src.support.makeFlussStreams import makeFlussStreams
from src.support.stoper import stoper

from src.worker.getCameras.getCamList import getCamList
from src.worker.getCameras.getCamURLfromID import getCamURL
from src.worker.mosaic.changeStream import changeStream

camera_count = int(args.mosaic)
size = mosaic[args.mosaic]

count = 0
cameras = getCamList()

makeFlussStreams(camera_count, size)

def main():
    global count, cameras

    try:

        for num in range(camera_count):
            id, name = cameras[count]
            logger.debug('Count = {count}'.format(count = count))

            url = getCamURL(id)
            text = 'Camera ID - {id}\n{name}'.format(test = '\n', id = str(id), name = name)
            changeStream(url, text, num)

            if count < len(cameras) - 1:
                count += 1
            else:
                count = 0
                cameras = getCamList()

        sleep(60.0)

    except KeyboardInterrupt:
        logger.warning('Server STOPed with KeyboardInterrupt!')
        stoper()

    except InterruptedError as int_err:
        logger.critical('Some exception! Server is stop now! Exception is : {}'.format(int_err))
        stoper()

    except Exception as err:
        logger.critical("Unexpected err = {err}, type(err) = {type}".format(err = err, type = type(err)))
        stoper()

    finally:
        logger.debug('...')

signal.signal(signal.SIGINT, stoper)
signal.signal(signal.SIGTERM, stoper)

if __name__ == "__main__":
    while True:
        main()