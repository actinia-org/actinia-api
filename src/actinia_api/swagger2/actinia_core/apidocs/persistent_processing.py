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
API docs for ephemeral_processing
"""

from actinia_core.core.common.process_chain import ProcessChainModel
from actinia_core.models.response_models import ProcessingResponseModel

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Guido Riembauer, Anika Weinmann"
__copyright__ = "Copyright 2016-2022, mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

DESCR = """Execute a user defined process chain in an existing mapset
of the persistent user database or in a new mapset that will be
created by this request in the persistent user database.

The process chain is executed asynchronously. The provided status URL
in the response must be polled to gain information about the processing
progress and finishing status.

**Note**

    Space-time dataset processing can only be performed in a new mapset
    that is created by this resource call, since merging of temporal databases
    of different mapsets is not supported yet.

The mapset that is used for processing will be locked until the process
chain execution finished (successfully or not), even if the mapset is be
created by the request.
Other requests on the locked mapset will abort with a mapset lock error.

The persistent user database will not be modified if
the process chain does not run successfully. The processing is performed in an
ephemeral database and then merged or copied into the persistent user database.

**Note**

    Make sure that the process chain definition identifies all raster, vector
    or space time datasets correctly with name and mapset: name@mapset.

    All required mapsets will be identified by analysing the input parameter
    of all module descriptions in the provided process chain
    and mounted into the ephemeral database that is used for processing.

"""

post_doc = {
    "tags": ["Processing"],
    "description": DESCR,
    "consumes": ["application/json"],
    "parameters": [
        {
            "name": "location_name",
            "description": "The location name",
            "required": True,
            "in": "path",
            "type": "string",
            "default": "nc_spm_08",
        },
        {
            "name": "mapset_name",
            "description": "The name of an existing mapset or a new mapset "
            "that should be created",
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
            "description": "The result of the process chain execution",
            "schema": ProcessingResponseModel,
        },
        "400": {
            "description": "The error message and a detailed log why process "
            "chain execution did not succeed",
            "schema": ProcessingResponseModel,
        },
    },
}
