# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MotionsInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'music': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'music': 'music'
    }

    def __init__(self, name=None, music=None):  # noqa: E501
        """MotionsInfo - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._music = None
        self.discriminator = None

        self.name = name
        self.music = music

    @property
    def name(self):
        """Gets the name of this MotionsInfo.  # noqa: E501

        动作名称  # noqa: E501

        :return: The name of this MotionsInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MotionsInfo.

        动作名称  # noqa: E501

        :param name: The name of this MotionsInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def music(self):
        """Gets the music of this MotionsInfo.  # noqa: E501

        是否带有音乐  # noqa: E501

        :return: The music of this MotionsInfo.  # noqa: E501
        :rtype: bool
        """
        return self._music

    @music.setter
    def music(self, music):
        """Sets the music of this MotionsInfo.

        是否带有音乐  # noqa: E501

        :param music: The music of this MotionsInfo.  # noqa: E501
        :type: bool
        """
        if music is None:
            raise ValueError("Invalid value for `music`, must not be `None`")  # noqa: E501

        self._music = music

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MotionsInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MotionsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
