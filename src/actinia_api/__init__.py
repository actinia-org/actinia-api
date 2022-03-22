from pkg_resources import get_distribution, DistributionNotFound

API_VERSION = "v3"

# This is the URL prefix that must be used in the tests
URL_PREFIX = "/api/%s" % API_VERSION

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
