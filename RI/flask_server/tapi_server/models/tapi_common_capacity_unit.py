# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiCommonCapacityUnit(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    TB = "TB"
    TBPS = "TBPS"
    GB = "GB"
    GBPS = "GBPS"
    MB = "MB"
    MBPS = "MBPS"
    KB = "KB"
    KBPS = "KBPS"
    GHZ = "GHz"
    MHZ = "MHz"

    def __init__(self):  # noqa: E501
        """TapiCommonCapacityUnit - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonCapacityUnit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.CapacityUnit of this TapiCommonCapacityUnit.  # noqa: E501
        :rtype: TapiCommonCapacityUnit
        """
        return util.deserialize_model(dikt, cls)