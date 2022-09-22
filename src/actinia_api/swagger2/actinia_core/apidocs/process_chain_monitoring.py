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
API docs for process_chain_monitoring
"""

from actinia_core.models.response_models import SimpleResponseModel

from actinia_api.swagger2.actinia_core.schemas.process_chain_monitoring import (
    MapsetSizeResponseModel,
    MaxMapsetSizeResponseModel,
)


__license__ = "GPLv3"
__author__ = "Anika Weinmann, Carmen Tawalika"
__copyright__ = "Copyright 2021-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

mapset_size_get_doc = {
    "tags": ["Process Chain Monitoring"],
    "description": "Get the mapset sizes of a resource. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "resource_id",
            "description": "The id of the resource",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "The current state of the resource",
            "schema": MapsetSizeResponseModel,
        },
        "400": {
            "description": "The error message if the resource does not exist",
            "schema": SimpleResponseModel,
        },
    },
}

mapset_sizediff_get_doc = {
    "tags": ["Process Chain Monitoring"],
    "description": "Get the step-by-step mapset size differences of a "
    "resource. Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "resource_id",
            "description": "The id of the resource",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "The current state of the resource",
            "schema": MapsetSizeResponseModel,
        },
        "400": {
            "description": "The error message if the resource does not exists",
            "schema": SimpleResponseModel,
        },
    },
}

mapset_maxsize_get_doc = {
    "tags": ["Process Chain Monitoring"],
    "description": "Get the maximum mapset size of a resource. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "resource_id",
            "description": "The id of the resource",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "The current state of the resource",
            "schema": MaxMapsetSizeResponseModel,
        },
        "400": {
            "description": "The error message if the resource does not exist",
            "schema": SimpleResponseModel,
        },
    },
}

mapset_render_sizes_get_doc = {
    "tags": ["Process Chain Monitoring"],
    "description": "Render the mapset sizes of a resource. "
    "Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "resource_id",
            "description": "The id of the resource",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "produces": ["image/png"],
    "responses": {
        "200": {"description": "The PNG image"},
        "400": {
            "description": "The error message and a detailed log why "
            "rendering did not succeed",
            "schema": SimpleResponseModel,
        },
    },
}

mapset_render_sizediff_get_doc = {
    "tags": ["Process Chain Monitoring"],
    "description": "Render the step-by-step mapset size differences of a "
    "resource. Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "resource_id",
            "description": "The id of the resource",
            "required": True,
            "in": "path",
            "type": "string",
        },
    ],
    "produces": ["image/png"],
    "responses": {
        "200": {"description": "The PNG image"},
        "400": {
            "description": "The error message and a detailed log why "
            "rendering did not succeed",
            "schema": SimpleResponseModel,
        },
    },
}
