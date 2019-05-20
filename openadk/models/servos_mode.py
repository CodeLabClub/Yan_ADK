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


class ServosMode(object):
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
        'right_shoulder_roll': 'str',
        'right_shoulder_flex': 'str',
        'right_elbow_flex': 'str',
        'left_shoulder_roll': 'str',
        'left_shoulder_flex': 'str',
        'left_elbow_flex': 'str',
        'right_hip_lr': 'str',
        'right_hip_fb': 'str',
        'right_knee_flex': 'str',
        'right_ankle_fb': 'str',
        'right_ankle_ud': 'str',
        'left_hip_lr': 'str',
        'left_hip_fb': 'str',
        'left_knee_flex': 'str',
        'left_ankle_fb': 'str',
        'left_ankle_ud': 'str',
        'neck_lr': 'str'
    }

    attribute_map = {
        'right_shoulder_roll': 'RightShoulderRoll',
        'right_shoulder_flex': 'RightShoulderFlex',
        'right_elbow_flex': 'RightElbowFlex',
        'left_shoulder_roll': 'LeftShoulderRoll',
        'left_shoulder_flex': 'LeftShoulderFlex',
        'left_elbow_flex': 'LeftElbowFlex',
        'right_hip_lr': 'RightHipLR',
        'right_hip_fb': 'RightHipFB',
        'right_knee_flex': 'RightKneeFlex',
        'right_ankle_fb': 'RightAnkleFB',
        'right_ankle_ud': 'RightAnkleUD',
        'left_hip_lr': 'LeftHipLR',
        'left_hip_fb': 'LeftHipFB',
        'left_knee_flex': 'LeftKneeFlex',
        'left_ankle_fb': 'LeftAnkleFB',
        'left_ankle_ud': 'LeftAnkleUD',
        'neck_lr': 'NeckLR'
    }

    def __init__(self, right_shoulder_roll=None, right_shoulder_flex=None, right_elbow_flex=None, left_shoulder_roll=None, left_shoulder_flex=None, left_elbow_flex=None, right_hip_lr=None, right_hip_fb=None, right_knee_flex=None, right_ankle_fb=None, right_ankle_ud=None, left_hip_lr=None, left_hip_fb=None, left_knee_flex=None, left_ankle_fb=None, left_ankle_ud=None, neck_lr=None):  # noqa: E501
        """ServosMode - a model defined in Swagger"""  # noqa: E501

        self._right_shoulder_roll = None
        self._right_shoulder_flex = None
        self._right_elbow_flex = None
        self._left_shoulder_roll = None
        self._left_shoulder_flex = None
        self._left_elbow_flex = None
        self._right_hip_lr = None
        self._right_hip_fb = None
        self._right_knee_flex = None
        self._right_ankle_fb = None
        self._right_ankle_ud = None
        self._left_hip_lr = None
        self._left_hip_fb = None
        self._left_knee_flex = None
        self._left_ankle_fb = None
        self._left_ankle_ud = None
        self._neck_lr = None
        self.discriminator = None

        if right_shoulder_roll is not None:
            self.right_shoulder_roll = right_shoulder_roll
        if right_shoulder_flex is not None:
            self.right_shoulder_flex = right_shoulder_flex
        if right_elbow_flex is not None:
            self.right_elbow_flex = right_elbow_flex
        if left_shoulder_roll is not None:
            self.left_shoulder_roll = left_shoulder_roll
        if left_shoulder_flex is not None:
            self.left_shoulder_flex = left_shoulder_flex
        if left_elbow_flex is not None:
            self.left_elbow_flex = left_elbow_flex
        if right_hip_lr is not None:
            self.right_hip_lr = right_hip_lr
        if right_hip_fb is not None:
            self.right_hip_fb = right_hip_fb
        if right_knee_flex is not None:
            self.right_knee_flex = right_knee_flex
        if right_ankle_fb is not None:
            self.right_ankle_fb = right_ankle_fb
        if right_ankle_ud is not None:
            self.right_ankle_ud = right_ankle_ud
        if left_hip_lr is not None:
            self.left_hip_lr = left_hip_lr
        if left_hip_fb is not None:
            self.left_hip_fb = left_hip_fb
        if left_knee_flex is not None:
            self.left_knee_flex = left_knee_flex
        if left_ankle_fb is not None:
            self.left_ankle_fb = left_ankle_fb
        if left_ankle_ud is not None:
            self.left_ankle_ud = left_ankle_ud
        if neck_lr is not None:
            self.neck_lr = neck_lr

    @property
    def right_shoulder_roll(self):
        """Gets the right_shoulder_roll of this ServosMode.  # noqa: E501

        Servo 1  # noqa: E501

        :return: The right_shoulder_roll of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_shoulder_roll

    @right_shoulder_roll.setter
    def right_shoulder_roll(self, right_shoulder_roll):
        """Sets the right_shoulder_roll of this ServosMode.

        Servo 1  # noqa: E501

        :param right_shoulder_roll: The right_shoulder_roll of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_shoulder_roll not in allowed_values:
            raise ValueError(
                "Invalid value for `right_shoulder_roll` ({0}), must be one of {1}"  # noqa: E501
                .format(right_shoulder_roll, allowed_values)
            )

        self._right_shoulder_roll = right_shoulder_roll

    @property
    def right_shoulder_flex(self):
        """Gets the right_shoulder_flex of this ServosMode.  # noqa: E501

        Servo 2  # noqa: E501

        :return: The right_shoulder_flex of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_shoulder_flex

    @right_shoulder_flex.setter
    def right_shoulder_flex(self, right_shoulder_flex):
        """Sets the right_shoulder_flex of this ServosMode.

        Servo 2  # noqa: E501

        :param right_shoulder_flex: The right_shoulder_flex of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_shoulder_flex not in allowed_values:
            raise ValueError(
                "Invalid value for `right_shoulder_flex` ({0}), must be one of {1}"  # noqa: E501
                .format(right_shoulder_flex, allowed_values)
            )

        self._right_shoulder_flex = right_shoulder_flex

    @property
    def right_elbow_flex(self):
        """Gets the right_elbow_flex of this ServosMode.  # noqa: E501

        Servo 3  # noqa: E501

        :return: The right_elbow_flex of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_elbow_flex

    @right_elbow_flex.setter
    def right_elbow_flex(self, right_elbow_flex):
        """Sets the right_elbow_flex of this ServosMode.

        Servo 3  # noqa: E501

        :param right_elbow_flex: The right_elbow_flex of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_elbow_flex not in allowed_values:
            raise ValueError(
                "Invalid value for `right_elbow_flex` ({0}), must be one of {1}"  # noqa: E501
                .format(right_elbow_flex, allowed_values)
            )

        self._right_elbow_flex = right_elbow_flex

    @property
    def left_shoulder_roll(self):
        """Gets the left_shoulder_roll of this ServosMode.  # noqa: E501

        Servo 4  # noqa: E501

        :return: The left_shoulder_roll of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_shoulder_roll

    @left_shoulder_roll.setter
    def left_shoulder_roll(self, left_shoulder_roll):
        """Sets the left_shoulder_roll of this ServosMode.

        Servo 4  # noqa: E501

        :param left_shoulder_roll: The left_shoulder_roll of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_shoulder_roll not in allowed_values:
            raise ValueError(
                "Invalid value for `left_shoulder_roll` ({0}), must be one of {1}"  # noqa: E501
                .format(left_shoulder_roll, allowed_values)
            )

        self._left_shoulder_roll = left_shoulder_roll

    @property
    def left_shoulder_flex(self):
        """Gets the left_shoulder_flex of this ServosMode.  # noqa: E501

        Servo 5  # noqa: E501

        :return: The left_shoulder_flex of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_shoulder_flex

    @left_shoulder_flex.setter
    def left_shoulder_flex(self, left_shoulder_flex):
        """Sets the left_shoulder_flex of this ServosMode.

        Servo 5  # noqa: E501

        :param left_shoulder_flex: The left_shoulder_flex of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_shoulder_flex not in allowed_values:
            raise ValueError(
                "Invalid value for `left_shoulder_flex` ({0}), must be one of {1}"  # noqa: E501
                .format(left_shoulder_flex, allowed_values)
            )

        self._left_shoulder_flex = left_shoulder_flex

    @property
    def left_elbow_flex(self):
        """Gets the left_elbow_flex of this ServosMode.  # noqa: E501

        Servo 6  # noqa: E501

        :return: The left_elbow_flex of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_elbow_flex

    @left_elbow_flex.setter
    def left_elbow_flex(self, left_elbow_flex):
        """Sets the left_elbow_flex of this ServosMode.

        Servo 6  # noqa: E501

        :param left_elbow_flex: The left_elbow_flex of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_elbow_flex not in allowed_values:
            raise ValueError(
                "Invalid value for `left_elbow_flex` ({0}), must be one of {1}"  # noqa: E501
                .format(left_elbow_flex, allowed_values)
            )

        self._left_elbow_flex = left_elbow_flex

    @property
    def right_hip_lr(self):
        """Gets the right_hip_lr of this ServosMode.  # noqa: E501

        Servo 7  # noqa: E501

        :return: The right_hip_lr of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_hip_lr

    @right_hip_lr.setter
    def right_hip_lr(self, right_hip_lr):
        """Sets the right_hip_lr of this ServosMode.

        Servo 7  # noqa: E501

        :param right_hip_lr: The right_hip_lr of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_hip_lr not in allowed_values:
            raise ValueError(
                "Invalid value for `right_hip_lr` ({0}), must be one of {1}"  # noqa: E501
                .format(right_hip_lr, allowed_values)
            )

        self._right_hip_lr = right_hip_lr

    @property
    def right_hip_fb(self):
        """Gets the right_hip_fb of this ServosMode.  # noqa: E501

        Servo 8  # noqa: E501

        :return: The right_hip_fb of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_hip_fb

    @right_hip_fb.setter
    def right_hip_fb(self, right_hip_fb):
        """Sets the right_hip_fb of this ServosMode.

        Servo 8  # noqa: E501

        :param right_hip_fb: The right_hip_fb of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_hip_fb not in allowed_values:
            raise ValueError(
                "Invalid value for `right_hip_fb` ({0}), must be one of {1}"  # noqa: E501
                .format(right_hip_fb, allowed_values)
            )

        self._right_hip_fb = right_hip_fb

    @property
    def right_knee_flex(self):
        """Gets the right_knee_flex of this ServosMode.  # noqa: E501

        Servo 9  # noqa: E501

        :return: The right_knee_flex of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_knee_flex

    @right_knee_flex.setter
    def right_knee_flex(self, right_knee_flex):
        """Sets the right_knee_flex of this ServosMode.

        Servo 9  # noqa: E501

        :param right_knee_flex: The right_knee_flex of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_knee_flex not in allowed_values:
            raise ValueError(
                "Invalid value for `right_knee_flex` ({0}), must be one of {1}"  # noqa: E501
                .format(right_knee_flex, allowed_values)
            )

        self._right_knee_flex = right_knee_flex

    @property
    def right_ankle_fb(self):
        """Gets the right_ankle_fb of this ServosMode.  # noqa: E501

        Servo 10  # noqa: E501

        :return: The right_ankle_fb of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_ankle_fb

    @right_ankle_fb.setter
    def right_ankle_fb(self, right_ankle_fb):
        """Sets the right_ankle_fb of this ServosMode.

        Servo 10  # noqa: E501

        :param right_ankle_fb: The right_ankle_fb of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_ankle_fb not in allowed_values:
            raise ValueError(
                "Invalid value for `right_ankle_fb` ({0}), must be one of {1}"  # noqa: E501
                .format(right_ankle_fb, allowed_values)
            )

        self._right_ankle_fb = right_ankle_fb

    @property
    def right_ankle_ud(self):
        """Gets the right_ankle_ud of this ServosMode.  # noqa: E501

        Servo 11  # noqa: E501

        :return: The right_ankle_ud of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._right_ankle_ud

    @right_ankle_ud.setter
    def right_ankle_ud(self, right_ankle_ud):
        """Sets the right_ankle_ud of this ServosMode.

        Servo 11  # noqa: E501

        :param right_ankle_ud: The right_ankle_ud of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if right_ankle_ud not in allowed_values:
            raise ValueError(
                "Invalid value for `right_ankle_ud` ({0}), must be one of {1}"  # noqa: E501
                .format(right_ankle_ud, allowed_values)
            )

        self._right_ankle_ud = right_ankle_ud

    @property
    def left_hip_lr(self):
        """Gets the left_hip_lr of this ServosMode.  # noqa: E501

        Servo 12  # noqa: E501

        :return: The left_hip_lr of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_hip_lr

    @left_hip_lr.setter
    def left_hip_lr(self, left_hip_lr):
        """Sets the left_hip_lr of this ServosMode.

        Servo 12  # noqa: E501

        :param left_hip_lr: The left_hip_lr of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_hip_lr not in allowed_values:
            raise ValueError(
                "Invalid value for `left_hip_lr` ({0}), must be one of {1}"  # noqa: E501
                .format(left_hip_lr, allowed_values)
            )

        self._left_hip_lr = left_hip_lr

    @property
    def left_hip_fb(self):
        """Gets the left_hip_fb of this ServosMode.  # noqa: E501

        Servo 13  # noqa: E501

        :return: The left_hip_fb of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_hip_fb

    @left_hip_fb.setter
    def left_hip_fb(self, left_hip_fb):
        """Sets the left_hip_fb of this ServosMode.

        Servo 13  # noqa: E501

        :param left_hip_fb: The left_hip_fb of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_hip_fb not in allowed_values:
            raise ValueError(
                "Invalid value for `left_hip_fb` ({0}), must be one of {1}"  # noqa: E501
                .format(left_hip_fb, allowed_values)
            )

        self._left_hip_fb = left_hip_fb

    @property
    def left_knee_flex(self):
        """Gets the left_knee_flex of this ServosMode.  # noqa: E501

        Servo 14  # noqa: E501

        :return: The left_knee_flex of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_knee_flex

    @left_knee_flex.setter
    def left_knee_flex(self, left_knee_flex):
        """Sets the left_knee_flex of this ServosMode.

        Servo 14  # noqa: E501

        :param left_knee_flex: The left_knee_flex of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_knee_flex not in allowed_values:
            raise ValueError(
                "Invalid value for `left_knee_flex` ({0}), must be one of {1}"  # noqa: E501
                .format(left_knee_flex, allowed_values)
            )

        self._left_knee_flex = left_knee_flex

    @property
    def left_ankle_fb(self):
        """Gets the left_ankle_fb of this ServosMode.  # noqa: E501

        Servo 15  # noqa: E501

        :return: The left_ankle_fb of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_ankle_fb

    @left_ankle_fb.setter
    def left_ankle_fb(self, left_ankle_fb):
        """Sets the left_ankle_fb of this ServosMode.

        Servo 15  # noqa: E501

        :param left_ankle_fb: The left_ankle_fb of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_ankle_fb not in allowed_values:
            raise ValueError(
                "Invalid value for `left_ankle_fb` ({0}), must be one of {1}"  # noqa: E501
                .format(left_ankle_fb, allowed_values)
            )

        self._left_ankle_fb = left_ankle_fb

    @property
    def left_ankle_ud(self):
        """Gets the left_ankle_ud of this ServosMode.  # noqa: E501

        Servo 16  # noqa: E501

        :return: The left_ankle_ud of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._left_ankle_ud

    @left_ankle_ud.setter
    def left_ankle_ud(self, left_ankle_ud):
        """Sets the left_ankle_ud of this ServosMode.

        Servo 16  # noqa: E501

        :param left_ankle_ud: The left_ankle_ud of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if left_ankle_ud not in allowed_values:
            raise ValueError(
                "Invalid value for `left_ankle_ud` ({0}), must be one of {1}"  # noqa: E501
                .format(left_ankle_ud, allowed_values)
            )

        self._left_ankle_ud = left_ankle_ud

    @property
    def neck_lr(self):
        """Gets the neck_lr of this ServosMode.  # noqa: E501

        Servo 17  # noqa: E501

        :return: The neck_lr of this ServosMode.  # noqa: E501
        :rtype: str
        """
        return self._neck_lr

    @neck_lr.setter
    def neck_lr(self, neck_lr):
        """Sets the neck_lr of this ServosMode.

        Servo 17  # noqa: E501

        :param neck_lr: The neck_lr of this ServosMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["work", "program", "unknown", "nonsupport"]  # noqa: E501
        if neck_lr not in allowed_values:
            raise ValueError(
                "Invalid value for `neck_lr` ({0}), must be one of {1}"  # noqa: E501
                .format(neck_lr, allowed_values)
            )

        self._neck_lr = neck_lr

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
        if issubclass(ServosMode, dict):
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
        if not isinstance(other, ServosMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
