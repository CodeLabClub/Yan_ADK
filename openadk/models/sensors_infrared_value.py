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

from openadk.models.sensors_common_info import SensorsCommonInfo  # noqa: F401,E501


class SensorsInfraredValue(object):
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
        'infrared': 'list[SensorsCommonInfo]'
    }

    attribute_map = {
        'infrared': 'infrared'
    }

    def __init__(self, infrared=None):  # noqa: E501
        """SensorsInfraredValue - a model defined in Swagger"""  # noqa: E501

        self._infrared = None
        self.discriminator = None

        self.infrared = infrared

    @property
    def infrared(self):
        """Gets the infrared of this SensorsInfraredValue.  # noqa: E501


        :return: The infrared of this SensorsInfraredValue.  # noqa: E501
        :rtype: list[SensorsCommonInfo]
        """
        return self._infrared

    @infrared.setter
    def infrared(self, infrared):
        """Sets the infrared of this SensorsInfraredValue.


        :param infrared: The infrared of this SensorsInfraredValue.  # noqa: E501
        :type: list[SensorsCommonInfo]
        """
        if infrared is None:
            raise ValueError("Invalid value for `infrared`, must not be `None`")  # noqa: E501

        self._infrared = infrared

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
        if issubclass(SensorsInfraredValue, dict):
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
        if not isinstance(other, SensorsInfraredValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
