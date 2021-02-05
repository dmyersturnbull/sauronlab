#!/usr/bin/env python3
# coding=utf-8

import enum
import logging
from pathlib import Path
from typing import List

import typer
from pocketutils.core import SmartEnum

from sauronlab.core import SauronlabResources, log_factory, logger

ch = logging.StreamHandler()
logger.addHandler(ch)
ch.setFormatter(log_factory.formatter)
logger.setLevel(logging.INFO)


cli = typer.Typer()


class SauronlabProcessor:
    """"""

    @staticmethod
    @cli.command()
    def init() -> None:
        """
        Initialize.

        """
        logger.notice("Setting up sauronlab configuration...")
        n_created = sum(
            [
                SauronlabProcessor._copy_if(
                    Path.home() / ".sauronlab" / "valar_config.json",
                    SauronlabResources.path("example_valar_config.json"),
                ),
                SauronlabProcessor._copy_if(
                    Path.home() / ".sauronlab" / "sauronlab.config",
                    SauronlabResources.path("example.sauronlab.config"),
                ),
                SauronlabProcessor._copy_if(
                    Path.home() / ".sauronlab" / "jupyter_template.txt",
                    SauronlabResources.path("jupyter_template.txt"),
                ),
                SauronlabProcessor._copy_if(
                    Path.home() / ".sauronlab" / "sauronlab.mplstyle",
                    SauronlabResources.path("styles/default.mplstyle"),
                ),
                SauronlabProcessor._copy_if(
                    Path.home() / ".sauronlab" / "sauronlab_viz.properties",
                    SauronlabResources.path("styles/basic.viz.properties"),
                ),
            ]
        )
        if n_created > 0:
            logger.notice("Finished. Edit these files as needed.")
        else:
            logger.notice("Finished. You already have all required config files.")

    @staticmethod
    @cli.command()
    def dl(runs: List[str]):
        """
        Downloads runs with videos.

        Args:
            runs: Run IDs

        """
        from sauronlab.caches.video_caches import VideoCache

        cache = VideoCache()
        n_exists = sum([not cache.has_video(v) for v in runs])
        for arg in runs:
            cache.download(arg)
        logger.notice(f"Downloaded {n_exists} videos.")

    @staticmethod
    def _copy_if(dest: Path, source: Path) -> bool:
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


if __name__ == "__main__":
    cli()


__all__ = ["SauronlabProcessor"]
