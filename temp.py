from requests import Session
from letsbuilda.pypi import PyPIServices

http_session = Session()
pypi_client = PyPIServices(http_session)

# print(pypi_client.get_rss_feed(pypi_client.NEWEST_PACKAGES_FEED_URL))
print(pypi_client.get_package_metadata("letsbuilda-pypi"))
