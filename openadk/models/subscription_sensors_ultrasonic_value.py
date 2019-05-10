# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_sensors_ultrasonic_info import SubscriptionSensorsUltrasonicInfo  # noqa: F401,E501
from openadk import util


class SubscriptionSensorsUltrasonicValue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ultrasonic=None):  # noqa: E501
        """SubscriptionSensorsUltrasonicValue - a model defined in Swagger

        :param ultrasonic: The ultrasonic of this SubscriptionSensorsUltrasonicValue.  # noqa: E501
        :type ultrasonic: List[SubscriptionSensorsUltrasonicInfo]
        """
        self.swagger_types = {
            'ultrasonic': List[SubscriptionSensorsUltrasonicInfo]
        }

        self.attribute_map = {
            'ultrasonic': 'ultrasonic'
        }

        self._ultrasonic = ultrasonic

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionSensorsUltrasonicValue of this SubscriptionSensorsUltrasonicValue.  # noqa: E501
        :rtype: SubscriptionSensorsUltrasonicValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ultrasonic(self):
        """Gets the ultrasonic of this SubscriptionSensorsUltrasonicValue.


        :return: The ultrasonic of this SubscriptionSensorsUltrasonicValue.
        :rtype: List[SubscriptionSensorsUltrasonicInfo]
        """
        return self._ultrasonic

    @ultrasonic.setter
    def ultrasonic(self, ultrasonic):
        """Sets the ultrasonic of this SubscriptionSensorsUltrasonicValue.


        :param ultrasonic: The ultrasonic of this SubscriptionSensorsUltrasonicValue.
        :type ultrasonic: List[SubscriptionSensorsUltrasonicInfo]
        """
        if ultrasonic is None:
            raise ValueError("Invalid value for `ultrasonic`, must not be `None`")  # noqa: E501

        self._ultrasonic = ultrasonic