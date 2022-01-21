# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.4.1
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProxiedNode(object):
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
        'node_address': 'str',
        'status': 'str',
        'pub_key_set': 'ProxiedNodePubKeySet',
        'validator_cons_pub_key': 'str',
        'bond': 'str',
        'active_block_height': 'int',
        'bond_address': 'str',
        'status_since': 'int',
        'signer_membership': 'list[str]',
        'requested_to_leave': 'bool',
        'forced_to_leave': 'bool',
        'leave_height': 'int',
        'ip_address': 'str',
        'version': 'str',
        'slash_points': 'int',
        'jail': 'ProxiedNodeJail',
        'current_award': 'str',
        'observe_chains': 'list[ObservedChain]',
        'preflight_status': 'PreflightStatus'
    }

    attribute_map = {
        'node_address': 'node_address',
        'status': 'status',
        'pub_key_set': 'pub_key_set',
        'validator_cons_pub_key': 'validator_cons_pub_key',
        'bond': 'bond',
        'active_block_height': 'active_block_height',
        'bond_address': 'bond_address',
        'status_since': 'status_since',
        'signer_membership': 'signer_membership',
        'requested_to_leave': 'requested_to_leave',
        'forced_to_leave': 'forced_to_leave',
        'leave_height': 'leave_height',
        'ip_address': 'ip_address',
        'version': 'version',
        'slash_points': 'slash_points',
        'jail': 'jail',
        'current_award': 'current_award',
        'observe_chains': 'observe_chains',
        'preflight_status': 'preflight_status'
    }

    def __init__(self, node_address=None, status=None, pub_key_set=None, validator_cons_pub_key=None, bond=None, active_block_height=None, bond_address=None, status_since=None, signer_membership=None, requested_to_leave=None, forced_to_leave=None, leave_height=None, ip_address=None, version=None, slash_points=None, jail=None, current_award=None, observe_chains=None, preflight_status=None):  # noqa: E501
        """ProxiedNode - a model defined in Swagger"""  # noqa: E501
        self._node_address = None
        self._status = None
        self._pub_key_set = None
        self._validator_cons_pub_key = None
        self._bond = None
        self._active_block_height = None
        self._bond_address = None
        self._status_since = None
        self._signer_membership = None
        self._requested_to_leave = None
        self._forced_to_leave = None
        self._leave_height = None
        self._ip_address = None
        self._version = None
        self._slash_points = None
        self._jail = None
        self._current_award = None
        self._observe_chains = None
        self._preflight_status = None
        self.discriminator = None
        self.node_address = node_address
        self.status = status
        self.pub_key_set = pub_key_set
        self.validator_cons_pub_key = validator_cons_pub_key
        self.bond = bond
        self.active_block_height = active_block_height
        self.bond_address = bond_address
        self.status_since = status_since
        self.signer_membership = signer_membership
        self.requested_to_leave = requested_to_leave
        self.forced_to_leave = forced_to_leave
        self.leave_height = leave_height
        self.ip_address = ip_address
        self.version = version
        self.slash_points = slash_points
        self.jail = jail
        self.current_award = current_award
        self.observe_chains = observe_chains
        self.preflight_status = preflight_status

    @property
    def node_address(self):
        """Gets the node_address of this ProxiedNode.  # noqa: E501


        :return: The node_address of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._node_address

    @node_address.setter
    def node_address(self, node_address):
        """Sets the node_address of this ProxiedNode.


        :param node_address: The node_address of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if node_address is None:
            raise ValueError("Invalid value for `node_address`, must not be `None`")  # noqa: E501

        self._node_address = node_address

    @property
    def status(self):
        """Gets the status of this ProxiedNode.  # noqa: E501


        :return: The status of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProxiedNode.


        :param status: The status of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def pub_key_set(self):
        """Gets the pub_key_set of this ProxiedNode.  # noqa: E501


        :return: The pub_key_set of this ProxiedNode.  # noqa: E501
        :rtype: ProxiedNodePubKeySet
        """
        return self._pub_key_set

    @pub_key_set.setter
    def pub_key_set(self, pub_key_set):
        """Sets the pub_key_set of this ProxiedNode.


        :param pub_key_set: The pub_key_set of this ProxiedNode.  # noqa: E501
        :type: ProxiedNodePubKeySet
        """
        if pub_key_set is None:
            raise ValueError("Invalid value for `pub_key_set`, must not be `None`")  # noqa: E501

        self._pub_key_set = pub_key_set

    @property
    def validator_cons_pub_key(self):
        """Gets the validator_cons_pub_key of this ProxiedNode.  # noqa: E501


        :return: The validator_cons_pub_key of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._validator_cons_pub_key

    @validator_cons_pub_key.setter
    def validator_cons_pub_key(self, validator_cons_pub_key):
        """Sets the validator_cons_pub_key of this ProxiedNode.


        :param validator_cons_pub_key: The validator_cons_pub_key of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if validator_cons_pub_key is None:
            raise ValueError("Invalid value for `validator_cons_pub_key`, must not be `None`")  # noqa: E501

        self._validator_cons_pub_key = validator_cons_pub_key

    @property
    def bond(self):
        """Gets the bond of this ProxiedNode.  # noqa: E501


        :return: The bond of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._bond

    @bond.setter
    def bond(self, bond):
        """Sets the bond of this ProxiedNode.


        :param bond: The bond of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if bond is None:
            raise ValueError("Invalid value for `bond`, must not be `None`")  # noqa: E501

        self._bond = bond

    @property
    def active_block_height(self):
        """Gets the active_block_height of this ProxiedNode.  # noqa: E501


        :return: The active_block_height of this ProxiedNode.  # noqa: E501
        :rtype: int
        """
        return self._active_block_height

    @active_block_height.setter
    def active_block_height(self, active_block_height):
        """Sets the active_block_height of this ProxiedNode.


        :param active_block_height: The active_block_height of this ProxiedNode.  # noqa: E501
        :type: int
        """
        if active_block_height is None:
            raise ValueError("Invalid value for `active_block_height`, must not be `None`")  # noqa: E501

        self._active_block_height = active_block_height

    @property
    def bond_address(self):
        """Gets the bond_address of this ProxiedNode.  # noqa: E501


        :return: The bond_address of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._bond_address

    @bond_address.setter
    def bond_address(self, bond_address):
        """Sets the bond_address of this ProxiedNode.


        :param bond_address: The bond_address of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if bond_address is None:
            raise ValueError("Invalid value for `bond_address`, must not be `None`")  # noqa: E501

        self._bond_address = bond_address

    @property
    def status_since(self):
        """Gets the status_since of this ProxiedNode.  # noqa: E501


        :return: The status_since of this ProxiedNode.  # noqa: E501
        :rtype: int
        """
        return self._status_since

    @status_since.setter
    def status_since(self, status_since):
        """Sets the status_since of this ProxiedNode.


        :param status_since: The status_since of this ProxiedNode.  # noqa: E501
        :type: int
        """
        if status_since is None:
            raise ValueError("Invalid value for `status_since`, must not be `None`")  # noqa: E501

        self._status_since = status_since

    @property
    def signer_membership(self):
        """Gets the signer_membership of this ProxiedNode.  # noqa: E501


        :return: The signer_membership of this ProxiedNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._signer_membership

    @signer_membership.setter
    def signer_membership(self, signer_membership):
        """Sets the signer_membership of this ProxiedNode.


        :param signer_membership: The signer_membership of this ProxiedNode.  # noqa: E501
        :type: list[str]
        """
        if signer_membership is None:
            raise ValueError("Invalid value for `signer_membership`, must not be `None`")  # noqa: E501

        self._signer_membership = signer_membership

    @property
    def requested_to_leave(self):
        """Gets the requested_to_leave of this ProxiedNode.  # noqa: E501


        :return: The requested_to_leave of this ProxiedNode.  # noqa: E501
        :rtype: bool
        """
        return self._requested_to_leave

    @requested_to_leave.setter
    def requested_to_leave(self, requested_to_leave):
        """Sets the requested_to_leave of this ProxiedNode.


        :param requested_to_leave: The requested_to_leave of this ProxiedNode.  # noqa: E501
        :type: bool
        """
        if requested_to_leave is None:
            raise ValueError("Invalid value for `requested_to_leave`, must not be `None`")  # noqa: E501

        self._requested_to_leave = requested_to_leave

    @property
    def forced_to_leave(self):
        """Gets the forced_to_leave of this ProxiedNode.  # noqa: E501


        :return: The forced_to_leave of this ProxiedNode.  # noqa: E501
        :rtype: bool
        """
        return self._forced_to_leave

    @forced_to_leave.setter
    def forced_to_leave(self, forced_to_leave):
        """Sets the forced_to_leave of this ProxiedNode.


        :param forced_to_leave: The forced_to_leave of this ProxiedNode.  # noqa: E501
        :type: bool
        """
        if forced_to_leave is None:
            raise ValueError("Invalid value for `forced_to_leave`, must not be `None`")  # noqa: E501

        self._forced_to_leave = forced_to_leave

    @property
    def leave_height(self):
        """Gets the leave_height of this ProxiedNode.  # noqa: E501


        :return: The leave_height of this ProxiedNode.  # noqa: E501
        :rtype: int
        """
        return self._leave_height

    @leave_height.setter
    def leave_height(self, leave_height):
        """Sets the leave_height of this ProxiedNode.


        :param leave_height: The leave_height of this ProxiedNode.  # noqa: E501
        :type: int
        """
        if leave_height is None:
            raise ValueError("Invalid value for `leave_height`, must not be `None`")  # noqa: E501

        self._leave_height = leave_height

    @property
    def ip_address(self):
        """Gets the ip_address of this ProxiedNode.  # noqa: E501


        :return: The ip_address of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ProxiedNode.


        :param ip_address: The ip_address of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def version(self):
        """Gets the version of this ProxiedNode.  # noqa: E501


        :return: The version of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProxiedNode.


        :param version: The version of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def slash_points(self):
        """Gets the slash_points of this ProxiedNode.  # noqa: E501


        :return: The slash_points of this ProxiedNode.  # noqa: E501
        :rtype: int
        """
        return self._slash_points

    @slash_points.setter
    def slash_points(self, slash_points):
        """Sets the slash_points of this ProxiedNode.


        :param slash_points: The slash_points of this ProxiedNode.  # noqa: E501
        :type: int
        """
        if slash_points is None:
            raise ValueError("Invalid value for `slash_points`, must not be `None`")  # noqa: E501

        self._slash_points = slash_points

    @property
    def jail(self):
        """Gets the jail of this ProxiedNode.  # noqa: E501


        :return: The jail of this ProxiedNode.  # noqa: E501
        :rtype: ProxiedNodeJail
        """
        return self._jail

    @jail.setter
    def jail(self, jail):
        """Sets the jail of this ProxiedNode.


        :param jail: The jail of this ProxiedNode.  # noqa: E501
        :type: ProxiedNodeJail
        """
        if jail is None:
            raise ValueError("Invalid value for `jail`, must not be `None`")  # noqa: E501

        self._jail = jail

    @property
    def current_award(self):
        """Gets the current_award of this ProxiedNode.  # noqa: E501


        :return: The current_award of this ProxiedNode.  # noqa: E501
        :rtype: str
        """
        return self._current_award

    @current_award.setter
    def current_award(self, current_award):
        """Sets the current_award of this ProxiedNode.


        :param current_award: The current_award of this ProxiedNode.  # noqa: E501
        :type: str
        """
        if current_award is None:
            raise ValueError("Invalid value for `current_award`, must not be `None`")  # noqa: E501

        self._current_award = current_award

    @property
    def observe_chains(self):
        """Gets the observe_chains of this ProxiedNode.  # noqa: E501


        :return: The observe_chains of this ProxiedNode.  # noqa: E501
        :rtype: list[ObservedChain]
        """
        return self._observe_chains

    @observe_chains.setter
    def observe_chains(self, observe_chains):
        """Sets the observe_chains of this ProxiedNode.


        :param observe_chains: The observe_chains of this ProxiedNode.  # noqa: E501
        :type: list[ObservedChain]
        """
        if observe_chains is None:
            raise ValueError("Invalid value for `observe_chains`, must not be `None`")  # noqa: E501

        self._observe_chains = observe_chains

    @property
    def preflight_status(self):
        """Gets the preflight_status of this ProxiedNode.  # noqa: E501


        :return: The preflight_status of this ProxiedNode.  # noqa: E501
        :rtype: PreflightStatus
        """
        return self._preflight_status

    @preflight_status.setter
    def preflight_status(self, preflight_status):
        """Sets the preflight_status of this ProxiedNode.


        :param preflight_status: The preflight_status of this ProxiedNode.  # noqa: E501
        :type: PreflightStatus
        """
        if preflight_status is None:
            raise ValueError("Invalid value for `preflight_status`, must not be `None`")  # noqa: E501

        self._preflight_status = preflight_status

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
        if issubclass(ProxiedNode, dict):
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
        if not isinstance(other, ProxiedNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
