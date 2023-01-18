from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customuserauth/__init__.py
from customuserauth import __version__ as version

setup(
	name="customuserauth",
	version=version,
	description="A custom user authentication app",
	author="samuel wakumelo",
	author_email="SamuelWaku1st@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
