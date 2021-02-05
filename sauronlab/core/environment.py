from pocketutils.tools.filesys_tools import FilesysTools

from sauronlab.core import log_factory
from sauronlab.core._imports import *
from sauronlab.core.valar_singleton import *

# I really don't understand why this is needed here
for handler in logging.getLogger().handlers:
    handler.setFormatter(log_factory.formatter)

MAIN_DIR = Path.home() / ".sauronlab"
CONFIG_PATH = os.environ.get("SAURONLAB_CONFIG", MAIN_DIR / "sauronlab.config")
if CONFIG_PATH is None:
    raise FileDoesNotExistError(f"No config file at {CONFIG_PATH}")
VIZ_PATH = (
    MAIN_DIR / "sauronlab_viz.properties"
    if (MAIN_DIR / "sauronlab_viz.properties").exists()
    else SauronlabResources.path("styles", "default.properties")
)


@abcd.auto_repr_str()
@abcd.auto_eq(exclude=None)
@abcd.auto_info()
class SauronlabEnvironment:
    """
    A collection of settings for Sauronlab.
    Python files in Sauronlab use this singleton class directly.
    This is loaded from a file in the user's home directory at ~/sauronlab.config.

    Attributes:
        - username: The username in valar.users; no default
        - cache_dir: The location of the top-level cache path; defaults to ~/valar-cache
        - video_cache_dir:  The location of the cache for videos; defaults to  ~/valar-cache/videos
        - shire_path: The local or remote path to the Shire (raw data storage); by default this a location on Valinor
        - audio_waveform: Sauronlab will **save** StimFrame objects to the cache with audio waveforms; Enabling this will cause audio_waveform= arguments to be always true
        - matplotlib_style: The path to a Matplotlib stylesheet; defaults to Matplotlib default
        - use_multicore_tsne: Enable the multicore_tsne package
        - joblib_compression_level: Used in joblib.dump compress parameter if the filename ends with one of (‘.z’, ‘.gz’, ‘.bz2’, ‘.xz’ or ‘.lzma’); 3 by default
        - sauronlab_log_level: The log level recommended to be used for logging statements within Sauronlab; set up by jupyter.py
        - global_log_level: The log level recommended to be used for logging statements globally; set up by jupyter.py
        - viz_file: Path to sauronlab-specific visualization options in the style of Matplotlib RC
        - n_cores: Default number of cores for some jobs, including with parallelize()
        - jupyter_template: Path to a Jupyter template text file

    """

    def __init__(self):
        """"""
        self.config_file = Path(CONFIG_PATH).expanduser()
        if not self.config_file.exists():
            raise MissingResourceError(f"No config file at path {self.config_file}")
        props = self._get_props()

        def _try(key: str, fallback=None):
            return props.get(key, fallback)

        self.home = Path(__file__).parent.parent
        self.username = _try("username")
        if self.username is None:
            raise MissingConfigKeyError(f"Must specify username in {self.config_file}")
        self.user = Users.fetch(self.username)
        self.user_ref = Refs.fetch_or_none("manual:" + self.username)
        if self.user_ref is None:
            logger.warning(f"manual:{self.username} is not in `refs`. Using 'manual'.")
        self.user_ref = Refs.fetch_or_none("manual")
        self.sauronlab_log_level = _try("sauronlab_log_level", "MINOR")
        self.global_log_level = _try("global_log_level", "INFO")
        self.cache_dir = _try("cache", Path.home() / "valar-cache")
        self.video_cache_dir = Path(
            _try("video_cache", Path(self.cache_dir, "videos")).expanduser()
        )
        self.shire_path = _try("shire_path", "valinor:/shire/")
        self.audio_waveform = CommonTools.parse_bool(_try("save_with_audio_waveform", False))
        self.matplotlib_style = Path(
            _try("matplotlib_style", SauronlabResources.path("styles", "default.mplstyle"))
        ).expanduser()
        self.use_multicore_tsne = CommonTools.parse_bool(_try("multicore_tsne", False))
        self.joblib_compression_level = int(_try("joblib_compression_level", 3))
        self.n_cores = int(_try("n_cores", 1))
        self.jupyter_template = Path(
            _try("jupyter_template", SauronlabResources.path("jupyter_template.txt"))
        ).expanduser()
        self.viz_file = Path(_try("viz_file", VIZ_PATH)).expanduser()
        if not self.viz_file.exists():
            raise MissingResourceError(f"No viz file at path {self.viz_file}")
        self._adjust_logging()
        logger.info(f"Read {self.config_file} .")
        self.cache_dir.mkdir(exist_ok=True, parents=True)
        logger.info(
            f"Set {len(props)} sauronlab config items. Run 'print(sauronlab_env.info())' for details."
        )

    def _get_props(self):
        """ """
        try:
            props = {
                k: v.strip("\t '\"")
                for k, v in FilesysTools.read_properties_file(self.config_file).items()
            }
        except ParsingError as e:
            raise MissingConfigKeyError(f"Bad sauronlab config file {self.config_file}") from e
        return props

    def _adjust_logging(self):
        """ """
        logger.setLevel(self.sauronlab_log_level)
        logging.getLogger(self.global_log_level)
        logger.info(
            f"Set global log level to {self.global_log_level} and sauronlab to {self.sauronlab_log_level}."
        )


sauronlab_env = SauronlabEnvironment()

__all__ = ["SauronlabEnvironment", "sauronlab_env"]
