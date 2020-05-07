import os.path
import re

from setuptools import find_packages, setup

requirements_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements', 'requirements.txt')
requirements_test_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'requirements',
    'requirements_test.txt'
)


def get_requirments(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
    return re.findall(r"[A-Za-z][A-Za-z0-9\-\.]+==[0-9\.\-A-Za-z]*", data)


requirements = get_requirments(requirements_path)
requirements_test = get_requirments(requirements_test_path)


setup(
    name="simple_application",
    description="Simple application",
    version="0.0.1",
    install_requires=requirements,
    zip_safe=False,
    packages=find_packages(),
    extras_require={"dev": requirements_test, "test": requirements_test},
    platforms="Python 3.7 and later.",
)
