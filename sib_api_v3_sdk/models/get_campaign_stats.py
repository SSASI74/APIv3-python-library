# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCampaignStats(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'list_id': 'int',
        'unique_clicks': 'int',
        'clickers': 'int',
        'complaints': 'int',
        'delivered': 'int',
        'sent': 'int',
        'soft_bounces': 'int',
        'hard_bounces': 'int',
        'unique_views': 'int',
        'unsubscriptions': 'int',
        'viewed': 'int',
        'deferred': 'int'
    }

    attribute_map = {
        'list_id': 'listId',
        'unique_clicks': 'uniqueClicks',
        'clickers': 'clickers',
        'complaints': 'complaints',
        'delivered': 'delivered',
        'sent': 'sent',
        'soft_bounces': 'softBounces',
        'hard_bounces': 'hardBounces',
        'unique_views': 'uniqueViews',
        'unsubscriptions': 'unsubscriptions',
        'viewed': 'viewed',
        'deferred': 'deferred'
    }

    def __init__(self, list_id=None, unique_clicks=None, clickers=None, complaints=None, delivered=None, sent=None, soft_bounces=None, hard_bounces=None, unique_views=None, unsubscriptions=None, viewed=None, deferred=None):
        """
        GetCampaignStats - a model defined in Swagger
        """

        self._list_id = None
        self._unique_clicks = None
        self._clickers = None
        self._complaints = None
        self._delivered = None
        self._sent = None
        self._soft_bounces = None
        self._hard_bounces = None
        self._unique_views = None
        self._unsubscriptions = None
        self._viewed = None
        self._deferred = None

        self.list_id = list_id
        self.unique_clicks = unique_clicks
        self.clickers = clickers
        self.complaints = complaints
        self.delivered = delivered
        self.sent = sent
        self.soft_bounces = soft_bounces
        self.hard_bounces = hard_bounces
        self.unique_views = unique_views
        self.unsubscriptions = unsubscriptions
        self.viewed = viewed
        self.deferred = deferred

    @property
    def list_id(self):
        """
        Gets the list_id of this GetCampaignStats.
        List Id of email campaign (only in case of get email campaign(s))

        :return: The list_id of this GetCampaignStats.
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """
        Sets the list_id of this GetCampaignStats.
        List Id of email campaign (only in case of get email campaign(s))

        :param list_id: The list_id of this GetCampaignStats.
        :type: int
        """
        if list_id is None:
            raise ValueError("Invalid value for `list_id`, must not be `None`")

        self._list_id = list_id

    @property
    def unique_clicks(self):
        """
        Gets the unique_clicks of this GetCampaignStats.
        Number of unique clicks for the campaign

        :return: The unique_clicks of this GetCampaignStats.
        :rtype: int
        """
        return self._unique_clicks

    @unique_clicks.setter
    def unique_clicks(self, unique_clicks):
        """
        Sets the unique_clicks of this GetCampaignStats.
        Number of unique clicks for the campaign

        :param unique_clicks: The unique_clicks of this GetCampaignStats.
        :type: int
        """
        if unique_clicks is None:
            raise ValueError("Invalid value for `unique_clicks`, must not be `None`")

        self._unique_clicks = unique_clicks

    @property
    def clickers(self):
        """
        Gets the clickers of this GetCampaignStats.
        Number of clicks for the campaign

        :return: The clickers of this GetCampaignStats.
        :rtype: int
        """
        return self._clickers

    @clickers.setter
    def clickers(self, clickers):
        """
        Sets the clickers of this GetCampaignStats.
        Number of clicks for the campaign

        :param clickers: The clickers of this GetCampaignStats.
        :type: int
        """
        if clickers is None:
            raise ValueError("Invalid value for `clickers`, must not be `None`")

        self._clickers = clickers

    @property
    def complaints(self):
        """
        Gets the complaints of this GetCampaignStats.
        Number of complaints (Spam reports) for the campaign

        :return: The complaints of this GetCampaignStats.
        :rtype: int
        """
        return self._complaints

    @complaints.setter
    def complaints(self, complaints):
        """
        Sets the complaints of this GetCampaignStats.
        Number of complaints (Spam reports) for the campaign

        :param complaints: The complaints of this GetCampaignStats.
        :type: int
        """
        if complaints is None:
            raise ValueError("Invalid value for `complaints`, must not be `None`")

        self._complaints = complaints

    @property
    def delivered(self):
        """
        Gets the delivered of this GetCampaignStats.
        Number of delivered emails for the campaign

        :return: The delivered of this GetCampaignStats.
        :rtype: int
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """
        Sets the delivered of this GetCampaignStats.
        Number of delivered emails for the campaign

        :param delivered: The delivered of this GetCampaignStats.
        :type: int
        """
        if delivered is None:
            raise ValueError("Invalid value for `delivered`, must not be `None`")

        self._delivered = delivered

    @property
    def sent(self):
        """
        Gets the sent of this GetCampaignStats.
        Number of sent emails for the campaign

        :return: The sent of this GetCampaignStats.
        :rtype: int
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """
        Sets the sent of this GetCampaignStats.
        Number of sent emails for the campaign

        :param sent: The sent of this GetCampaignStats.
        :type: int
        """
        if sent is None:
            raise ValueError("Invalid value for `sent`, must not be `None`")

        self._sent = sent

    @property
    def soft_bounces(self):
        """
        Gets the soft_bounces of this GetCampaignStats.
        Number of softbounce for the campaign

        :return: The soft_bounces of this GetCampaignStats.
        :rtype: int
        """
        return self._soft_bounces

    @soft_bounces.setter
    def soft_bounces(self, soft_bounces):
        """
        Sets the soft_bounces of this GetCampaignStats.
        Number of softbounce for the campaign

        :param soft_bounces: The soft_bounces of this GetCampaignStats.
        :type: int
        """
        if soft_bounces is None:
            raise ValueError("Invalid value for `soft_bounces`, must not be `None`")

        self._soft_bounces = soft_bounces

    @property
    def hard_bounces(self):
        """
        Gets the hard_bounces of this GetCampaignStats.
        Number of harbounce for the campaign

        :return: The hard_bounces of this GetCampaignStats.
        :rtype: int
        """
        return self._hard_bounces

    @hard_bounces.setter
    def hard_bounces(self, hard_bounces):
        """
        Sets the hard_bounces of this GetCampaignStats.
        Number of harbounce for the campaign

        :param hard_bounces: The hard_bounces of this GetCampaignStats.
        :type: int
        """
        if hard_bounces is None:
            raise ValueError("Invalid value for `hard_bounces`, must not be `None`")

        self._hard_bounces = hard_bounces

    @property
    def unique_views(self):
        """
        Gets the unique_views of this GetCampaignStats.
        Number of unique openings for the campaign

        :return: The unique_views of this GetCampaignStats.
        :rtype: int
        """
        return self._unique_views

    @unique_views.setter
    def unique_views(self, unique_views):
        """
        Sets the unique_views of this GetCampaignStats.
        Number of unique openings for the campaign

        :param unique_views: The unique_views of this GetCampaignStats.
        :type: int
        """
        if unique_views is None:
            raise ValueError("Invalid value for `unique_views`, must not be `None`")

        self._unique_views = unique_views

    @property
    def unsubscriptions(self):
        """
        Gets the unsubscriptions of this GetCampaignStats.
        Number of unsubscription for the campaign

        :return: The unsubscriptions of this GetCampaignStats.
        :rtype: int
        """
        return self._unsubscriptions

    @unsubscriptions.setter
    def unsubscriptions(self, unsubscriptions):
        """
        Sets the unsubscriptions of this GetCampaignStats.
        Number of unsubscription for the campaign

        :param unsubscriptions: The unsubscriptions of this GetCampaignStats.
        :type: int
        """
        if unsubscriptions is None:
            raise ValueError("Invalid value for `unsubscriptions`, must not be `None`")

        self._unsubscriptions = unsubscriptions

    @property
    def viewed(self):
        """
        Gets the viewed of this GetCampaignStats.
        Number of openings for the campaign

        :return: The viewed of this GetCampaignStats.
        :rtype: int
        """
        return self._viewed

    @viewed.setter
    def viewed(self, viewed):
        """
        Sets the viewed of this GetCampaignStats.
        Number of openings for the campaign

        :param viewed: The viewed of this GetCampaignStats.
        :type: int
        """
        if viewed is None:
            raise ValueError("Invalid value for `viewed`, must not be `None`")

        self._viewed = viewed

    @property
    def deferred(self):
        """
        Gets the deferred of this GetCampaignStats.
        Number of deferred emails for the campaign

        :return: The deferred of this GetCampaignStats.
        :rtype: int
        """
        return self._deferred

    @deferred.setter
    def deferred(self, deferred):
        """
        Sets the deferred of this GetCampaignStats.
        Number of deferred emails for the campaign

        :param deferred: The deferred of this GetCampaignStats.
        :type: int
        """
        if deferred is None:
            raise ValueError("Invalid value for `deferred`, must not be `None`")

        self._deferred = deferred

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetCampaignStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other