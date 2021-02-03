"""

"""
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

from sauronlab import __version__
from sauronlab.startup import *

(
    MagicTemplate.from_path(sauronlab_env.jupyter_template)
    .add_version(__version__)
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
