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
API docs for resource_management
"""

from actinia_core.core.common.process_chain import ProcessChainModel
from actinia_core.models.response_models import (
    ProcessingResponseListModel,
    ProcessingResponseModel,
    SimpleResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

resource_get_doc = {
    "tags": ["Resource Management"],
    "description": "Get the status of a resource. Minimum required user "
    "role: user.",
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
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message if the resource does not exists",
            "schema": SimpleResponseModel,
        },
    },
}

resource_put_doc = {
    "tags": ["Resource Management"],
    "description": "Updates/Resumes the status of a failed resource. This "
    "assumes that 'save_interim_results' is configured. "
    "The job will restart at the step before the failed one and "
    "execute these steps in the possibly corrected process chain sent along "
    "with it. If 'save_interim_results' is set to 'True' the temporary mapset"
    " is saved before the failed step and the resumption should work without "
    "any problem. But if 'save_interim_results' is set to 'onError' the "
    "temporary mapset is only saved if an error occurs and so the mapset "
    "may contain changes from the failed step what may make resumption "
    "difficult or impossible. In the event of such an error, the process chain"
    " can then be adjusted so that the missing data is generated again, or the"
    " entire process can be started as a new job."
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
        {
            "name": "process_chain",
            "description": "The process chain that should be executed",
            "required": True,
            "in": "body",
            "schema": ProcessChainModel,
        },
    ],
    "responses": {
        "200": {
            "description": "The current state of the resource",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message if the resource does not exists",
            "schema": SimpleResponseModel,
        },
    },
}

resource_delete_doc = {
    "tags": ["Resource Management"],
    "description": "Request the termination of a resource. "
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
            "description": "Returned if termination request of the resource "
            "was successfully committed. "
            "Be aware that this does not mean, that the "
            "resource was successfully terminated.",
            "schema": SimpleResponseModel,
        },
        "400": {
            "description": "The error message why resource storage "
            "information gathering did not succeeded",
            "schema": SimpleResponseModel,
        },
    },
}

resources_get_doc = {
    "tags": ["Resource Management"],
    "description": "Get a list of resources that have been generated by the "
    "specified user. Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        },
        {
            "name": "num",
            "description": "The maximum number of jobs that should be "
            "returned",
            "required": False,
            "in": "query",
            "type": "integer",
        },
        {
            "name": "type",
            "description": "The type of job that should be returned: "
            "accepted, running, error, terminated, finished",
            "required": False,
            "in": "query",
            "type": "string",
        },
    ],
    "responses": {
        "200": {
            "description": "Returned a list of resources that have been "
            "generated by the specified user.",
            "schema": ProcessingResponseListModel,
        },
        "401": {
            "description": "The error message why resource gathering did "
            "not succeeded",
            "schema": SimpleResponseModel,
        },
    },
}

resources_delete_doc = {
    "tags": ["Resource Management"],
    "description": "Terminate all accepted and running resources of the "
    "specified user. Minimum required user role: user.",
    "parameters": [
        {
            "name": "user_id",
            "description": "The unique user name/id",
            "required": True,
            "in": "path",
            "type": "string",
        }
    ],
    "responses": {
        "200": {
            "description": "Termination requests have been successfully "
            "committed. Be aware that does not mean, that "
            "the resources have been successfully terminated.",
            "schema": SimpleResponseModel,
        },
        "401": {
            "description": "The error message why the resource termination "
            "did not succeeded",
            "schema": SimpleResponseModel,
        },
    },
}

resource_iteration_get_doc = {
    "tags": ["Resource Iteration Management"],
    "description": "Get the status of a resource with the iterations. "
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
        {
            "name": "iteration",
            "description": "The id of the resource",
            "required": True,
            "in": "path",
            "type": "integer",
        },
    ],
    "responses": {
        "200": {
            "description": "The current state of the resource",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message if the resource does not exists",
            "schema": SimpleResponseModel,
        },
    },
}
