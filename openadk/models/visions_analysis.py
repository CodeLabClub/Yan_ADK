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

from openadk.models.visions_age import VisionsAge  # noqa: F401,E501
from openadk.models.visions_expression import VisionsExpression  # noqa: F401,E501
from openadk.models.visions_gender import VisionsGender  # noqa: F401,E501


class VisionsAnalysis(object):
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
        'age': 'VisionsAge',
        'gender': 'VisionsGender',
        'expression': 'VisionsExpression'
    }

    attribute_map = {
        'age': 'age',
        'gender': 'gender',
        'expression': 'expression'
    }

    def __init__(self, age=None, gender=None, expression=None):  # noqa: E501
        """VisionsAnalysis - a model defined in Swagger"""  # noqa: E501

        self._age = None
        self._gender = None
        self._expression = None
        self.discriminator = None

        if age is not None:
            self.age = age
        if gender is not None:
            self.gender = gender
        if expression is not None:
            self.expression = expression

    @property
    def age(self):
        """Gets the age of this VisionsAnalysis.  # noqa: E501


        :return: The age of this VisionsAnalysis.  # noqa: E501
        :rtype: VisionsAge
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this VisionsAnalysis.


        :param age: The age of this VisionsAnalysis.  # noqa: E501
        :type: VisionsAge
        """

        self._age = age

    @property
    def gender(self):
        """Gets the gender of this VisionsAnalysis.  # noqa: E501


        :return: The gender of this VisionsAnalysis.  # noqa: E501
        :rtype: VisionsGender
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this VisionsAnalysis.


        :param gender: The gender of this VisionsAnalysis.  # noqa: E501
        :type: VisionsGender
        """

        self._gender = gender

    @property
    def expression(self):
        """Gets the expression of this VisionsAnalysis.  # noqa: E501


        :return: The expression of this VisionsAnalysis.  # noqa: E501
        :rtype: VisionsExpression
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this VisionsAnalysis.


        :param expression: The expression of this VisionsAnalysis.  # noqa: E501
        :type: VisionsExpression
        """

        self._expression = expression

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
        if issubclass(VisionsAnalysis, dict):
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
        if not isinstance(other, VisionsAnalysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
