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


class VisionsGetRequest(object):
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
        'option': 'str',
        'type': 'str'
    }

    attribute_map = {
        'option': 'option',
        'type': 'type'
    }

    def __init__(self, option=None, type=None):  # noqa: E501
        """VisionsGetRequest - a model defined in Swagger"""  # noqa: E501

        self._option = None
        self._type = None
        self.discriminator = None

        self.option = option
        self.type = type

    @property
    def option(self):
        """Gets the option of this VisionsGetRequest.  # noqa: E501

        模型类型。 可选值为 'face', 'hand', 'object'  # noqa: E501

        :return: The option of this VisionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this VisionsGetRequest.

        模型类型。 可选值为 'face', 'hand', 'object'  # noqa: E501

        :param option: The option of this VisionsGetRequest.  # noqa: E501
        :type: str
        """
        if option is None:
            raise ValueError("Invalid value for `option`, must not be `None`")  # noqa: E501
        allowed_values = ["face", "hand", "object"]  # noqa: E501
        if option not in allowed_values:
            raise ValueError(
                "Invalid value for `option` ({0}), must be one of {1}"  # noqa: E501
                .format(option, allowed_values)
            )

        self._option = option

    @property
    def type(self):
        """Gets the type of this VisionsGetRequest.  # noqa: E501

        任务。当模型类型为'face' 时, 可选值为 'age_analysis', 'gender_analysis', 'expression_analysis', 'quantity', 'recognition', 'tracking'。当模型类型为 'hand' 时, 可选值为 'quantity'。 当模型类型为 'object'时, 可选值为'recognition'  # noqa: E501

        :return: The type of this VisionsGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VisionsGetRequest.

        任务。当模型类型为'face' 时, 可选值为 'age_analysis', 'gender_analysis', 'expression_analysis', 'quantity', 'recognition', 'tracking'。当模型类型为 'hand' 时, 可选值为 'quantity'。 当模型类型为 'object'时, 可选值为'recognition'  # noqa: E501

        :param type: The type of this VisionsGetRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["age_analysis", "gender_analysis", "expression_analysis", "quantity", "recognition", "tracking"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(VisionsGetRequest, dict):
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
        if not isinstance(other, VisionsGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
