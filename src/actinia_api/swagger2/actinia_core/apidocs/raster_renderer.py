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
API docs for raster_renderer
"""

from actinia_core.models.response_models import (
    ProcessingErrorResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

raster_render_get_doc = {
    "tags": ["Raster Management"],
    "description": "Render a raster map layer as a PNG image. "
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
            "description": "The name of the raster map layer to render",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "elevation",
        },
        {
            "name": "n",
            "description": "Northern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "s",
            "description": "Southern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "e",
            "description": "Eastern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "w",
            "description": "Western border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "width",
            "description": "Image width in pixel, default is 800",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
            "default": 800,
        },
        {
            "name": "height",
            "description": "Image height in pixel, default is 600",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
            "default": 600,
        },
    ],
    "produces": ["image/png"],
    "responses": {
        "200": {"description": "The PNG image"},
        "400": {
            "description": "The error message and a detailed log why "
            "rendering did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

raster_rgb_render_get_doc = {
    "tags": ["Raster Management"],
    "description": "Render three raster map layer as composed RGB PNG image. "
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
            "default": "landsat",
        },
        {
            "name": "red",
            "description": "The name of the raster map layer to render "
            "as color red",
            "required": True,
            "in": "query",
            "type": "string",
            "default": "lsat5_1987_30",
        },
        {
            "name": "green",
            "description": "The name of the raster map layer to render as "
            "color green",
            "required": True,
            "in": "query",
            "type": "string",
            "default": "lsat5_1987_20",
        },
        {
            "name": "blue",
            "description": "The name of the raster map layer to render as "
            "color blue",
            "required": True,
            "in": "query",
            "type": "string",
            "default": "lsat5_1987_10",
        },
        {
            "name": "n",
            "description": "Northern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "s",
            "description": "Southern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "e",
            "description": "Eastern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "w",
            "description": "Western border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "width",
            "description": "Image width in pixel, default is 800",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
            "default": 800,
        },
        {
            "name": "height",
            "description": "Image height in pixel, default is 600",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
            "default": 600,
        },
    ],
    "produces": ["image/png"],
    "responses": {
        "200": {"description": "The RGB composition PNG image"},
        "400": {
            "description": "The error message and a detailed log why "
            "rendering did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}

raster_shade_render_get_doc = {
    "tags": ["Raster Management"],
    "description": "Render two raster layers as a composed shade PNG image. "
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
            "name": "shade",
            "description": "The name of the raster map layer to be used "
            "for shading",
            "required": True,
            "in": "query",
            "type": "string",
            "default": "aspect",
        },
        {
            "name": "color",
            "description": "The name of the raster map layer to be used for "
            "coloring",
            "required": True,
            "in": "query",
            "type": "string",
            "default": "elevation",
        },
        {
            "name": "n",
            "description": "Northern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "s",
            "description": "Southern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "e",
            "description": "Eastern border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "w",
            "description": "Western border",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "double",
        },
        {
            "name": "width",
            "description": "Image width in pixel, default is 800",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
            "default": 800,
        },
        {
            "name": "height",
            "description": "Image height in pixel, default is 600",
            "required": False,
            "in": "query",
            "type": "number",
            "format": "integer",
            "default": 600,
        },
    ],
    "produces": ["image/png"],
    "responses": {
        "200": {"description": "The shade/color composition PNG image"},
        "400": {
            "description": "The error message and a detailed log why "
            "rendering did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
