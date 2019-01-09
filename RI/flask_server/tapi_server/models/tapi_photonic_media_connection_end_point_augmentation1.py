# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_otsi_assembly_connection_end_point_spec import TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaConnectionEndPointAugmentation1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, otsi_assembly_connection_end_point_spec=None):  # noqa: E501
        """TapiPhotonicMediaConnectionEndPointAugmentation1 - a model defined in OpenAPI

        :param otsi_assembly_connection_end_point_spec: The otsi_assembly_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation1.  # noqa: E501
        :type otsi_assembly_connection_end_point_spec: TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec
        """
        self.openapi_types = {
            'otsi_assembly_connection_end_point_spec': TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec
        }

        self.attribute_map = {
            'otsi_assembly_connection_end_point_spec': 'otsi-assembly-connection-end-point-spec'
        }

        self._otsi_assembly_connection_end_point_spec = otsi_assembly_connection_end_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaConnectionEndPointAugmentation1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.ConnectionEndPointAugmentation1 of this TapiPhotonicMediaConnectionEndPointAugmentation1.  # noqa: E501
        :rtype: TapiPhotonicMediaConnectionEndPointAugmentation1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def otsi_assembly_connection_end_point_spec(self):
        """Gets the otsi_assembly_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation1.


        :return: The otsi_assembly_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation1.
        :rtype: TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec
        """
        return self._otsi_assembly_connection_end_point_spec

    @otsi_assembly_connection_end_point_spec.setter
    def otsi_assembly_connection_end_point_spec(self, otsi_assembly_connection_end_point_spec):
        """Sets the otsi_assembly_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation1.


        :param otsi_assembly_connection_end_point_spec: The otsi_assembly_connection_end_point_spec of this TapiPhotonicMediaConnectionEndPointAugmentation1.
        :type otsi_assembly_connection_end_point_spec: TapiPhotonicMediaOtsiAssemblyConnectionEndPointSpec
        """

        self._otsi_assembly_connection_end_point_spec = otsi_assembly_connection_end_point_spec