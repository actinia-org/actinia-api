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
API docs for vector_layer
"""

from actinia_core.models.response_models import (
    ProcessingErrorResponseModel,
    ProcessingResponseModel,
)

from actinia_api import URL_PREFIX
from actinia_api.swagger2.actinia_core.schemas.vector_layer import (
    VectorInfoResponseModel,
    VectorRegionCreationModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Guido Riembauer, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Vector Management"],
    "description": "Get information about an existing vector map layer. "
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
            "required vector map layer",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "PERMANENT",
        },
        {
            "name": "vector_name",
            "description": "The name of the vector map layer to get "
            "information about",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "boundary_county",
        },
    ],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "The vector map layer information",
            "schema": VectorInfoResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "gathering vector map layer information "
            "did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

delete_dop = {
    "tags": ["Vector Management"],
    "description": "Delete an existing vector map layer. "
    "Minimum required user role: user.",
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
            "required vector map layer",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "vector_name",
            "description": "The name of the vector map layer to be deleted",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "Successfully delete a vector map layer",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why vector "
            "map layer deletion did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

post_doc = {
    "tags": ["Vector Management"],
    "description": "Create a new vector map layer by uploading a GPKG, "
    "zipped Shapefile or GeoJSON. "
    "This method will fail if the map already exists. "
    'An example request is \'curl -L -u "XXX:XXX" -X POST '
    '-H "Content-Type: multipart/form-data" -F '
    '"file=@/home/....gpkg" http://localhost:8088'
    f"{URL_PREFIX}/"
    "locations/nc_spm_08/mapsets/test_mapset/vector_layers/"
    "testvector'. Minimum required user role: user.",
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
            "required vector map layer",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "vector_name",
            "description": "The name of the new vector map layer to be "
            "created.",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "creation_params",
            "description": "Parameters to create random vector point map "
            "layer in a specific region.",
            "required": True,
            "in": "body",
            "schema": VectorRegionCreationModel,
        },
    ],
    "consumes": ["Content-Type: multipart/form-data"],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "The vector map layer import information",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why "
            "vector map layer import failed",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
