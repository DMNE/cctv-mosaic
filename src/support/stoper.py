import logging
import requests

logger = logging.getLogger(__name__)

from src.support.config import flussonic_config

headers = {
    'Authorization': flussonic_config['auth'],
}

def stoper(_sig_ign = None, _sig_dfl = None):
    from src.support.starter import args
    logger.warning('stoper!')
    
    count = int(args.mosaic)
    del_list = [flussonic_config['fluss_url'] + flussonic_config['mosaic_name']]

    for num in range(count):
        del_list.append('{url}{mosaic}_{name}_{num}'.format(
                                                url = flussonic_config['fluss_url'], 
                                                mosaic = flussonic_config['mosaic_name'], 
                                                name = flussonic_config['stream_name'], 
                                                num = num,
                                            ))

    for url in del_list:
        del_request = requests.delete(url, headers = headers)
        logger.warning('Stream {url} deleted with {code}'.format(url = url, code = del_request.status_code))
    
    logger.warning('All streams is deleted.')
    exit(0)