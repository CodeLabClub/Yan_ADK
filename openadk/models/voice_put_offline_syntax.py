# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openadk.models.voice_offline_slot import VoiceOfflineSlot  # noqa: F401,E501
from openadk.models.voice_offline_syntax_rule import VoiceOfflineSyntaxRule  # noqa: F401,E501


class VoicePutOfflineSyntax(object):
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
        'grammar': 'str',
        'slot': 'list[VoiceOfflineSlot]',
        'start': 'str',
        'startinfo': 'str',
        'rule': 'list[VoiceOfflineSyntaxRule]'
    }

    attribute_map = {
        'grammar': 'grammar',
        'slot': 'slot',
        'start': 'start',
        'startinfo': 'startinfo',
        'rule': 'rule'
    }

    def __init__(self, grammar=None, slot=None, start=None, startinfo=None, rule=None):  # noqa: E501
        """VoicePutOfflineSyntax - a model defined in Swagger"""  # noqa: E501

        self._grammar = None
        self._slot = None
        self._start = None
        self._startinfo = None
        self._rule = None
        self.discriminator = None

        self.grammar = grammar
        self.slot = slot
        self.start = start
        self.startinfo = startinfo
        self.rule = rule

    @property
    def grammar(self):
        """Gets the grammar of this VoicePutOfflineSyntax.  # noqa: E501

         Define offline grammar. Only support alphabets.   # noqa: E501

        :return: The grammar of this VoicePutOfflineSyntax.  # noqa: E501
        :rtype: str
        """
        return self._grammar

    @grammar.setter
    def grammar(self, grammar):
        """Sets the grammar of this VoicePutOfflineSyntax.

         Define offline grammar. Only support alphabets.   # noqa: E501

        :param grammar: The grammar of this VoicePutOfflineSyntax.  # noqa: E501
        :type: str
        """
        if grammar is None:
            raise ValueError("Invalid value for `grammar`, must not be `None`")  # noqa: E501

        self._grammar = grammar

    @property
    def slot(self):
        """Gets the slot of this VoicePutOfflineSyntax.  # noqa: E501

         Declare the slot, the content can support alphabets and numbers. All operators and keywords are half-width characters. The full-width characters cannot supported.   # noqa: E501

        :return: The slot of this VoicePutOfflineSyntax.  # noqa: E501
        :rtype: list[VoiceOfflineSlot]
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this VoicePutOfflineSyntax.

         Declare the slot, the content can support alphabets and numbers. All operators and keywords are half-width characters. The full-width characters cannot supported.   # noqa: E501

        :param slot: The slot of this VoicePutOfflineSyntax.  # noqa: E501
        :type: list[VoiceOfflineSlot]
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

    @property
    def start(self):
        """Gets the start of this VoicePutOfflineSyntax.  # noqa: E501

         Declare the slot, the content can support alphabets and numbers. All operators and keywords are half-width characters. The full-width characters cannot supported.   # noqa: E501

        :return: The start of this VoicePutOfflineSyntax.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VoicePutOfflineSyntax.

         Declare the slot, the content can support alphabets and numbers. All operators and keywords are half-width characters. The full-width characters cannot supported.   # noqa: E501

        :param start: The start of this VoicePutOfflineSyntax.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def startinfo(self):
        """Gets the startinfo of this VoicePutOfflineSyntax.  # noqa: E501

         Define start rule details.   # noqa: E501

        :return: The startinfo of this VoicePutOfflineSyntax.  # noqa: E501
        :rtype: str
        """
        return self._startinfo

    @startinfo.setter
    def startinfo(self, startinfo):
        """Sets the startinfo of this VoicePutOfflineSyntax.

         Define start rule details.   # noqa: E501

        :param startinfo: The startinfo of this VoicePutOfflineSyntax.  # noqa: E501
        :type: str
        """
        if startinfo is None:
            raise ValueError("Invalid value for `startinfo`, must not be `None`")  # noqa: E501

        self._startinfo = startinfo

    @property
    def rule(self):
        """Gets the rule of this VoicePutOfflineSyntax.  # noqa: E501

         Define all offline rules' name and value. The rule's value should not be NULL.   # noqa: E501

        :return: The rule of this VoicePutOfflineSyntax.  # noqa: E501
        :rtype: list[VoiceOfflineSyntaxRule]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this VoicePutOfflineSyntax.

         Define all offline rules' name and value. The rule's value should not be NULL.   # noqa: E501

        :param rule: The rule of this VoicePutOfflineSyntax.  # noqa: E501
        :type: list[VoiceOfflineSyntaxRule]
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

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
        if issubclass(VoicePutOfflineSyntax, dict):
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
        if not isinstance(other, VoicePutOfflineSyntax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
