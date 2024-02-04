from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bulk_message/__init__.py
from bulk_message import __version__ as version

setup(
	name="bulk_message",
	version=version,
	description="bulk message",
	author="tejal",
	author_email="tejal.kumbhar@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
