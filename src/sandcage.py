# -*- coding: utf-8 -*-
import requests
import os


class SandCage:
    API_ROOT = 'https://api.sandcage.com/'  # API root
    API_VERSION = '0.2'  # API version
    TIMEOUT = 30  # timeout in seconds
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    TRUSTED = os.path.join(__location__, 'cacert.pem')

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.sandcage_api_endpoint = '{0}/{1}/'.format(self.API_ROOT, self.API_VERSION)
        self.user_agent = '{0} - {1}'.format('SandCage', self.API_VERSION)

    def call(self, endpoint, post=False, data=None):
        """
        call endpoint

        :type endpoint: str
        :type post: bool
        :type data: dict
        :rtype: Response
        """
        headers = {'User-Agent': self.user_agent}
        if post:
            r = requests.post(endpoint, headers=headers, timeout=self.TIMEOUT, json=data, verify=self.TRUSTED)
        else:
            r = requests.get(endpoint, headers=headers, timeout=self.TIMEOUT, verify=self.TRUSTED)
        return r

    def get_info(self, payload=None):
        """
        get-info method

        :type payload: dict
        :rtype: Response
        """
        return self.call(self.sandcage_api_endpoint + 'get-info', post=True, data=self._get_data(payload))

    def list_files(self, payload=None):
        """
        list-files method

        :type payload: dict
        :rtype: Response
        """
        return self.call(self.sandcage_api_endpoint + 'list-files', post=True, data=self._get_data(payload))

    def destroy_files(self, payload=None, callback_endpoint=None):
        """
        destroy-files method

        :type payload: dict
        :type callback_endpoint: str
        :rtype: Response
        """
        data = self._get_data(payload)
        self._update_callback(data, callback_endpoint)
        return self.call(self.sandcage_api_endpoint + 'destroy-files', post=True, data=data)

    def schedule_files(self, payload=None, callback_endpoint=None):
        """
        schedule-tasks method

        :type payload: dict
        :type callback_endpoint: str
        :rtype: Response
        """
        data = self._get_data(payload)
        self._update_callback(data, callback_endpoint)
        return self.call(self.sandcage_api_endpoint + 'schedule-tasks', post=True, data=data)

    def _get_data(self, payload=None):
        d = {'key': self.api_key}
        if payload:
            d.update(payload)
        return d

    @staticmethod
    def _update_callback(data, callback_endpoint=None):
        if callback_endpoint:
            data.update({'callback_url': callback_endpoint})
