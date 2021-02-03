#!/usr/bin/env python3
# coding=utf-8

import enum
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from pocketutils.core import SmartEnum
from pocketutils.tools.call_tools import CallTools
from pocketutils.tools.filesys_tools import FilesysTools
from pocketutils.tools.string_tools import StringTools

from sauronlab.core import SauronlabResources, log_factory, logger

ch = logging.StreamHandler()
logger.addHandler(ch)
ch.setFormatter(log_factory.formatter)
logger.setLevel(logging.INFO)


class SauronlabCmd(SmartEnum):
    """"""

    init = enum.auto()
    parrot = enum.auto()
    video = enum.auto()


class SauronlabProcessor:
    """"""

    def run(self, args) -> None:
        """


        Args:
            args:

        Returns:

        """
        import argparse

        parser = argparse.ArgumentParser("""Install, update, or initialize Sauronlab""")
        # noinspection PyTypeChecker
        parser.add_argument("cmd", type=SauronlabCmd.of, choices=[s for s in SauronlabCmd])
        parser.add_argument("args", nargs="*")
        opts = parser.parse_args(args)
        self.process(opts.cmd, opts.args)

    def process(self, cmd: SauronlabCmd, args) -> None:
        """


        Args:
            cmd: SauronlabCmd:
            args:

        Returns:

        """
        if cmd == SauronlabCmd.init:
            self.init()
        elif cmd == SauronlabCmd.video:
            self.download_video(args)
        else:
            print(SauronlabResources.text("art", cmd.name + ".txt"))

    # noinspection PyTypeChecker
    def init(self) -> None:
        """"""
        logger.notice("Setting up sauronlab configuration...")
        n_created = sum(
            [
                self._copy_if(
                    Path.home() / ".sauronlab" / "valar_config.json",
                    SauronlabResources.path("example_valar_config.json"),
                ),
                self._copy_if(
                    Path.home() / ".sauronlab" / "sauronlab.config",
                    SauronlabResources.path("example.sauronlab.config"),
                ),
                self._copy_if(
                    Path.home() / ".sauronlab" / "jupyter_template.txt",
                    SauronlabResources.path("jupyter_template.txt"),
                ),
                self._copy_if(
                    Path.home() / ".sauronlab" / "sauronlab.mplstyle",
                    SauronlabResources.path("styles/default.mplstyle"),
                ),
                self._copy_if(
                    Path.home() / ".sauronlab" / "sauronlab_viz.properties",
                    SauronlabResources.path("styles/basic.viz.properties"),
                ),
            ]
        )
        if n_created > 0:
            logger.notice("Finished. Edit these files as needed.")
        else:
            logger.notice("Finished. You already have all required config files.")

    def download_video(self, args):
        """


        Args:
            args:

        """
        from sauronlab.caches.video_caches import VideoCache

        cache = VideoCache()
        n_exists = sum([not cache.has_video(v) for v in args])
        for arg in args:
            cache.download(arg)
        logger.notice(f"Downloaded {n_exists} videos.")

    def _copy_if(self, dest: Path, source: Path) -> bool:
        """


        Args:
            dest: Path:
            source: Path:

        Returns:

        """
        import shutil

        if not dest.exists():
            # noinspection PyTypeChecker
            dest.parent.mkdir(parents=True, exist_ok=True)
            # noinspection PyTypeChecker
            shutil.copy(source, dest)
            logger.info(f"Copied {source} → {dest}")
            return True
        else:
            logger.info(f"Skipping {dest}")
            return False


def main():
    """"""
    # noinspection PyBroadException
    try:
        SauronlabProcessor().run(None)
    except Exception:
        logger.fatal("Failed while running command.", exc_info=True)


if __name__ == "__main__":
    main()

__all__ = ["SauronlabProcessor", "SauronlabCmd"]
