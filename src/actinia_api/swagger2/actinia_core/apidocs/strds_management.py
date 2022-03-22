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
API docs for strds_management
"""

from actinia_core.models.response_models import (
    ProcessingErrorResponseModel,
    ProcessingResponseModel,
    StringListProcessingResultResponseModel,
)

from actinia_api.swagger2.actinia_core.schemas.strds_management import (
    STRDSCreationModel,
    STRDSInfoResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

list_get_doc = {
    "tags": ["STRDS Management"],
    "description": "Get a list of all STRDS that are located in a specific "
    "location/mapset. Minimum required user role: user.",
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
        {
            "name": "where",
            "description": "A where statement to select user specific STRDS",
            "required": False,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns a list of STRDS names and "
            "timestamps and the log of the process chain "
            "that was used to create the response.",
            "schema": StringListProcessingResultResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why listing "
            "of STRDS did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

get_doc = {
    "tags": ["STRDS Management"],
    "description": "Get information about a STRDS that is located in a "
    "specific location/mapset. "
    "Minimum required user role: user.",
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
        {
            "name": "strds_name",
            "description": "The name of the STRDS",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns information about a "
            "specific STRDS and the log of the process chain "
            "that was used to create the response.",
            "schema": STRDSInfoResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "information gathering of the STRDS did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

delete_doc = {
    "tags": ["STRDS Management"],
    "description": "Delete a STRDS that is located in a specific location/"
    "mapset. Minimum required user role: user.",
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
        {
            "name": "strds_name",
            "description": "The name of the STRDS",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "recursive",
            "description": "Delete the STRDS and all registered raster map "
            "layer recursively",
            "required": False,
            "in": "query",
            "type": "boolean",
        },
    ],
    "responses": {
        "200": {
            "description": "Deletion of the STRDS was successfully finished.",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "deletion of the STRDS did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

post_doc = {
    "tags": ["STRDS Management"],
    "description": "Create a new STRDS in a specific location/mapset. "
    "Minimum required user role: user.",
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
        {
            "name": "strds_name",
            "description": "The name of the STRDS",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "metadata",
            "description": "Temporal type, title and description of the STRDS",
            "required": True,
            "in": "body",
            "schema": STRDSCreationModel,
        },
    ],
    "responses": {
        "200": {
            "description": "Creation of the STRDS was successfully finished.",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "creation of the STRDS did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
