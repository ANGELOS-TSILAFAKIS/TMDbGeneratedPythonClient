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


class InlineResponse2003(object):
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
        'avatar': 'InlineResponse2003Avatar',
        'id': 'int',
        'iso_639_1': 'str',
        'iso_3166_1': 'str',
        'name': 'str',
        'include_adult': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'avatar': 'avatar',
        'id': 'id',
        'iso_639_1': 'iso_639_1',
        'iso_3166_1': 'iso_3166_1',
        'name': 'name',
        'include_adult': 'include_adult',
        'username': 'username'
    }

    def __init__(self, avatar=None, id=None, iso_639_1=None, iso_3166_1=None, name=None, include_adult=None, username=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger"""  # noqa: E501
        self._avatar = None
        self._id = None
        self._iso_639_1 = None
        self._iso_3166_1 = None
        self._name = None
        self._include_adult = None
        self._username = None
        self.discriminator = None
        if avatar is not None:
            self.avatar = avatar
        if id is not None:
            self.id = id
        if iso_639_1 is not None:
            self.iso_639_1 = iso_639_1
        if iso_3166_1 is not None:
            self.iso_3166_1 = iso_3166_1
        if name is not None:
            self.name = name
        if include_adult is not None:
            self.include_adult = include_adult
        if username is not None:
            self.username = username

    @property
    def avatar(self):
        """Gets the avatar of this InlineResponse2003.  # noqa: E501


        :return: The avatar of this InlineResponse2003.  # noqa: E501
        :rtype: InlineResponse2003Avatar
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this InlineResponse2003.


        :param avatar: The avatar of this InlineResponse2003.  # noqa: E501
        :type: InlineResponse2003Avatar
        """

        self._avatar = avatar

    @property
    def id(self):
        """Gets the id of this InlineResponse2003.  # noqa: E501


        :return: The id of this InlineResponse2003.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2003.


        :param id: The id of this InlineResponse2003.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def iso_639_1(self):
        """Gets the iso_639_1 of this InlineResponse2003.  # noqa: E501


        :return: The iso_639_1 of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._iso_639_1

    @iso_639_1.setter
    def iso_639_1(self, iso_639_1):
        """Sets the iso_639_1 of this InlineResponse2003.


        :param iso_639_1: The iso_639_1 of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._iso_639_1 = iso_639_1

    @property
    def iso_3166_1(self):
        """Gets the iso_3166_1 of this InlineResponse2003.  # noqa: E501


        :return: The iso_3166_1 of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._iso_3166_1

    @iso_3166_1.setter
    def iso_3166_1(self, iso_3166_1):
        """Sets the iso_3166_1 of this InlineResponse2003.


        :param iso_3166_1: The iso_3166_1 of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._iso_3166_1 = iso_3166_1

    @property
    def name(self):
        """Gets the name of this InlineResponse2003.  # noqa: E501


        :return: The name of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2003.


        :param name: The name of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def include_adult(self):
        """Gets the include_adult of this InlineResponse2003.  # noqa: E501


        :return: The include_adult of this InlineResponse2003.  # noqa: E501
        :rtype: bool
        """
        return self._include_adult

    @include_adult.setter
    def include_adult(self, include_adult):
        """Sets the include_adult of this InlineResponse2003.


        :param include_adult: The include_adult of this InlineResponse2003.  # noqa: E501
        :type: bool
        """

        self._include_adult = include_adult

    @property
    def username(self):
        """Gets the username of this InlineResponse2003.  # noqa: E501


        :return: The username of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineResponse2003.


        :param username: The username of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(InlineResponse2003, dict):
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other