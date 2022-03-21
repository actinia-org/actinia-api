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
API docs for map_layer_management
"""

from actinia_core.models.response_models import (
    ProcessingResponseModel,
    StringListProcessingResultResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

raster_get_doc = {
    "tags": ["Raster Management"],
    "description": "Get a list of raster map layer names that are located "
    "in a specific location/mapset."
    " Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location that should be accessed",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset from which the raster "
            "map layers should be listed",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
        {
            "name": "pattern",
            "description": "A parameter passed to g.list for raster map"
            ' layer selection, eg.: http://<url>?pattern="*"',
            "required": False,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns a list of raster map layers "
            "and the log of the process chain that was used to "
            "create the response.",
            "schema": StringListProcessingResultResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why listing "
            "of raster map layers did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}

raster_put_doc = {
    "tags": ["Raster Management"],
    "description": "Rename a single raster map layer or a list of raster "
    "map layers that are located in a specific location/mapset. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location that should be accessed",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset from which the raster "
            "map layers should be renamed",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "rename_list",
            "description": "A list of raster name tuples [(a, a_new),"
            "(b, b_new),(c, c_new), ...]",
            "required": True,
            "in": "body",
            "schema": {"type": "string"},
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns the log of the process "
            "chain that was used to create the response.",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why listing "
            "of raster map layers did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}

raster_delete_doc = {
    "tags": ["Raster Management"],
    "description": "Delete a single raster map layer or a list of raster "
    "map layer names that are located in a specific "
    "location/mapset. Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location that should be accessed",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset from which the raster map "
            "layers should be deleted",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "pattern",
            "description": "A parameter passed for g.remove to remove a list "
            "of raster map layers, to remove all eg.: "
            'http://<url>?pattern="*"',
            "required": False,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns the log of the process chain"
            " that was used to create the response.",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why deletion "
            "of raster map layers did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}

vector_get_doc = {
    "tags": ["Vector Management"],
    "description": "Get a list of vector map layer names that are located "
    "in a specific location/mapset."
    " Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location that should be accessed",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset from which the vector map "
            "layers should be listed",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
        {
            "name": "pattern",
            "description": "A parameter passed to g.list for vector map"
            ' layer selection, eg.: http://<url>?pattern="*"',
            "required": False,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns a list of vector map layers "
            "and the log of the process chain that was used "
            "to create the response.",
            "schema": StringListProcessingResultResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why listing "
            "of vector map layers did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}

vector_put_doc = {
    "tags": ["Vector Management"],
    "description": "Rename a single vector map layer or a list of vector "
    "map layers that are located in a specific "
    "location/mapset. Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location that should be accessed",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset from which the vector "
            "map layers should be renamed",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "rename_list",
            "description": "A list of vector name tuples [(a, a_new),"
            "(b, b_new),(c, c_new), ...]",
            "required": True,
            "in": "body",
            "schema": {"type": "string"},
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns the log of the process chain"
            " that was used to create the response.",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why listing "
            "of vector map layers did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}

vector_delete_doc = {
    "tags": ["Vector Management"],
    "description": "Delete a single vector map layer or a list of vector "
    "map layer names that are located in a specific "
    "location/mapset. Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The name of the location that should be accessed",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset from which the vector "
            "map layers should be deleted",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "pattern",
            "description": "A parameter passed for g.remove to remove a "
            "list of vector map layers, to remove all eg.: "
            'http://<url>?pattern="*"',
            "required": False,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns the log "
            "of the process chain that was used to create "
            "the response.",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why deletion "
            "of vector map layers did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}
