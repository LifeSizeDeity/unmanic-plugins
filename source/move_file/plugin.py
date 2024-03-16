#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from unmanic.libs.unplugins.settings import PluginSettings

# Configure plugin logger
logger = logging.getLogger("Unmanic.Plugin.move_file")


class Settings(PluginSettings):
    settings = {}

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)


def on_postprocessor_file_movement(data):
    """
    Runner function - configures additional postprocessor file movements during the postprocessor stage of a task.

    The 'data' object argument includes:
        library_id              - Integer, the library that the current task is associated with.
        source_data             - Dictionary, data pertaining to the original source file.
        remove_source_file      - Boolean, should Unmanic remove the original source file after all copy operations are complete. (default: 'True' if file name has changed)
        copy_file               - Boolean, should Unmanic run a copy operation with the returned data variables. (default: 'False')
        file_in                 - String, the converted cache file to be copied by the postprocessor.
        file_out                - String, the destination file that the file will be copied to.
        run_default_file_copy   - Boolean, should Unmanic run the default post-process file movement. (default: 'True')

    :param data:
    :return:
    
    """
    return
