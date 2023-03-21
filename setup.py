from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in space_secure/__init__.py
from space_secure import __version__ as version

setup(
	name="space_secure",
	version=version,
	description="Space Secure Dashboard",
	author="MalekQumboz",
	author_email="malek.h.qumboz@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
