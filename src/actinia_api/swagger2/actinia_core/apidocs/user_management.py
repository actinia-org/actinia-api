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
API docs for user_management
"""

from actinia_core.models.response_models import (
    UserInfoResponseModel,
    UserListResponseModel,
    SimpleResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

user_list_get_doc = {
    "tags": ["User Management"],
    "description": "Get a list of all users. "
    "Minimum required user role: admin.",
    "responses": {
        "200": {
            "description": "This response returns a list of user names.",
            "schema": UserListResponseModel,
        }
    },
}

user_get_doc = {
    "tags": ["User Management"],
    "description": "Get information about the group, role and permissions "
    "of a certain user. "
    "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "user",
            "description": "The unique name of the user",
            "required": True,
            "in": "path",
            "type": "string",
        }
    ],
    "responses": {
        "200": {
            "description": "This response returns information about a "
            "certain user.",
            "schema": UserInfoResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}

user_post_doc = {
    "tags": ["User Management"],
    "description": "Creates a new user in the database. "
    "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique name of the user",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "password",
            "description": "The password of the new user",
            "required": True,
            "in": "query",
            "type": "string",
        },
        {
            "name": "group",
            "description": "The group of the new user",
            "required": True,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "This response returns the status of user "
            "creation.",
            "schema": SimpleResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}

user_delete_doc = {
    "tags": ["User Management"],
    "description": "Deletes a user. " "Minimum required user role: admin.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique name of the user",
            "required": True,
            "in": "path",
            "type": "string",
        }
    ],
    "responses": {
        "200": {
            "description": "This response returns the status of user "
            "deletion.",
            "schema": SimpleResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}
