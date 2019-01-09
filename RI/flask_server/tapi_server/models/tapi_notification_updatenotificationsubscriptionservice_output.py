# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_notification_subscription_service import TapiNotificationNotificationSubscriptionService  # noqa: F401,E501
from tapi_server import util


class TapiNotificationUpdatenotificationsubscriptionserviceOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subscription_service=None):  # noqa: E501
        """TapiNotificationUpdatenotificationsubscriptionserviceOutput - a model defined in OpenAPI

        :param subscription_service: The subscription_service of this TapiNotificationUpdatenotificationsubscriptionserviceOutput.  # noqa: E501
        :type subscription_service: TapiNotificationNotificationSubscriptionService
        """
        self.openapi_types = {
            'subscription_service': TapiNotificationNotificationSubscriptionService
        }

        self.attribute_map = {
            'subscription_service': 'subscription-service'
        }

        self._subscription_service = subscription_service

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationUpdatenotificationsubscriptionserviceOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.updatenotificationsubscriptionservice.Output of this TapiNotificationUpdatenotificationsubscriptionserviceOutput.  # noqa: E501
        :rtype: TapiNotificationUpdatenotificationsubscriptionserviceOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_service(self):
        """Gets the subscription_service of this TapiNotificationUpdatenotificationsubscriptionserviceOutput.


        :return: The subscription_service of this TapiNotificationUpdatenotificationsubscriptionserviceOutput.
        :rtype: TapiNotificationNotificationSubscriptionService
        """
        return self._subscription_service

    @subscription_service.setter
    def subscription_service(self, subscription_service):
        """Sets the subscription_service of this TapiNotificationUpdatenotificationsubscriptionserviceOutput.


        :param subscription_service: The subscription_service of this TapiNotificationUpdatenotificationsubscriptionserviceOutput.
        :type subscription_service: TapiNotificationNotificationSubscriptionService
        """

        self._subscription_service = subscription_service