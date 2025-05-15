#######
# actinia-core - an open source REST API for scalable, distributed, high
# performance processing of geographical data that uses GRASS GIS for
# computational tasks. For details, see https://actinia.mundialis.de/
#
# Copyright (c) 2016-2025 Sören Gebbert and mundialis GmbH & Co. KG
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

"""API docs for project_management."""

from actinia_core.models.response_models import (
    MapsetInfoResponseModel,
    ProcessingResponseModel,
    SimpleResponseModel,
)

from actinia_api.swagger2.actinia_core.schemas.project_management import (
    ProjectionInfoModel,
    ProjectListResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2016-2025, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

get_doc = {
    "tags": ["Project Management"],
    "description": "Get a list of all available projects that are located in "
    "the GRASS database and the user has access to. Minimum required "
    "user role: user.",
    "responses": {
        "200": {
            "description": "This response returns a list of project names",
            "schema": ProjectListResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}

get_user_doc = {
    "tags": ["Project Management"],
    "description": "Get the project projection and current computational "
    "region of the PERMANENT mapset. Minimum required user "
    "role: user.",
    "parameters": [
        {
            "name": "project_name",
            "description": "The name of the project",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        }
    ],
    "responses": {
        "200": {
            "description": "The project projection and current computational "
            "region of the PERMANENT mapset",
            "schema": MapsetInfoResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": ProcessingResponseModel,
        },
    },
}

delete_user_doc = {
    "tags": ["Project Management"],
    "description": "Delete an existing project and everything inside from the"
    " user database. Minimum required user role: user.",
    "parameters": [
        {
            "name": "project_name",
            "description": "The name of the project to be deleted",
            "required": True,
            "in": "path",
            "type": "string",
        }
    ],
    "responses": {
        "200": {
            "description": "Success message for project deletion",
            "schema": SimpleResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": SimpleResponseModel,
        },
    },
}

post_user_doc = {
    "tags": ["Project Management"],
    "description": "Create a new project based on EPSG code in the user "
    "database. Minimum required user role: user.",
    "consumes": ["application/json"],
    "parameters": [
        {
            "name": "project_name",
            "description": "The name of the project to be created",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "epsg_code",
            "description": "The EPSG code",
            "required": True,
            "in": "body",
            "schema": ProjectionInfoModel,
        },
    ],
    "responses": {
        "200": {
            "description": "Create a new project based on EPSG code",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message",
            "schema": ProcessingResponseModel,
        },
    },
}
