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
API docs for process_validation
"""

from actinia_core.core.common.process_chain import ProcessChainModel
from actinia_core.models.response_models import (
    ProcessingResponseModel,
    ProcessingErrorResponseModel,
)

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

DESCR = """Validate a process chain, check the provided sources (links)
and the mapsets. The list of processes that were checked by Actinia are
returned in the JSON response.
"""

post_doc = {
    "tags": ["Processing"],
    "description": DESCR,
    "consumes": ["application/json"],
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name that contains the data that "
            "should be used in the process chain",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "process_chain",
            "description": "The process chain that should be validated",
            "required": True,
            "in": "body",
            "schema": ProcessChainModel,
        },
    ],
    "responses": {
        "200": {
            "description": "The result of the process chain validation. "
            "A list of processes that will be executed by "
            "Actinia Core",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why process "
            "chain validation did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
