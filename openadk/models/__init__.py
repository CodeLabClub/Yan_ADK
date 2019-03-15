# coding: utf-8

# flake8: noqa
"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from openadk.models.common_response import CommonResponse
from openadk.models.devices_battery import DevicesBattery
from openadk.models.devices_battery_response import DevicesBatteryResponse
from openadk.models.devices_fall_management import DevicesFallManagement
from openadk.models.devices_fall_management_response import DevicesFallManagementResponse
from openadk.models.devices_led import DevicesLED
from openadk.models.devices_led_response import DevicesLEDResponse
from openadk.models.devices_language import DevicesLanguage
from openadk.models.devices_language_response import DevicesLanguageResponse
from openadk.models.devices_versions import DevicesVersions
from openadk.models.devices_versions_response import DevicesVersionsResponse
from openadk.models.devices_volume import DevicesVolume
from openadk.models.devices_volume_response import DevicesVolumeResponse
from openadk.models.media_music_list import MediaMusicList
from openadk.models.media_music_list_response import MediaMusicListResponse
from openadk.models.media_music_operation import MediaMusicOperation
from openadk.models.media_music_status import MediaMusicStatus
from openadk.models.media_music_status_response import MediaMusicStatusResponse
from openadk.models.motions_info import MotionsInfo
from openadk.models.motions_list import MotionsList
from openadk.models.motions_list_response import MotionsListResponse
from openadk.models.motions_operation import MotionsOperation
from openadk.models.motions_parameter import MotionsParameter
from openadk.models.motions_status import MotionsStatus
from openadk.models.motions_status_response import MotionsStatusResponse
from openadk.models.name import Name
from openadk.models.run_status import RunStatus
from openadk.models.runtime_response import RuntimeResponse
from openadk.models.sensors_common_info import SensorsCommonInfo
from openadk.models.sensors_environment_info import SensorsEnvironmentInfo
from openadk.models.sensors_environment_value import SensorsEnvironmentValue
from openadk.models.sensors_environment_value_response import SensorsEnvironmentValueResponse
from openadk.models.sensors_gyro_info import SensorsGyroInfo
from openadk.models.sensors_gyro_value import SensorsGyroValue
from openadk.models.sensors_gyro_value_response import SensorsGyroValueResponse
from openadk.models.sensors_info import SensorsInfo
from openadk.models.sensors_infrared_value import SensorsInfraredValue
from openadk.models.sensors_infrared_value_response import SensorsInfraredValueResponse
from openadk.models.sensors_list import SensorsList
from openadk.models.sensors_list_response import SensorsListResponse
from openadk.models.sensors_operation_request import SensorsOperationRequest
from openadk.models.sensors_parameter import SensorsParameter
from openadk.models.sensors_pressure_value import SensorsPressureValue
from openadk.models.sensors_pressure_value_response import SensorsPressureValueResponse
from openadk.models.sensors_touch_value import SensorsTouchValue
from openadk.models.sensors_touch_value_response import SensorsTouchValueResponse
from openadk.models.sensors_ultrasonic_value import SensorsUltrasonicValue
from openadk.models.sensors_ultrasonic_value_response import SensorsUltrasonicValueResponse
from openadk.models.servos_angles import ServosAngles
from openadk.models.servos_angles_request import ServosAnglesRequest
from openadk.models.servos_angles_response import ServosAnglesResponse
from openadk.models.servos_list import ServosList
from openadk.models.servos_mode import ServosMode
from openadk.models.servos_mode_request import ServosModeRequest
from openadk.models.servos_mode_response import ServosModeResponse
from openadk.models.servos_result import ServosResult
from openadk.models.servos_result_response import ServosResultResponse
from openadk.models.subscriptions_motions import SubscriptionsMotions
from openadk.models.subscriptions_sensors import SubscriptionsSensors
from openadk.models.subscriptions_stream import SubscriptionsStream
from openadk.models.subscriptions_visions import SubscriptionsVisions
from openadk.models.subscriptions_voice import SubscriptionsVoice
from openadk.models.total_time import TotalTime
from openadk.models.visions_age import VisionsAge
from openadk.models.visions_analysis import VisionsAnalysis
from openadk.models.visions_delete_tags import VisionsDeleteTags
from openadk.models.visions_expression import VisionsExpression
from openadk.models.visions_gender import VisionsGender
from openadk.models.visions_get_response import VisionsGetResponse
from openadk.models.visions_photo import VisionsPhoto
from openadk.models.visions_photo_list_response import VisionsPhotoListResponse
from openadk.models.visions_put import VisionsPut
from openadk.models.visions_put_response import VisionsPutResponse
from openadk.models.visions_put_tags import VisionsPutTags
from openadk.models.visions_quantity import VisionsQuantity
from openadk.models.visions_results import VisionsResults
from openadk.models.visions_sample_delete_request import VisionsSampleDeleteRequest
from openadk.models.visions_stream import VisionsStream
from openadk.models.visions_tags_response import VisionsTagsResponse
from openadk.models.visions_task import VisionsTask
from openadk.models.voice_asr_option import VoiceAsrOption
from openadk.models.voice_response import VoiceResponse
from openadk.models.voice_status_response import VoiceStatusResponse
from openadk.models.voice_tts_str import VoiceTTSStr
