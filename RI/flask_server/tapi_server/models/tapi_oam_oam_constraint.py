# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_forwarding_direction import TapiCommonForwardingDirection  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server import util


class TapiOamOamConstraint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, layer_protocol_name=None, meg_level=None, direction=None):  # noqa: E501
        """TapiOamOamConstraint - a model defined in OpenAPI

        :param layer_protocol_name: The layer_protocol_name of this TapiOamOamConstraint.  # noqa: E501
        :type layer_protocol_name: TapiCommonLayerProtocolName
        :param meg_level: The meg_level of this TapiOamOamConstraint.  # noqa: E501
        :type meg_level: int
        :param direction: The direction of this TapiOamOamConstraint.  # noqa: E501
        :type direction: TapiCommonForwardingDirection
        """
        self.openapi_types = {
            'layer_protocol_name': TapiCommonLayerProtocolName,
            'meg_level': int,
            'direction': TapiCommonForwardingDirection
        }

        self.attribute_map = {
            'layer_protocol_name': 'layer-protocol-name',
            'meg_level': 'meg-level',
            'direction': 'direction'
        }

        self._layer_protocol_name = layer_protocol_name
        self._meg_level = meg_level
        self._direction = direction

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamOamConstraint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.OamConstraint of this TapiOamOamConstraint.  # noqa: E501
        :rtype: TapiOamOamConstraint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiOamOamConstraint.


        :return: The layer_protocol_name of this TapiOamOamConstraint.
        :rtype: TapiCommonLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiOamOamConstraint.


        :param layer_protocol_name: The layer_protocol_name of this TapiOamOamConstraint.
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name

    @property
    def meg_level(self):
        """Gets the meg_level of this TapiOamOamConstraint.

        none  # noqa: E501

        :return: The meg_level of this TapiOamOamConstraint.
        :rtype: int
        """
        return self._meg_level

    @meg_level.setter
    def meg_level(self, meg_level):
        """Sets the meg_level of this TapiOamOamConstraint.

        none  # noqa: E501

        :param meg_level: The meg_level of this TapiOamOamConstraint.
        :type meg_level: int
        """

        self._meg_level = meg_level

    @property
    def direction(self):
        """Gets the direction of this TapiOamOamConstraint.


        :return: The direction of this TapiOamOamConstraint.
        :rtype: TapiCommonForwardingDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TapiOamOamConstraint.


        :param direction: The direction of this TapiOamOamConstraint.
        :type direction: TapiCommonForwardingDirection
        """

        self._direction = direction
