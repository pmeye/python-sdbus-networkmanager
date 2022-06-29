# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class WpanSettings(NetworkManagerSettingsMixin):
    """IEEE 802.15.4 (WPAN) MAC Settings"""

    channel: Optional[int] = field(
        metadata={'dbus_name': 'channel', 'dbus_type': 'i'},
        default=None,
    )
    mac_address: Optional[str] = field(
        metadata={'dbus_name': 'mac-address', 'dbus_type': 's'},
        default=None,
    )
    page: Optional[int] = field(
        metadata={'dbus_name': 'page', 'dbus_type': 'i'},
        default=None,
    )
    pan_id: Optional[int] = field(
        metadata={'dbus_name': 'pan-id', 'dbus_type': 'u'},
        default=65535,
    )
    short_address: Optional[int] = field(
        metadata={'dbus_name': 'short-address', 'dbus_type': 'u'},
        default=65535,
    )