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
API docs for download_cache_management
"""

from actinia_core.models.response_models import (
    StorageResponseModel,
    ProcessingResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"


get_doc = {
    "tags": ["Cache Management"],
    "description": "Get the current size of the download cache. "
    "Minimum required user role: admin.",
    "responses": {
        "200": {
            "description": "The current state of the download cache",
            "schema": StorageResponseModel,
        },
        "400": {
            "description": "The error message why cache information "
            "gathering did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}


delete_doc = {
    "tags": ["Cache Management"],
    "description": "Clean the download cache and remove all cached data. "
    "Minimum required user role: admin.",
    "responses": {
        "200": {
            "description": "Processing status of cache deletion",
            "schema": StorageResponseModel,
        },
        "400": {
            "description": "The error message why cache cleaning did not succeeded",
            "schema": ProcessingResponseModel,
        },
    },
}
