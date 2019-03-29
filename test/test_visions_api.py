# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import openadk
from openadk import Name, VisionsDeleteTags, VisionsGetRequest
from openadk.api.visions_api import VisionsApi  # noqa: E501
from openadk.rest import ApiException
from pprint import pprint


class TestVisionsApi(unittest.TestCase):
    """VisionsApi unit test stubs"""

    def setUp(self):
        self.configuration = openadk.Configuration()
        self.configuration.host = 'http://10.10.61.184:9090/v1'
        self.api_instance = openadk.api.visions_api.VisionsApi(openadk.ApiClient(self.configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_vision_photo(self):
        """Test case for delete_vision_photo

        删除指定照片  # noqa: E501
        """
        try:
            # ??????
            test_file_list = ['ssss', 'hello', '123123', '@!@#!@#']
            for name in test_file_list:
                body = Name(name=name)
                api_response = self.api_instance.delete_vision_photo(body)
                print(api_response)
                self.assertEqual(20002, api_response.code)
                self.assertEqual('Resource not exist.', api_response.msg)

        except ApiException as e:
            print("Exception when calling VisionsApi->delete_vision_photo_samples: %s\n" % e)

    def test_delete_vision_photo_samples(self):
        """Test case for delete_vision_photo_samples

        删除上传的样本  # noqa: E501
        """
        test_file_list = ['ssss', 'hello', '123123', '@!@#!@#']
        for name in test_file_list:
            body = openadk.Name(name=name)  # Name | ???? (optional)
            try:
                # ???????
                api_response = self.api_instance.delete_vision_photo_samples(body=body)
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->delete_vision_photo_samples: %s\n" % e)

    def test_delete_visions_streams(self):
        """Test case for delete_visions_streams

        关闭摄像头的视频流  # noqa: E501
        """
        body = openadk.VisionsStream()  # VisionsStream |  (optional)
        try:
            # ?????????
            api_response = self.api_instance.delete_visions_streams(body=body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->delete_visions_streams: %s\n" % e)

    def test_delete_visions_tags(self):
        """Test case for delete_visions_tags

        删除指定样本标签  # noqa: E501
        """
        test_tags_name = ['sss', '#$@#', '//1923\?']
        for tags in test_tags_name:
            body = VisionsDeleteTags(tags=tags)  # VisionsDeleteTags | ???? (optional)

            try:
                # ????????
                api_response = self.api_instance.delete_visions_tags(body=body)
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->delete_visions_tags: %s\n" % e)

    def test_get_photo_samples(self):
        """Test case for get_photo_samples

        获取上传样本列表  # noqa: E501
        """
        try:
            # ????????
            api_response = self.api_instance.get_photo_samples()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->get_photo_samples: %s\n" % e)

    def test_get_vision(self):
        """Test case for get_vision

        获取任务結果  # noqa: E501
        """
        option_list = ['face', 'hand', 'object']
        face_option_list = ['age_analysis', 'gender_analysis', 'expression_analysis', 'quantity', 'tracking', 'recognition']
        hand_option_list = ['quantity']
        object_option_list = ['recognition']

            # ??????
        for face_option in face_option_list:
            try:
                api_response = self.api_instance.get_vision(option=option_list[0], type=face_option)
                print(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->get_vision: %s\n" % e)

        for hand_option in hand_option_list:
            try:
                api_response = self.api_instance.get_vision(option=option_list[1], type=hand_option)
                print(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->get_vision: %s\n" % e)

        for object_option in object_option_list:
            try:
                api_response = self.api_instance.get_vision(option=option_list[2], type=object_option)
                print(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->get_vision: %s\n" % e)

    def test_get_visions_photos(self):
        """Test case for get_visions_photos

        获取指定照片  # noqa: E501
        """
        try:
            # ??????
            api_response = self.api_instance.get_visions_photos()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->get_visions_photos: %s\n" % e)

    def test_get_visions_photos_lists(self):
        """Test case for get_visions_photos_lists

        获取拍照列表  # noqa: E501
        """
        try:
            #  ??????
            api_response = self.api_instance.get_visions_photos_lists()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->get_visions_photos_lists: %s\n" % e)

    def test_get_visions_tags(self):
        """Test case for get_visions_tags

        获取已设置标签列表  # noqa: E501
        """
        try:
            # ?????????
            api_response = self.api_instance.get_visions_tags()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->get_visions_tags: %s\n" % e)

    def test_post_vision_photo(self):
        """Test case for post_vision_photo

        拍一张照片  # noqa: E501
        """
        try:
            # ?????
            api_response = self.api_instance.post_vision_photo()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->post_vision_photo: %s\n" % e)

    def test_post_visions_streams(self):
        """Test case for post_visions_streams

        打开摄像头的视频流  # noqa: E501
        """
        pass

    def test_put_visions(self):
        """Test case for put_visions

        ???????????  # noqa: E501
        """
        try:
            # ???????????
            api_response = self.api_instance.put_visions()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->put_visions: %s\n" % e)

    def test_put_visions_photo_samples(self):
        """Test case for put_visions_photo_samples

        上传样本  # noqa: E501
        """
        try:
            # ????
            api_response = self.api_instance.put_visions_photo_samples()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->put_visions_photo_samples: %s\n" % e)

    def test_put_visions_tags(self):
        """Test case for put_visions_tags

        设置样本标签  # noqa: E501
        """
        try:
            # ??????
            api_response = self.api_instance.put_visions_tags()
            print(api_response)
        except ApiException as e:
            print("Exception when calling VisionsApi->put_visions_tags: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
