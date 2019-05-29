# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest,time

import openadk
from openadk.api.media_api import MediaApi  # noqa: E501
from openadk.rest import ApiException

from openadk.models.name import Name
from openadk.models.media_music_operation import MediaMusicOperation


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self):
        self.configuration = openadk.Configuration()
        self.configuration.host = 'http://10.10.60.131:9090/v1'
        self.api_instance = MediaApi(openadk.ApiClient(self.configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_media_music(self):
        """Test case for delete_media_music

        Delete uploaded music  # noqa: E501
        """
        # delete nonexistent music
        name = 'unknown_music'
        body = Name(name=name)
        ret = self.api_instance.delete_media_music(body=body)
        self.assertEqual(ret.code, 120, ret)

        # delete existent music
        name = 'little_frog.mp3'
        file = 'files/' + name
        ret = self.api_instance.post_media_music(file)
        self.assertEqual(ret.code, 0, ret)
        body = Name(name=name)
        ret = self.api_instance.delete_media_music(body=body)
        self.assertEqual(ret.code, 0, ret)

    def test_get_media_music(self):
        """Test case for get_media_music

        Get the music playing status  # noqa: E501
        """
        # get status while playing
        data = {'operation': 'start', 'name': 'Little_Apple.mp3'}
        body = MediaMusicOperation(operation=data['operation'], name=data['name'])
        ret = self.api_instance.put_media_music(body)
        self.assertEqual(ret.code, 0, ret)
        self.assertNotEqual(ret.data, None, ret)

        ret = self.api_instance.get_media_music()  # return MediaMusicStatusResponse instance 
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(ret.data.name, data['name'], ret)
        self.assertEqual(ret.data.status, 'run', ret)

        # get status after stop
        data['operation'] = 'stop'
        body = MediaMusicOperation(operation=data['operation'], name=data['name'])
        ret = self.api_instance.put_media_music(body)
        self.assertEqual(ret.code, 0, ret)

        ret = self.api_instance.get_media_music()   # return MediaMusicStatusResponse instance 
        self.assertEqual(ret.code, 0, ret)
        self.assertEqual(ret.data.name, '', ret)
        self.assertEqual(ret.data.status, 'idle', ret)

    def test_get_media_music_list(self):
        """Test case for get_media_music_list

        Get the music list  # noqa: E501
        """
        ret = self.api_instance.get_media_music_list()  # return MediaMusicListResponse instance 
        some_music = Name(name='Little_Apple.mp3')
        self.assertEqual(ret.code, 0, ret)
        self.assertNotEqual(len(ret.data.music), 0, ret)
        self.assertEqual(some_music in ret.data.music, True, ret)

    def test_post_media_music(self):
        """Test case for post_media_music

        Upload music  # noqa: E501
        """

        for name in ['my_waka.hts', 'little_frog.mp3', 'my_waka.zip']:
            file = 'files/' + name
            ret = self.api_instance.post_media_music(file)
            if file.endswith('mp3') or file.endswith('wav'):
                self.assertEqual(ret.code, 0, ret)
                # check if in list or not
                ret = self.api_instance.get_media_music_list()  # return MediaMusicListResponse instance 
                some_music = Name(name=name)
                self.assertEqual(ret.code, 0, ret)
                self.assertEqual(some_music in ret.data.music, True, ret)
                # check if can be played or not
                body = MediaMusicOperation(operation='start', name=name)
                ret = self.api_instance.put_media_music(body)
                self.assertEqual(ret.code, 0, ret)
                self.assertNotEqual(ret.data, None, ret)
                time.sleep(3.0)
                body = MediaMusicOperation(operation='stop', name=name)
                ret = self.api_instance.put_media_music(body)
                self.assertEqual(ret.code, 0, ret)
            else:
                self.assertEqual(ret.code, 121, ret)

    def test_put_media_music(self):
        """Test case for put_media_music

        Start or stop music  # noqa: E501
        """
        test_data = [{'operation': 'start', 'name': 'Little_Apple.mp3'},
                     {'operation': 'stop', 'name': 'Little_Apple.mp3'}]
        for data in test_data:
            body = MediaMusicOperation(operation=data['operation'], name=data['name'])
            ret = self.api_instance.put_media_music(body)
            self.assertEqual(ret.code, 0, ret)
            self.assertNotEqual(ret.data, None, ret)
            if data['operation'] == 'start':
                time.sleep(3)


if __name__ == '__main__':
    unittest.main()
