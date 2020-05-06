from setuptools import find_packages, setup

setup(
    name="simple_application",
    description="Simple application",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "aiocache==0.11.1",
        "aiohttp==3.5.4",
        "asyncio==3.4.3",
        "click==7.0",
        "sanic==18.12.0",
    ],
    extras_require={
        "test": [
            "asynctest==0.13.0",
            "flake8==3.5.0",
            "flake8-import-order==0.17.1",
            "pytest==4.3.1",
            "pytest-sanic==1.6.1"
        ]
    },
    test_suite="nose.collector",
    platforms="Python 3.7 and later.",
)
