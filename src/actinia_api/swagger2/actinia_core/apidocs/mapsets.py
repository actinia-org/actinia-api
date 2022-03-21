# -*- coding: utf-8 -*-
#######
# actinia-core - an open source REST API for scalable, distributed, high
# performance processing of geographical data that uses GRASS GIS for
# computational tasks. For details, see https://actinia.mundialis.de/
#
# Copyright (c) 2021-2022 mundialis GmbH & Co. KG
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
API docs for mapsets
"""

from actinia_core.models.response_models import (
    LockedMapsetListResponseModel,
    SimpleResponseModel,
)

__license__ = "GPLv3"
__author__ = "Julia Haas, Guido Riembauer, Anika Weinmann"
__copyright__ = "Copyright 2021-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Mapsets"],
    "description": "List available or locked mapsets.",
    "parameters": [
        {
            "in": "path",
            "name": "mapsets",
            "type": "string",
            "description": "List all mapsets in the global database available "
            "to the authenticated user.",
        },
        {
            "in": "path",
            "name": "status",
            "type": "string",
            "description": (
                "If set to 'locked', list all locked mapsets across "
                "all locations. Minimum required user role: admin."
            ),
        },
        {
            "in": "path",
            "name": "user",
            "type": "string",
            "description": (
                "List all mapsets in the global database available "
                "to the specified user. "
                "Minimum required user role: admin"
            ),
        },
    ],
    "responses": {
        "200": {
            "description": "Returns a list of available (or locked) mapsets ",
            "schema": LockedMapsetListResponseModel,
        },
        "500": {
            "description": "The error message and a detailed error log",
            "schema": SimpleResponseModel,
        },
    },
}
