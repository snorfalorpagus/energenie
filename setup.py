#!/usr/bin/env python

from setuptools import setup

setup(
    name="Energenie",
    version="1.0",
    description="CLI for the Energenie Pi-Mote",
    author="Joshua Arnott",
    author_email="josh@snorfalorpagus.net",
    packages=["energenie"],
    scripts=["scripts/energenie"]
)
