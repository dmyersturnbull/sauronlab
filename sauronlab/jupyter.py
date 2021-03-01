"""

"""
import logging
import sys

# In jupyterlab, all logging gets directed to stderr and is displayed with a red background
# The styling appears to come from codemirror
# Regardless, showing all output in red is really distracting and hard to read
# So, we'll split so that only warning and higher get sent to stderr
logging.getLogger().setLevel(30)
logging.getLogger("sauronlab").setLevel(15)
for __handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(__handler)
_to_stdout = logging.StreamHandler(sys.stdout)
_to_stdout.setLevel(10)
_to_stdout.addFilter(
    lambda record: record.levelno < 30 or record.levelno == 35 and record.msg != "%s"
)
_to_stderr = logging.StreamHandler(sys.stderr)
_to_stderr.setLevel(10)
# We could set the level to 30, but it could get reset later
# based on the sauronlab config
# Instead, set the level of the logger (for both handlers) in the config
# But always filter based on < / >= 30 with Filters
# Also filter out the NOTICE level
_to_stderr.addFilter(
    lambda record: record.levelno >= 30 and record.levelno != 35 and record.msg != "%s"
)
logging.getLogger().addHandler(_to_stdout)
logging.getLogger().addHandler(_to_stderr)

import IPython
from IPython.display import HTML, Markdown, display
from pandas.plotting import register_matplotlib_converters
from pocketutils.notebooks.j import J, JFonts

from sauronlab.core.core_imports import *
from sauronlab.startup import *

pd.Series.reverse = pd.DataFrame.reverse = lambda self: self[::-1]
from pocketutils.notebooks.magic_template import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from sauronlab import version
from sauronlab.startup import *

(
    MagicTemplate.from_path(sauronlab_env.jupyter_template)
    .add_version(version)
    .add_datetime()
    .add("username", sauronlab_env.username)
    .add("author", sauronlab_env.username.title())
    .add("config", sauronlab_env.config_file)
).register_magic("sauronlab")

J.full_width()
# noinspection PyTypeChecker
display(HTML("<style>.container { width:100% !important; }</style>"))
logger.debug("Set Jupyter & Pandas display options")


def _plot_all(it: Iterable[Tup[str, Figure]]) -> None:
    """

    Args:
        it:
    """
    for name, figure in it:
        print(f"Plotting {name}")
        plt.show(figure)


plt.show_all = _plot_all

Namers = WellNamers
Cols = WellFrameColumns

register_matplotlib_converters()
