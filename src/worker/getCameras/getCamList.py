import logging
import requests

logger = logging.getLogger(__name__)

from src.support.config import vs_config

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

vs_payload = {
    'AdminLogin': vs_config['vs_admin_login'],
    'AdminPassword': vs_config['vs_admin_pass'],
    'AccountID': vs_config['vs_account_id'],
}

def getCamList():
    cameras = []

    vs_addr = "https://{vs_ip}{vs_url}".format(
        vs_ip = vs_config['vs_server_address'], 
        vs_url = vs_config['vs_get_camera_id_url'],
    )
    
    vs_request = requests.post(vs_addr, headers = headers, data = vs_payload).json()

    for camera in vs_request:
        cameras.append([camera.get('ID'), camera.get('Name')])

    logger.debug('CamList: {vs_request}'.format(vs_request = cameras))

    return cameras