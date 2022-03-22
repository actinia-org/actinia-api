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
API docs for user_api_key
"""

from actinia_api.swagger2.actinia_core.schemas.user_api_key import (
    TokenResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

apikey_get_doc = {
    "tags": ["Authentication Management"],
    "description": "Create an API key for permanent authentication. "
    "API keys have no expiration time. "
    "Minimum required user role: admin.",
    "responses": {
        "200": {
            "description": "The API key generation response",
            "schema": TokenResponseModel,
        },
        "400": {
            "description": "The error message in case of failure",
            "schema": TokenResponseModel,
        },
    },
}

token_get_doc = {
    "tags": ["Authentication Management"],
    "description": "Create an authentication token. Tokens have an "
    "expiration time. The default expiration time is one day "
    "(86400s). maximum length is 365 days. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "expiration_time",
            "description": "The expiration time in seconds for the generated "
            "token.",
            "required": False,
            "in": "query",
            "type": "integer",
            "default": 86400,
        }
    ],
    "responses": {
        "200": {
            "description": "The token generation response",
            "schema": TokenResponseModel,
        },
        "400": {
            "description": "The error message in case of failure",
            "schema": TokenResponseModel,
        },
    },
}
