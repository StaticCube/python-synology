# -*- coding: utf-8 -*-
"""DSM Upgrade data and actions."""


class SynoCoreUpgrade(object):
    """Class containing upgrade data and actions."""

    API_BASE_KEY = "SYNO.Core.Upgrade"
    API_SERVER_KEY = API_BASE_KEY + ".Server"

    def __init__(self, dsm):
        self._dsm = dsm
        self._data = {}

    def update(self):
        """Updates Upgrade data."""
        raw_data = self._dsm.get(self.API_SERVER_KEY, "check")
        if raw_data:
            self._data.update(raw_data["data"])

    @property
    def update_available(self):
        """Gets all Upgrade info."""
        return self._data["update"].get("available")
