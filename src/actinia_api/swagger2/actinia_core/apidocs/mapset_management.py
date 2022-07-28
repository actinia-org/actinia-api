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
API docs for mapset_management
"""

from actinia_core.models.response_models import (
    MapsetInfoResponseModel,
    ProcessingResponseModel,
    ProcessingErrorResponseModel,
    StringListProcessingResultResponseModel,
)

from actinia_api.swagger2.actinia_core.schemas.mapset_management import (
    MapsetLockManagementResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Mapset Management"],
    "description": "Get a list of all mapsets that are located in a "
    "specific location. "
    "Minimum required user role: user.",
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
            "description": "This response returns a list of mapset names "
            "and the log of the process chain that was used "
            "to create the response.",
            "schema": StringListProcessingResultResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why listing "
            "of mapsets did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

get_user_doc = {
    "tags": ["Mapset Management"],
    "description": "Get the current computational region of the mapset and the"
    " projection of the location as WKT string. Minimum required "
    "user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
    ],
    "responses": {
        "200": {
            "description": "The current computational region of the "
            "mapset and the projection of the location",
            "schema": MapsetInfoResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

post_user_doc = {
    "tags": ["Mapset Management"],
    "description": "Create a new mapset in an existing location. Minimum "
    "required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "Success message for mapset creation",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

delete_user_doc = {
    "tags": ["Mapset Management"],
    "description": "Delete an existing mapset. Minimum required user role:"
    " user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "Success message for mapset deletion",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

get_lock_doc = {
    "tags": ["Mapset Management"],
    "description": "Get the location/mapset lock status. "
    "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
    ],
    "responses": {
        "200": {
            "description": "Get the location/mapset lock status, either "
            '"True" or "None"',
            "schema": MapsetLockManagementResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingResponseModel,
        },
    },
}

post_lock_doc = {
    "tags": ["Mapset Management"],
    "description": "Create a location/mapset lock. A location/mapset lock can "
    "be created so that no operation can be performed on it "
    "until it is unlocked. "
    "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
    ],
    "responses": {
        "200": {
            "description": "Success message if the location/mapset was "
            "locked successfully",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingResponseModel,
        },
    },
}

delete_lock_doc = {
    "tags": ["Mapset Management"],
    "description": "Delete a location/mapset lock. A location/mapset lock "
    "can be deleted so that operation can be performed on "
    "it until it is locked. "
    "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
    ],
    "responses": {
        "200": {
            "description": "Success message if the location/mapset was "
            "unlocked successfully",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingResponseModel,
        },
    },
}
