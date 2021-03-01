"""
Contains the lowest-level code in Sauronlab.
This package cannot not depend on any other packages in Sauronlab.
"""

from __future__ import annotations

import enum
import logging
import os
import time
import warnings
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime
from functools import total_ordering
from pathlib import Path
from typing import Generator, Mapping, Union

from pocketutils.logging.fancy_logger import *
from pocketutils.logging.log_format import *

from sauronlab import version as sauronlab_version

warnings.filterwarnings(
    action="ignore",
    message=".*Monkey-patching ssl after ssl has already been imported may lead to errors.*",
)


class SauronlabResources:
    """ """

    @classmethod
    def path(cls, *parts) -> Path:
        """


        Args:
            *parts:

        Returns:

        """
        return Path(Path(__file__).parent.parent, "resources", *parts)

    @classmethod
    def text(cls, *parts) -> str:
        """


        Args:
            *parts:

        Returns:

        """
        return SauronlabResources.path(*parts).read_text(encoding="utf8")

    @classmethod
    def binary(cls, *parts) -> bytes:
        """


        Args:
            *parts:

        Returns:

        """
        return SauronlabResources.path(*parts).read_bytes()


LogLevel.initalize()
logger = AdvancedLogger.create("sauronlab")
log_factory = PrettyRecordFactory(10, 12, 5, width=100, symbols=True).modifying(logger)
logger.setLevel("INFO")  # good start; can be changed

sauronlab_start_time = datetime.now()
sauronlab_start_clock = time.monotonic()

__all__ = [
    "sauronlab_version",
    "sauronlab_start_time",
    "sauronlab_start_clock",
    "LogLevel",
    "SauronlabResources",
    "logger",
    "log_factory",
]
