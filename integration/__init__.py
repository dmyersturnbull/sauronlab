import os
import sys
import inspect
import logging
import subprocess
from pathlib import Path
from typing import Optional

logger = logging.getLogger("SAURONLAB.TEST")
_root_user = "root"
_root_pwd = "root"


class Scaffold:
    _sauronlab_root: Optional[Path] = None
    _integration_root: Optional[Path] = None
    _module_root: Optional[Path] = None

    @classmethod
    def init(cls) -> __qualname__:
        cls._sauronlab_root = Path(__file__).parent.parent.absolute()
        cls._integration_root = Path(__file__).parent.absolute()
        # set path
        sys.path.insert(0, str(cls._sauronlab_root))
        # figure out which integration test we're in by reflection
        _stack = inspect.stack()[1]
        module_nodes = inspect.getmodule(_stack[0]).__name__.split(".")
        cls._module_root = (cls._integration_root / module_nodes[-2]).absolute()
        # set env vars
        cls.valarpy_config(cls._integration_root / "connection.json")
        cls.sauronlab_config(cls._module_root / "sauronlab.toml")
        return cls

    @classmethod
    def valarpy_config(cls, path: Path) -> __qualname__:
        os.environ["VALARPY_CONFIG"] = str(path)
        return cls

    @classmethod
    def sauronlab_config(cls, path: Path) -> __qualname__:
        os.environ["SAURONLAB_CONFIG"] = str(path)
        return cls

    @classmethod
    def load_db(cls) -> __qualname__:
        """
        Loads the schema .sql file (``testdb-schema.sql``).
        """
        cls.run_sql(cls._integration_root / "testdb-schema.sql")
        return cls

    @classmethod
    def load_rows(cls) -> __qualname__:
        """
        Loads all .sql files under the module path.
        """
        for path in cls._module_root.rglob("*.sql"):
            cls.run_sql(path)
        return cls

    @classmethod
    def connect(cls, write: bool = False) -> __qualname__:
        # connect via valarpy
        from sauronlab.core.valar_singleton import VALAR, Runs

        # noinspection PyProtectedMember
        db = VALAR.backend._peewee_database
        # make 100000% sure we're not on the real db
        if db.database != "kaletest":
            raise SystemError(f"Database is {db.database}, not 'kaletest'")
        if len(Runs.select()) > 10:
            raise SystemError(
                f"There are {len(Runs.select())} runs. Is this a production database?"
            )
        if write:
            VALAR.backend.enable_write()
        return cls

    @classmethod
    def run_sql(cls, path: Path) -> __qualname__:
        logger.info(f"Running {path}")
        subprocess.check_call(
            ["mysql", f"--user={_root_user}", f"--password={_root_pwd}", f"-e source {str(path)}"]
        )
        return cls


__all__ = ["logger", "Scaffold"]
