import os
import orjson
import logging
from pathlib import Path
from subprocess import check_call, DEVNULL
from typing import List
import random

import typer

from sauronlab.core import SauronlabResources, log_factory, logger

ch = logging.StreamHandler()
logger.addHandler(ch)
ch.setFormatter(log_factory.formatter)
logger.setLevel(logging.INFO)

MAIN_DIR = os.environ.get("SAURONLAB_DIR", Path.home() / ".sauronlab")
cli = typer.Typer()


class Installer:
    """"""

    def __init__(self):
        self.n_created = 0

    def init(self) -> None:
        """
        Initializes.

        """
        typer.echo("Setting up sauronlab configuration...")
        conn_file, config_file = MAIN_DIR / "connection.json", MAIN_DIR / "sauronlab.config"
        if not conn_file.exists():
            typer.echo("No connection.json detected. Asking for that info:")
            rand = random.randint(49152, 65535)
            conn = dict(
                database="valar",
                user=typer.prompt("connection username", type=str),
                password=typer.prompt("connection password", type=str),
                host=typer.prompt("connection hostname", type=str, default="127.0.0.1"),
                port=typer.prompt(
                    f"connection port (49152–65535) [how about: {rand}?]", type=int, default=3306
                ),
            )
            conn_file.write_bytes(orjson.dumps(conn, option=orjson.OPT_INDENT_2))
            self.n_created += 1
        if not config_file.exists():
            typer.echo("No sauronlab.config detected. Asking for that info:")
            user = typer.prompt("username in valar.users (e.g. 'john')", type=str)
            shire_path = typer.prompt(
                "Path to video store (e.g. '/shire' or 'none')", default="none"
            )
            tunnel_host = typer.prompt("Remote hostname for SSH tunnel", default="valinor")
            tunnel_port = typer.prompt("Remote port for tunnel (49152–65535)", default="3306")
            data = (
                SauronlabResources.path("templates", "sauronlab.config")
                .read_text(encoding="utf8")
                .replace("$${user}", user)
                .replace("$${shire}", str(shire_path))
                .replace("$${tunnel_host}", tunnel_host)
                .replace("$${tunnel_port}", str(tunnel_port))
            )
            if shire_path is None:
                data = data.replace("shire_path = none", "")
            config_file.write_text(data)
            self.n_created += 1
        self._copy_if(
            MAIN_DIR / "jupyter.txt",
            SauronlabResources.path("templates", "jupyter.txt"),
        )
        self._copy_if(
            MAIN_DIR / "sauronlab.mplstyle",
            SauronlabResources.path("styles", "default.mplstyle"),
        )
        self._copy_if(
            MAIN_DIR / "sauronlab_viz.properties",
            SauronlabResources.path("styles", "default.properties"),
        )
        if self.n_created > 0:
            typer.echo("Finished. Edit these files as needed.")
        else:
            typer.echo("Finished. You already have all required config files.")

    def _copy_if(self, dest: Path, source: Path) -> None:
        import shutil

        if dest.exists():
            typer.echo(f"Skipped {dest}")
            return
        # noinspection PyTypeChecker
        dest.parent.mkdir(parents=True, exist_ok=True)
        # noinspection PyTypeChecker
        shutil.copy(source, dest)
        typer.echo(f"Copied {source} → {dest}")
        self.n_created += 1


class Commands:
    @staticmethod
    @cli.command()
    def init() -> None:
        Installer().init()

    @staticmethod
    @cli.command()
    def tunnel() -> None:
        from pocketutils.tools.filesys_tools import FilesysTools

        config = FilesysTools.read_properties_file(MAIN_DIR / "sauronlab.config")
        vpy = orjson.loads((MAIN_DIR / "connection.json").read_text(encoding="utf8"))
        if "tunnel_host" not in config or "tunnel_port" not in config:
            raise ValueError(f"Tunnel host or port in sauronlab.config missing")
        host, port = vpy["host"], vpy["port"]
        remote_host, remote_port = config["tunnel_host"], config["tunnel_port"]
        # ssh -L 53419:localhost:3306 valinor.ucsf.edu
        typer.echo("Tunneling into valar...")
        cmd = ["ssh", "-L", f"{port}:{host}:{remote_port}", remote_host]
        typer.echo(f"Running: {' '.join(cmd)}")
        try:
            check_call(cmd, stdout=DEVNULL)  # nosec
        finally:
            typer.echo("Closed tunnel to valar.")

    @staticmethod
    @cli.command()
    def dl(runs: List[str]) -> None:
        """
        Downloads runs with videos.

        Args:
            runs: Run IDs

        """
        from sauronlab.extras.video_caches import VideoCache

        cache = VideoCache()
        n_exists = sum([not cache.has_video(v) for v in runs])
        for arg in runs:
            cache.download(arg)
        logger.notice(f"Downloaded {n_exists} videos.")


if __name__ == "__main__":
    cli()


__all__ = ["Commands"]
