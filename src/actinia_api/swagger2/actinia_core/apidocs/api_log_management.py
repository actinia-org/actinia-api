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
API docs for api_log_management
"""

from actinia_api.swagger2.actinia_core.schemas.api_log_management import (
    ApiLogListModel,
)
from actinia_core.models.response_models import SimpleResponseModel

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"


get_doc = {
    "tags": ["API Log"],
    "description": "Get a list of all API calls that have been called by the "
    "provided user. Admin and superadmin roles can list API "
    "calls from any user. A user role can only list API calls "
    "from itself. "
    "Minimum required user role: user.",
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
            "description": "Returned a list of all API calls that have been "
            "called by the provided user.",
            "schema": ApiLogListModel,
        },
        "400": {
            "description": "The error message why API log gathering did not "
            "succeeded",
            "schema": SimpleResponseModel,
        },
    },
}
