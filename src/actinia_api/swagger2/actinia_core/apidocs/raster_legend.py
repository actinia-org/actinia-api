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
API docs for raster_legend
"""

from actinia_core.models.response_models import (
    ProcessingErrorResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Raster Management"],
    "description": "Render the legend of a raster map layer as a PNG image. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "project_name",
            "description": "The project name",
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
            "description": "The name of the raster map layer of which the "
            "legend should be rendered",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "elevation",
        },
    ],
    "produces": ["image/png"],
    "responses": {
        "200": {"description": "The PNG image"},
        "400": {
            "description": "The error message and a detailed log why legend "
            "rendering did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
