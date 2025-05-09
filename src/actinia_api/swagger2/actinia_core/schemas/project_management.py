# -*- coding: utf-8 -*-
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

"""
Models for project_management
"""

from flask_restful_swagger_2 import Schema

__license__ = "GPLv3"
__author__ = "Sören Gebbert, Carmen Tawalika, Anika Weinmann"
__copyright__ = (
    "Copyright 2016-2025, Sören Gebbert and mundialis GmbH & Co. KG"
)
__maintainer__ = "mundialis GmbH & Co. KG"

from actinia_core.version import init_versions, G_VERSION

init_versions()


class ProjectListResponseModel(Schema):
    """Response schema for projects lists"""

    type = "object"
    properties = {
        "status": {
            "type": "string",
            "description": "The status of the resource, values: accepted, "
            "running, finished, terminated, error",
        },
        "locations": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The list of projects in the GRASS database",
        },
        "projects": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The list of projects in the GRASS database",
        },
    }
    example = {
        "locations": ["nc_spm_08", "latlong_wgs84", "ECAD"],
        "projects": ["nc_spm_08", "latlong_wgs84", "ECAD"],
        "status": "success",
    }
    grass_version_s = G_VERSION["version"]
    grass_version = [int(item) for item in grass_version_s.split(".")[:2]]
    if grass_version < [8, 4]:
        required = ["status", "locations"]
    else:
        required = ["status", "projects"]


class ProjectionInfoModel(Schema):
    """Schema to define projection information as JSON input in POST requests"""

    type = "object"
    properties = {
        "epsg": {
            "type": "string",
            "description": "The EPSG code of the projection that should be used "
            "to create a project",
        }
    }
    example = {"epsg": "4326"}
    required = ["epsg"]
