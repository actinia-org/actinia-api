"""actinia-api.
=========
actinia-api is a RESTful API for the actinia framework. It provides a
web service interface to the actinia framework, which is a geospatial
processing framework based on the GRASS GIS software. The API allows
users to access and manipulate geospatial data, run processing tasks,
and manage the underlying GRASS GIS environment.
"""

import importlib.metadata

API_VERSION = "v3"

# This is the URL prefix that must be used in the tests
URL_PREFIX = f"/api/{API_VERSION}"

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = importlib.metadata.version(dist_name)
except Exception:
    __version__ = "unknown"
