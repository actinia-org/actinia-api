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
API docs for raster_export
"""

from actinia_core.models.response_models import (
    ProcessingResponseModel,
    ProcessingErrorResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

post_doc = {
    "tags": ["Raster Management"],
    "description": "Export an existing raster map layer as GTiff or COG "
    "(if COG driver available). The link to the exported "
    "raster map layer is located in the JSON response."
    "The current region settings of the mapset are used to "
    "export the raster layer. Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset that contains the "
            "required raster map layer",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
        {
            "name": "raster_name",
            "description": "The name of the raster map layer to export",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "elevation",
        },
    ],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "The response including the URL to the raster "
            "map layer GeoTiff file",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why"
            " gathering raster map layer information did "
            "not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

region_post_doc = {
    "tags": ["Raster Management"],
    "description": "Export an existing raster map layer as GTiff or COG "
    "(if COG driver available). The link to the exported "
    "raster map layer is located in the JSON response. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset that contains the "
            "required raster map layer",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
        {
            "name": "raster_name",
            "description": "The name of the raster map layer to export",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "elevation",
        },
    ],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "The response including the URL to the raster "
            "map layer GeoTiff file",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "gathering raster map layer information did "
            "not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
