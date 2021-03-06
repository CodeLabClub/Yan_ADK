# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_sensors_environment_value import SubscriptionSensorsEnvironmentValue  # noqa: F401,E501
from openadk import util


class SubscriptionSensorsEnvironmentValueResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code=None, data=None, msg=None):  # noqa: E501
        """SubscriptionSensorsEnvironmentValueResponse - a model defined in Swagger

        :param code: The code of this SubscriptionSensorsEnvironmentValueResponse.  # noqa: E501
        :type code: int
        :param data: The data of this SubscriptionSensorsEnvironmentValueResponse.  # noqa: E501
        :type data: SubscriptionSensorsEnvironmentValue
        :param msg: The msg of this SubscriptionSensorsEnvironmentValueResponse.  # noqa: E501
        :type msg: str
        """
        self.swagger_types = {
            'code': int,
            'data': SubscriptionSensorsEnvironmentValue,
            'msg': str
        }

        self.attribute_map = {
            'code': 'code',
            'data': 'data',
            'msg': 'msg'
        }

        self._code = code
        self._data = data
        self._msg = msg

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionSensorsEnvironmentValueResponse of this SubscriptionSensorsEnvironmentValueResponse.  # noqa: E501
        :rtype: SubscriptionSensorsEnvironmentValueResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this SubscriptionSensorsEnvironmentValueResponse.

        Return code. 0 means success.  # noqa: E501

        :return: The code of this SubscriptionSensorsEnvironmentValueResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SubscriptionSensorsEnvironmentValueResponse.

        Return code. 0 means success.  # noqa: E501

        :param code: The code of this SubscriptionSensorsEnvironmentValueResponse.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def data(self):
        """Gets the data of this SubscriptionSensorsEnvironmentValueResponse.


        :return: The data of this SubscriptionSensorsEnvironmentValueResponse.
        :rtype: SubscriptionSensorsEnvironmentValue
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SubscriptionSensorsEnvironmentValueResponse.


        :param data: The data of this SubscriptionSensorsEnvironmentValueResponse.
        :type data: SubscriptionSensorsEnvironmentValue
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def msg(self):
        """Gets the msg of this SubscriptionSensorsEnvironmentValueResponse.

        Return code's details.  # noqa: E501

        :return: The msg of this SubscriptionSensorsEnvironmentValueResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SubscriptionSensorsEnvironmentValueResponse.

        Return code's details.  # noqa: E501

        :param msg: The msg of this SubscriptionSensorsEnvironmentValueResponse.
        :type msg: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg
