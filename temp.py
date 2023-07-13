from letsbuilda.pypi.distributions import read_distribution_tarball
from requests import Session
from letsbuilda.pypi import PyPIServices

http_session = Session()
pypi_client = PyPIServices(http_session)

# print(pypi_client.get_rss_feed(pypi_client.NEWEST_PACKAGES_FEED_URL))
# print(pypi_client.get_package_metadata("letsbuilda-pypi"))

_bytes = pypi_client.fetch_package_distribution(
    "https://files.pythonhosted.org/packages/71/a0/d9b47f7a17efb1d296d189ae83c5381c80efa0e0984a96cb2f719136797e/letsbuilda-pypi-4.0.0.tar.gz")
print(read_distribution_tarball(_bytes))
