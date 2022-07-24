from setuptools import find_packages, setup

setup(
    name="m4i_atlas_core",
    version="0.1.0",
    author="Aurelius Enterprise",
    packages=find_packages(),
    install_requires=[
        "aiocache",
        "aiohttp",
        "dataclasses-json",
        "pandas"
        # "python-keycloak"
    ]
)
