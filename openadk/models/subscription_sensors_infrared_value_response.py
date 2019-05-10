# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_sensors_infrared_value import SubscriptionSensorsInfraredValue  # noqa: F401,E501
from openadk import util


class SubscriptionSensorsInfraredValueResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code=None, data=None, msg=None):  # noqa: E501
        """SubscriptionSensorsInfraredValueResponse - a model defined in Swagger

        :param code: The code of this SubscriptionSensorsInfraredValueResponse.  # noqa: E501
        :type code: int
        :param data: The data of this SubscriptionSensorsInfraredValueResponse.  # noqa: E501
        :type data: SubscriptionSensorsInfraredValue
        :param msg: The msg of this SubscriptionSensorsInfraredValueResponse.  # noqa: E501
        :type msg: str
        """
        self.swagger_types = {
            'code': int,
            'data': SubscriptionSensorsInfraredValue,
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
        :return: The SubscriptionSensorsInfraredValueResponse of this SubscriptionSensorsInfraredValueResponse.  # noqa: E501
        :rtype: SubscriptionSensorsInfraredValueResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this SubscriptionSensorsInfraredValueResponse.

        返回码，0表示正常  # noqa: E501

        :return: The code of this SubscriptionSensorsInfraredValueResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SubscriptionSensorsInfraredValueResponse.

        返回码，0表示正常  # noqa: E501

        :param code: The code of this SubscriptionSensorsInfraredValueResponse.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def data(self):
        """Gets the data of this SubscriptionSensorsInfraredValueResponse.


        :return: The data of this SubscriptionSensorsInfraredValueResponse.
        :rtype: SubscriptionSensorsInfraredValue
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SubscriptionSensorsInfraredValueResponse.


        :param data: The data of this SubscriptionSensorsInfraredValueResponse.
        :type data: SubscriptionSensorsInfraredValue
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def msg(self):
        """Gets the msg of this SubscriptionSensorsInfraredValueResponse.

        提示信息  # noqa: E501

        :return: The msg of this SubscriptionSensorsInfraredValueResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SubscriptionSensorsInfraredValueResponse.

        提示信息  # noqa: E501

        :param msg: The msg of this SubscriptionSensorsInfraredValueResponse.
        :type msg: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg