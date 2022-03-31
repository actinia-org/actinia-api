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
API docs for ephemeral_processing_with_export
"""

from actinia_core.models.response_models import (
    ProcessingResponseModel,
    ProcessingErrorResponseModel,
)
from actinia_core.core.common.process_chain import ProcessChainModel


__license__ = "GPLv3"
__author__ = "Sören Gebbert, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

DESCR = """Execute a user defined process chain in an ephemeral database
and provide the generated resources as downloadable files via URL's.
Minimum required user role: user.

The process chain is executed asynchronously. The provided status URL
in the response must be polled to gain information about the processing
progress and finishing status.

**Note**

    Make sure that the process chain definition identifies all raster, vector
    or space-time datasets correctly with name and mapset: name@mapset if you
    use data from other mapsets in the specified location.

    All required mapsets will be identified by analysing the input parameter
    of all module descriptions in the provided process chain and
    mounted read-only into the ephemeral database that is used for processing.

The persistent database will not be modified. The ephemeral database will be
removed after processing.
Use the URL's provided in the finished response to download the resource that
were specified in the process chain for export.

This endpoint also allows the creation of STAC ITEMS through the
ACTINIA STAC PLUGIN. The STAC item is stored in a dedicated
CATALOG following the standard from STAC specification (https://stacspec.org/).
"""

post_doc = {
    "tags": ["Processing"],
    "description": DESCR,
    "consumes": ["application/json"],
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name that contains the data that "
            "should be processed",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
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
            "description": "The result of the process chain execution",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why process "
            "chain execution did not succeeded",
            "schema": ProcessingErrorResponseModel,
        },
    },
}
