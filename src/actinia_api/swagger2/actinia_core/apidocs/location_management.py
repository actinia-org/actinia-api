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
API docs for location_management
"""

from actinia_core.models.response_models import (
    MapsetInfoResponseModel,
    ProcessingResponseModel,
    SimpleResponseModel,
)
from actinia_api.swagger2.actinia_core.schemas.location_management import (
    LocationListResponseModel,
)
from actinia_api.swagger2.actinia_core.schemas.location_management import (
    ProjectionInfoModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Location Management"],
    "description": "Get a list of all available locations that are located in "
    "the GRASS database and the user has access to. Minimum required "
    "user role: user.",
    "responses": {
        "200": {
            "description": "This response returns a list of location names",
            "schema": LocationListResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}

get_user_doc = {
    "tags": ["Location Management"],
    "description": "Get the location projection and current computational "
    "region of the PERMANENT mapset. Minimum required user "
    "role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        }
    ],
    "responses": {
        "200": {
            "description": "The location projection and current computational "
            "region of the PERMANENT mapset",
            "schema": MapsetInfoResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": ProcessingResponseModel,
        },
    },
}

delete_user_doc = {
    "tags": ["Location Management"],
    "description": "Delete an existing location and everything inside from the"
    " user database. Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location to be deleted",
            "required": True,
            "in": "path",
            "type": "string",
        }
    ],
    "responses": {
        "200": {
            "description": "Success message for location deletion",
            "schema": SimpleResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}

post_user_doc = {
    "tags": ["Location Management"],
    "description": "Create a new location based on EPSG code in the user "
    "database. Minimum required user role: user.",
    "consumes": ["application/json"],
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location to be created",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "epsg_code",
            "description": "The EPSG code",
            "required": True,
            "in": "body",
            "schema": ProjectionInfoModel,
        },
    ],
    "responses": {
        "200": {
            "description": "Create a new location based on EPSG code",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": ProcessingResponseModel,
        },
    },
}
