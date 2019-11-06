# coding: utf-8

"""
    API

    ## Welcome  This is a place to put general notes and extra information, for internal use.  To get started designing/documenting this API, select a version on the left. # Title No Description  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse20057(object):
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
        'success': 'bool',
        'guest_session_id': 'str',
        'expires_at': 'str'
    }

    attribute_map = {
        'success': 'success',
        'guest_session_id': 'guest_session_id',
        'expires_at': 'expires_at'
    }

    def __init__(self, success=None, guest_session_id=None, expires_at=None):  # noqa: E501
        """InlineResponse20057 - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._guest_session_id = None
        self._expires_at = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if guest_session_id is not None:
            self.guest_session_id = guest_session_id
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def success(self):
        """Gets the success of this InlineResponse20057.  # noqa: E501


        :return: The success of this InlineResponse20057.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse20057.


        :param success: The success of this InlineResponse20057.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def guest_session_id(self):
        """Gets the guest_session_id of this InlineResponse20057.  # noqa: E501


        :return: The guest_session_id of this InlineResponse20057.  # noqa: E501
        :rtype: str
        """
        return self._guest_session_id

    @guest_session_id.setter
    def guest_session_id(self, guest_session_id):
        """Sets the guest_session_id of this InlineResponse20057.


        :param guest_session_id: The guest_session_id of this InlineResponse20057.  # noqa: E501
        :type: str
        """

        self._guest_session_id = guest_session_id

    @property
    def expires_at(self):
        """Gets the expires_at of this InlineResponse20057.  # noqa: E501


        :return: The expires_at of this InlineResponse20057.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this InlineResponse20057.


        :param expires_at: The expires_at of this InlineResponse20057.  # noqa: E501
        :type: str
        """

        self._expires_at = expires_at

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
        if issubclass(InlineResponse20057, dict):
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
        if not isinstance(other, InlineResponse20057):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other