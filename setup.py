import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    raise Exception("Only Python 3.6+ is supported")

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="drf_kafka_logger",
    version="1.0.0",
    author="VertCapital",
    author_email="caiofaria@vert-capital.com",
    description="Logger to consumer kafka",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vert-capital/drf-kafka-logger",
    packages=find_packages(
        exclude=["ez_setup", "examples", "tests", "release"]),
    install_requires=[
        "Django>=2.0",
        "django_kafka @ git+https://github.com/vert-capital/django_kafka.git",
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
