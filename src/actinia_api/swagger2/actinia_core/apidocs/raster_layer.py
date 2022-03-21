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
API docs for raster_layer
"""

from actinia_core.models.response_models import (
    ProcessingResponseModel,
    ProcessingErrorResponseModel,
)

from actinia_api import URL_PREFIX
from actinia_api.swagger2.actinia_core.schemas.raster_layer import (
    RasterInfoResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Guido Riembauer, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Raster Management"],
    "description": "Get information about an existing raster map layer. "
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
            "description": "The name of the mapset that contains the required "
            "raster map layer",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
        {
            "name": "raster_name",
            "description": "The name of the raster map layer to get "
            "information about",
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
            "description": "The raster map layer information",
            "schema": RasterInfoResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "gathering raster map "
            "layer information did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

delete_doc = {
    "tags": ["Raster Management"],
    "description": "Delete an existing raster map layer. Minimum required "
    "user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset that contains the "
            "required raster map layer",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "raster_name",
            "description": "The name of the raster map layer to be deleted",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "Successfuly delete a raster map layer",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "raster map "
            "layer deletion did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

post_doc = {
    "tags": ["Raster Management"],
    "description": "Create a new raster map layer by uploading a GeoTIFF. "
    "This method will fail if the map already exists. "
    'An example request is \'curl -L -u "XXX:XXX" -X POST '
    '-H "Content-Type: multipart/form-data" -F '
    '"file=@/home/....tif" http://localhost:8088'
    f"{URL_PREFIX}/"
    "locations/nc_spm_08/mapsets/test_mapset/raster_layers/"
    "testraster'. Minimum required user role: user.",
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "mapset_name",
            "description": "The name of the mapset in which the raster map "
            "layer should be created",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "raster_name",
            "description": "The name of the new raster map layer to be "
            "created",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "consumes": ["Content-Type: multipart/form-data"],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "Raster map layer import information",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why raster "
            "map layer import failed",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
