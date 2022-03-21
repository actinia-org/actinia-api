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
API docs for raster_colors
"""

from actinia_core.models.response_models import (
    ProcessingResponseModel,
    ProcessingErrorResponseModel,
    StringListProcessingResultResponseModel,
)

from actinia_api.swagger2.actinia_core.schemas.raster_colors import (
    RasterColorModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Raster Management"],
    "description": "Get the color definition of an existing raster map layer. "
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
            "required raster map layer",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "raster_name",
            "description": "The name of the raster map layer to get the "
            "color table from",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "produces": ["application/json"],
    "responses": {
        "200": {
            "description": "A list of color rules",
            "schema": StringListProcessingResultResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingErrorResponseModel,
        },
    },
}


post_doc = {
    "tags": ["Raster Management"],
    "description": "Set the color definition for an existing raster map "
    "layer. Minimum required user role: user.",
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
            "description": "The name of the raster map layer to set the "
            "color table",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "color",
            "description": "The color definition.",
            "required": True,
            "in": "body",
            "schema": RasterColorModel,
        },
    ],
    "produces": ["application/json"],
    "consumes": ["application/json"],
    "responses": {
        "200": {
            "description": "Successfuly set the color table for a raster map "
            "layer",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed error log",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
