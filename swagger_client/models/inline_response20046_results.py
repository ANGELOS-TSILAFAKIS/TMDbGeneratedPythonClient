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


class InlineResponse20046Results(object):
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
        'id': 'int',
        'episode_number': 'int',
        'season_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'episode_number': 'episode_number',
        'season_number': 'season_number'
    }

    def __init__(self, id=None, episode_number=None, season_number=None):  # noqa: E501
        """InlineResponse20046Results - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._episode_number = None
        self._season_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if episode_number is not None:
            self.episode_number = episode_number
        if season_number is not None:
            self.season_number = season_number

    @property
    def id(self):
        """Gets the id of this InlineResponse20046Results.  # noqa: E501


        :return: The id of this InlineResponse20046Results.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20046Results.


        :param id: The id of this InlineResponse20046Results.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def episode_number(self):
        """Gets the episode_number of this InlineResponse20046Results.  # noqa: E501


        :return: The episode_number of this InlineResponse20046Results.  # noqa: E501
        :rtype: int
        """
        return self._episode_number

    @episode_number.setter
    def episode_number(self, episode_number):
        """Sets the episode_number of this InlineResponse20046Results.


        :param episode_number: The episode_number of this InlineResponse20046Results.  # noqa: E501
        :type: int
        """

        self._episode_number = episode_number

    @property
    def season_number(self):
        """Gets the season_number of this InlineResponse20046Results.  # noqa: E501


        :return: The season_number of this InlineResponse20046Results.  # noqa: E501
        :rtype: int
        """
        return self._season_number

    @season_number.setter
    def season_number(self, season_number):
        """Sets the season_number of this InlineResponse20046Results.


        :param season_number: The season_number of this InlineResponse20046Results.  # noqa: E501
        :type: int
        """

        self._season_number = season_number

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
        if issubclass(InlineResponse20046Results, dict):
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
        if not isinstance(other, InlineResponse20046Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
