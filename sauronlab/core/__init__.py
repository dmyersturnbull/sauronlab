"""
Contains the lowest-level code in Sauronlab.
This package cannot not depend on any other packages in Sauronlab.
"""

from __future__ import annotations

import time
import warnings
from datetime import datetime
from pathlib import Path

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

# ###
# This works around problems with orjson
# It requires the Rust toolchain, which may not be installed
# ###

try:
    import orjson

    class Json:
        @staticmethod
        def to_str(obj: dict) -> str:
            return orjson.dumps(obj, option=orjson.OPT_INDENT_2).decode(encoding="utf8")

        @staticmethod
        def from_str(s: str) -> dict:
            return orjson.loads(s)

        @staticmethod
        def to_file(obj: dict, path: Path) -> None:
            path.write_bytes(orjson.dumps(obj, option=orjson.OPT_INDENT_2))

        @staticmethod
        def from_file(path: Path) -> dict:
            return orjson.loads(path.read_text(encoding="utf8"))


except ImportError:
    logger.error(f"Cannot import orjson. This may cause problems.")
    logger.debug(f"Cannot import orjson. This may cause problems.", exc_info=True)
    import json

    class Json:
        @staticmethod
        def to_str(obj: dict) -> str:
            return json.dumps(obj, indent=2)

        @staticmethod
        def from_str(s: str) -> dict:
            return json.loads(s)

        @staticmethod
        def to_file(obj: dict, path: Path) -> None:
            with path.open("w") as f:
                json.dump(obj, f, ensure_ascii=False, indent=2)

        @staticmethod
        def from_file(path: Path) -> dict:
            return json.loads(path.read_text(encoding="utf8"))


__all__ = [
    "sauronlab_version",
    "sauronlab_start_time",
    "sauronlab_start_clock",
    "LogLevel",
    "SauronlabResources",
    "logger",
    "log_factory",
    "Json",
]
