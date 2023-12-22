import logging
import requests

logger = logging.getLogger(__name__)

from src.support.stoper import stoper
from src.worker.mosaic.changeStream import changeStream

from src.support.config import flussonic_config

url = "fake://fake"
text = 'fake'
headers = {
    'Content-Type': 'application/json',
    'Authorization': flussonic_config['auth'],
}

def makeFlussStreams(cameras_count, size):
    try:

        streams = 'mosaic://' + ','.join([flussonic_config['mosaic_name'] + '_' + flussonic_config['stream_name'] + '_' + str(num) for num in range (cameras_count)])
        params = [
            'fps={fps}'.format(fps = flussonic_config['fps']),
            'preset={preset}'.format(preset = flussonic_config['preset']),
            'bitrate={bitrate}'.format(bitrate = flussonic_config['bitrate']),
            'size={size}'.format(size = size),
            'mosaic_size={cameras_count}'.format(cameras_count = cameras_count),
        ]
        streams = streams + '?' + '&'.join(params)
        logger.debug(streams)

        for num in range(cameras_count):
            changeStream(url, text, num)

        mosaic_url = flussonic_config['fluss_url'] + flussonic_config['mosaic_name']

        payload = {
            "inputs": [
                {"url": streams},
            ],
            "on_play": {
                "url": flussonic_config['on_play'],
            },
            "pushes": [
                {"url": flussonic_config['push']},
            ],
        }

        fluss_request = requests.put(mosaic_url, headers = headers, json = payload)
        logger.debug('Flussonic make stream {mosaic_url} response: {request}'.format(mosaic_url = mosaic_url, request = fluss_request.status_code))

    except Exception as err:
        logger.critical("Unexpected err = {err}, type(err) = {type}".format(err = err, type = type(err)))
        stoper(cameras_count)