# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_sensors_touch_info import SubscriptionSensorsTouchInfo  # noqa: F401,E501
from openadk import util


class SubscriptionSensorsTouchValue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, touch=None):  # noqa: E501
        """SubscriptionSensorsTouchValue - a model defined in Swagger

        :param touch: The touch of this SubscriptionSensorsTouchValue.  # noqa: E501
        :type touch: List[SubscriptionSensorsTouchInfo]
        """
        self.swagger_types = {
            'touch': List[SubscriptionSensorsTouchInfo]
        }

        self.attribute_map = {
            'touch': 'touch'
        }

        self._touch = touch

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionSensorsTouchValue of this SubscriptionSensorsTouchValue.  # noqa: E501
        :rtype: SubscriptionSensorsTouchValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def touch(self):
        """Gets the touch of this SubscriptionSensorsTouchValue.


        :return: The touch of this SubscriptionSensorsTouchValue.
        :rtype: List[SubscriptionSensorsTouchInfo]
        """
        return self._touch

    @touch.setter
    def touch(self, touch):
        """Sets the touch of this SubscriptionSensorsTouchValue.


        :param touch: The touch of this SubscriptionSensorsTouchValue.
        :type touch: List[SubscriptionSensorsTouchInfo]
        """
        if touch is None:
            raise ValueError("Invalid value for `touch`, must not be `None`")  # noqa: E501

        self._touch = touch