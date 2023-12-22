import logging
import requests

logger = logging.getLogger(__name__)

from src.support.config import flussonic_config

headers = {
    'Content-Type': 'application/json',
    'Authorization': flussonic_config['auth'],
}

def changeStream(url, text, num):
    stream_url = '{url}{mosaic}_{name}_{num}'.format(
                                                url = flussonic_config['fluss_url'], 
                                                mosaic = flussonic_config['mosaic_name'], 
                                                name = flussonic_config['stream_name'], 
                                                num = num,
                                            )

    payload = {
        "inputs": [
            {"url": url}, 
            {"url": flussonic_config['fluss_file']},
        ], 
        "source_timeout": 10,
        "transcoder": {
            "global": {
                "hw": "nvenc",
                "deviceid": "auto",
            },
            "video": [
                {
                    "bitrate": 1536000,
                    "track": 1,
                    "burn": {
                        "text": {
                            "text": text,
                            "position": "bl",
                            "x": 10,
                            "y": 10,
                        }
                    }
                }
            ]
        },
        "on_play": {
            "url": flussonic_config['on_play'],
        },
    }

    fluss_request = requests.put(stream_url, headers = headers, json = payload)
    logger.debug('Flussonic make stream {stream_url} with text {text} response: {request}'.format(stream_url = stream_url, text = text, request = fluss_request))