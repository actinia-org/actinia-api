# -*- coding: utf-8 -*-
#######
# actinia-core - an open source REST API for scalable, distributed, high
# performance processing of geographical data that uses GRASS GIS for
# computational tasks. For details, see https://actinia.mundialis.de/
#
# Copyright (c) 2016-2022 Sören Gebbert and mundialis GmbH & Co. KG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#######

"""
API docs for resource_storage_management
"""

from actinia_core.models.response_models import (
    ProcessingErrorResponseModel,
    ProcessingResponseModel,
    StorageResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Resource Management"],
    "description": "Get the current size of the resource storage. "
    "Minimum required user role: admin.",
    "responses": {
        "200": {
            "description": "The current state of the resource storage",
            "schema": StorageResponseModel,
        },
        "400": {
            "description": "The error message why resource storage "
            "information gathering did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

delete_doc = {
    "tags": ["Resource Management"],
    "description": "Clean the resource storage and remove all cached data. "
    "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "olderthan",
            "description": "Number of days to delete the resource files. If "
            "this parameter is set all resources older than this number of "
            "days will be deleted.",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
        },
    ],
    "responses": {
        "200": {
            "description": "Processing status of resource storage deletion",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message why resource storage cleaning "
            "did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
