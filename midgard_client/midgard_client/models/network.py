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

class Network(object):
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
        'bond_metrics': 'BondMetrics',
        'block_rewards': 'BlockRewards',
        'active_bonds': 'list[str]',
        'standby_bonds': 'list[str]',
        'active_node_count': 'str',
        'standby_node_count': 'str',
        'total_pooled_rune': 'str',
        'total_reserve': 'str',
        'next_churn_height': 'str',
        'pool_activation_countdown': 'str',
        'pool_share_factor': 'str',
        'bonding_apy': 'str',
        'liquidity_apy': 'str'
    }

    attribute_map = {
        'bond_metrics': 'bondMetrics',
        'block_rewards': 'blockRewards',
        'active_bonds': 'activeBonds',
        'standby_bonds': 'standbyBonds',
        'active_node_count': 'activeNodeCount',
        'standby_node_count': 'standbyNodeCount',
        'total_pooled_rune': 'totalPooledRune',
        'total_reserve': 'totalReserve',
        'next_churn_height': 'nextChurnHeight',
        'pool_activation_countdown': 'poolActivationCountdown',
        'pool_share_factor': 'poolShareFactor',
        'bonding_apy': 'bondingAPY',
        'liquidity_apy': 'liquidityAPY'
    }

    def __init__(self, bond_metrics=None, block_rewards=None, active_bonds=None, standby_bonds=None, active_node_count=None, standby_node_count=None, total_pooled_rune=None, total_reserve=None, next_churn_height=None, pool_activation_countdown=None, pool_share_factor=None, bonding_apy=None, liquidity_apy=None):  # noqa: E501
        """Network - a model defined in Swagger"""  # noqa: E501
        self._bond_metrics = None
        self._block_rewards = None
        self._active_bonds = None
        self._standby_bonds = None
        self._active_node_count = None
        self._standby_node_count = None
        self._total_pooled_rune = None
        self._total_reserve = None
        self._next_churn_height = None
        self._pool_activation_countdown = None
        self._pool_share_factor = None
        self._bonding_apy = None
        self._liquidity_apy = None
        self.discriminator = None
        self.bond_metrics = bond_metrics
        self.block_rewards = block_rewards
        self.active_bonds = active_bonds
        self.standby_bonds = standby_bonds
        self.active_node_count = active_node_count
        self.standby_node_count = standby_node_count
        self.total_pooled_rune = total_pooled_rune
        self.total_reserve = total_reserve
        self.next_churn_height = next_churn_height
        self.pool_activation_countdown = pool_activation_countdown
        self.pool_share_factor = pool_share_factor
        self.bonding_apy = bonding_apy
        self.liquidity_apy = liquidity_apy

    @property
    def bond_metrics(self):
        """Gets the bond_metrics of this Network.  # noqa: E501


        :return: The bond_metrics of this Network.  # noqa: E501
        :rtype: BondMetrics
        """
        return self._bond_metrics

    @bond_metrics.setter
    def bond_metrics(self, bond_metrics):
        """Sets the bond_metrics of this Network.


        :param bond_metrics: The bond_metrics of this Network.  # noqa: E501
        :type: BondMetrics
        """
        if bond_metrics is None:
            raise ValueError("Invalid value for `bond_metrics`, must not be `None`")  # noqa: E501

        self._bond_metrics = bond_metrics

    @property
    def block_rewards(self):
        """Gets the block_rewards of this Network.  # noqa: E501


        :return: The block_rewards of this Network.  # noqa: E501
        :rtype: BlockRewards
        """
        return self._block_rewards

    @block_rewards.setter
    def block_rewards(self, block_rewards):
        """Sets the block_rewards of this Network.


        :param block_rewards: The block_rewards of this Network.  # noqa: E501
        :type: BlockRewards
        """
        if block_rewards is None:
            raise ValueError("Invalid value for `block_rewards`, must not be `None`")  # noqa: E501

        self._block_rewards = block_rewards

    @property
    def active_bonds(self):
        """Gets the active_bonds of this Network.  # noqa: E501


        :return: The active_bonds of this Network.  # noqa: E501
        :rtype: list[str]
        """
        return self._active_bonds

    @active_bonds.setter
    def active_bonds(self, active_bonds):
        """Sets the active_bonds of this Network.


        :param active_bonds: The active_bonds of this Network.  # noqa: E501
        :type: list[str]
        """
        if active_bonds is None:
            raise ValueError("Invalid value for `active_bonds`, must not be `None`")  # noqa: E501

        self._active_bonds = active_bonds

    @property
    def standby_bonds(self):
        """Gets the standby_bonds of this Network.  # noqa: E501

        Array of Standby Bonds  # noqa: E501

        :return: The standby_bonds of this Network.  # noqa: E501
        :rtype: list[str]
        """
        return self._standby_bonds

    @standby_bonds.setter
    def standby_bonds(self, standby_bonds):
        """Sets the standby_bonds of this Network.

        Array of Standby Bonds  # noqa: E501

        :param standby_bonds: The standby_bonds of this Network.  # noqa: E501
        :type: list[str]
        """
        if standby_bonds is None:
            raise ValueError("Invalid value for `standby_bonds`, must not be `None`")  # noqa: E501

        self._standby_bonds = standby_bonds

    @property
    def active_node_count(self):
        """Gets the active_node_count of this Network.  # noqa: E501

        Int64, Number of Active Nodes  # noqa: E501

        :return: The active_node_count of this Network.  # noqa: E501
        :rtype: str
        """
        return self._active_node_count

    @active_node_count.setter
    def active_node_count(self, active_node_count):
        """Sets the active_node_count of this Network.

        Int64, Number of Active Nodes  # noqa: E501

        :param active_node_count: The active_node_count of this Network.  # noqa: E501
        :type: str
        """
        if active_node_count is None:
            raise ValueError("Invalid value for `active_node_count`, must not be `None`")  # noqa: E501

        self._active_node_count = active_node_count

    @property
    def standby_node_count(self):
        """Gets the standby_node_count of this Network.  # noqa: E501

        Int64, Number of Standby Nodes  # noqa: E501

        :return: The standby_node_count of this Network.  # noqa: E501
        :rtype: str
        """
        return self._standby_node_count

    @standby_node_count.setter
    def standby_node_count(self, standby_node_count):
        """Sets the standby_node_count of this Network.

        Int64, Number of Standby Nodes  # noqa: E501

        :param standby_node_count: The standby_node_count of this Network.  # noqa: E501
        :type: str
        """
        if standby_node_count is None:
            raise ValueError("Invalid value for `standby_node_count`, must not be `None`")  # noqa: E501

        self._standby_node_count = standby_node_count

    @property
    def total_pooled_rune(self):
        """Gets the total_pooled_rune of this Network.  # noqa: E501

        Int64(e8), Total Rune pooled in all pools  # noqa: E501

        :return: The total_pooled_rune of this Network.  # noqa: E501
        :rtype: str
        """
        return self._total_pooled_rune

    @total_pooled_rune.setter
    def total_pooled_rune(self, total_pooled_rune):
        """Sets the total_pooled_rune of this Network.

        Int64(e8), Total Rune pooled in all pools  # noqa: E501

        :param total_pooled_rune: The total_pooled_rune of this Network.  # noqa: E501
        :type: str
        """
        if total_pooled_rune is None:
            raise ValueError("Invalid value for `total_pooled_rune`, must not be `None`")  # noqa: E501

        self._total_pooled_rune = total_pooled_rune

    @property
    def total_reserve(self):
        """Gets the total_reserve of this Network.  # noqa: E501

        Int64(e8), Total left in Reserve  # noqa: E501

        :return: The total_reserve of this Network.  # noqa: E501
        :rtype: str
        """
        return self._total_reserve

    @total_reserve.setter
    def total_reserve(self, total_reserve):
        """Sets the total_reserve of this Network.

        Int64(e8), Total left in Reserve  # noqa: E501

        :param total_reserve: The total_reserve of this Network.  # noqa: E501
        :type: str
        """
        if total_reserve is None:
            raise ValueError("Invalid value for `total_reserve`, must not be `None`")  # noqa: E501

        self._total_reserve = total_reserve

    @property
    def next_churn_height(self):
        """Gets the next_churn_height of this Network.  # noqa: E501

        Int64, next height of blocks  # noqa: E501

        :return: The next_churn_height of this Network.  # noqa: E501
        :rtype: str
        """
        return self._next_churn_height

    @next_churn_height.setter
    def next_churn_height(self, next_churn_height):
        """Sets the next_churn_height of this Network.

        Int64, next height of blocks  # noqa: E501

        :param next_churn_height: The next_churn_height of this Network.  # noqa: E501
        :type: str
        """
        if next_churn_height is None:
            raise ValueError("Invalid value for `next_churn_height`, must not be `None`")  # noqa: E501

        self._next_churn_height = next_churn_height

    @property
    def pool_activation_countdown(self):
        """Gets the pool_activation_countdown of this Network.  # noqa: E501

        Int64, the remaining time of pool activation (in blocks)  # noqa: E501

        :return: The pool_activation_countdown of this Network.  # noqa: E501
        :rtype: str
        """
        return self._pool_activation_countdown

    @pool_activation_countdown.setter
    def pool_activation_countdown(self, pool_activation_countdown):
        """Sets the pool_activation_countdown of this Network.

        Int64, the remaining time of pool activation (in blocks)  # noqa: E501

        :param pool_activation_countdown: The pool_activation_countdown of this Network.  # noqa: E501
        :type: str
        """
        if pool_activation_countdown is None:
            raise ValueError("Invalid value for `pool_activation_countdown`, must not be `None`")  # noqa: E501

        self._pool_activation_countdown = pool_activation_countdown

    @property
    def pool_share_factor(self):
        """Gets the pool_share_factor of this Network.  # noqa: E501


        :return: The pool_share_factor of this Network.  # noqa: E501
        :rtype: str
        """
        return self._pool_share_factor

    @pool_share_factor.setter
    def pool_share_factor(self, pool_share_factor):
        """Sets the pool_share_factor of this Network.


        :param pool_share_factor: The pool_share_factor of this Network.  # noqa: E501
        :type: str
        """
        if pool_share_factor is None:
            raise ValueError("Invalid value for `pool_share_factor`, must not be `None`")  # noqa: E501

        self._pool_share_factor = pool_share_factor

    @property
    def bonding_apy(self):
        """Gets the bonding_apy of this Network.  # noqa: E501

        Float, (1 + (bondReward * blocksPerMonth/totalActiveBond)) ^ 12 -1  # noqa: E501

        :return: The bonding_apy of this Network.  # noqa: E501
        :rtype: str
        """
        return self._bonding_apy

    @bonding_apy.setter
    def bonding_apy(self, bonding_apy):
        """Sets the bonding_apy of this Network.

        Float, (1 + (bondReward * blocksPerMonth/totalActiveBond)) ^ 12 -1  # noqa: E501

        :param bonding_apy: The bonding_apy of this Network.  # noqa: E501
        :type: str
        """
        if bonding_apy is None:
            raise ValueError("Invalid value for `bonding_apy`, must not be `None`")  # noqa: E501

        self._bonding_apy = bonding_apy

    @property
    def liquidity_apy(self):
        """Gets the liquidity_apy of this Network.  # noqa: E501

        Float, (1 + (stakeReward * blocksPerMonth/totalDepth of active pools)) ^ 12 -1  # noqa: E501

        :return: The liquidity_apy of this Network.  # noqa: E501
        :rtype: str
        """
        return self._liquidity_apy

    @liquidity_apy.setter
    def liquidity_apy(self, liquidity_apy):
        """Sets the liquidity_apy of this Network.

        Float, (1 + (stakeReward * blocksPerMonth/totalDepth of active pools)) ^ 12 -1  # noqa: E501

        :param liquidity_apy: The liquidity_apy of this Network.  # noqa: E501
        :type: str
        """
        if liquidity_apy is None:
            raise ValueError("Invalid value for `liquidity_apy`, must not be `None`")  # noqa: E501

        self._liquidity_apy = liquidity_apy

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
        if issubclass(Network, dict):
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
        if not isinstance(other, Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
