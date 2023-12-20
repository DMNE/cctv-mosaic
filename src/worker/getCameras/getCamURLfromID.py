import logging
import requests

logger = logging.getLogger(__name__)

from src.support.config import local_ip, vs_config

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

cameras_payload = {
    'AdminLogin': vs_config['vs_admin_login'],
    'AdminPassword': vs_config['vs_admin_pass'],
    'UserLogin': vs_config['user_login'],
    'ClientIP': vs_config['client_ip'],
    'UserIP': local_ip,
}

def getCamURL(camera_ID):
    cameras_payload['CameraID'] = camera_ID

    vs_addr = "https://{vs_ip}{vs_url}".format(
        vs_ip = vs_config['vs_server_address'], 
        vs_url = vs_config['vs_get_translation_url'],
    )

    vs_request = requests.post(vs_addr, headers = headers, data = cameras_payload).json()
    logger.debug('VS ID response: {vs_request}'.format(vs_request = vs_request))

    return 'rtsp' + vs_request.get('URL')[4:]