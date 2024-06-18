#!/usr/bin/python
# -*- coding: utf-8 -*-

from netmiko.base_connection import BaseConnection
from netmiko import log


class PhoenixFl(BaseConnection):
    """
    Implement methods for interacting with Phoenix FL (TODO: figure out which devices exactly)
     devices
    for both SSH and telnet.

    Not applicable in Phoenix FL (disabled):
        -

    Overriden methods to adapt Phoenix FL behavior (changed):
    TODO: ADAPT
        - session_preparation()
        - set_base_prompt()
        - config_mode()
        - exit_config_mode()
        - check_config_mode()
        - save_config()
        - commit()
        - strip_prompt()
        - enable()
        - check_enable_mode()
    """
    pass


class PhoenixFlSSH(PhoenixFl):
    pass


class PhoenixFlTelnet(PhoenixFl):
    pass
