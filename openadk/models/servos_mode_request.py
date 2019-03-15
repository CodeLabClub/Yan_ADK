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

from openadk.models.servos_list import ServosList  # noqa: F401,E501


class ServosModeRequest(object):
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
        'mode': 'str',
        'servos': 'list[ServosList]'
    }

    attribute_map = {
        'mode': 'mode',
        'servos': 'servos'
    }

    def __init__(self, mode=None, servos=None):  # noqa: E501
        """ServosModeRequest - a model defined in Swagger"""  # noqa: E501

        self._mode = None
        self._servos = None
        self.discriminator = None

        self.mode = mode
        self.servos = servos

    @property
    def mode(self):
        """Gets the mode of this ServosModeRequest.  # noqa: E501

        模式取值：work（工作模式）和program（编程模式）  # noqa: E501

        :return: The mode of this ServosModeRequest.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ServosModeRequest.

        模式取值：work（工作模式）和program（编程模式）  # noqa: E501

        :param mode: The mode of this ServosModeRequest.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["work", "program"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def servos(self):
        """Gets the servos of this ServosModeRequest.  # noqa: E501


        :return: The servos of this ServosModeRequest.  # noqa: E501
        :rtype: list[ServosList]
        """
        return self._servos

    @servos.setter
    def servos(self, servos):
        """Sets the servos of this ServosModeRequest.


        :param servos: The servos of this ServosModeRequest.  # noqa: E501
        :type: list[ServosList]
        """
        if servos is None:
            raise ValueError("Invalid value for `servos`, must not be `None`")  # noqa: E501

        self._servos = servos

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
        if issubclass(ServosModeRequest, dict):
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
        if not isinstance(other, ServosModeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
