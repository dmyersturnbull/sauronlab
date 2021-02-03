"""
Sets up standard imports and settings for Sauronlab.
"""
import os

from pocketutils.logging.warning_utils import *

################################
# set up warnings
################################


__filterer = (
    GlobalWarningUtils.init()
    .filter_common_numeric()
    .substring_once("Number of features and number of timestamps differ by 1")
)

################################
# set up logger for Jupyter
################################
import logging

from sauronlab.core import log_factory, logger
from sauronlab.core.environment import sauronlab_env

logging.getLogger("chemspipy").setLevel(logging.WARNING)
logging.getLogger("url_query").setLevel(logging.WARNING)

import traceback
from collections import OrderedDict, namedtuple

################################
# external imports
################################
from decimal import Decimal
from io import StringIO
from tempfile import NamedTemporaryFile, TemporaryDirectory, TemporaryFile

# external packages
import joblib
import matplotlib
import matplotlib.gridspec as gridspec
import seaborn as sns
import sklearn
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from natsort import natsorted
from pocketutils.biochem.multiwell_plates import *

# pocketutils
from pocketutils.core import frozenlist
from pocketutils.core.dot_dict import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC

from sauronlab.analysis.auto_analyses import *
from sauronlab.analysis.mandos_searches import *

# analysis
from sauronlab.analysis.phenosearches import *
from sauronlab.caches.audio_caches import *
from sauronlab.caches.caching_wfs import *

# caches
from sauronlab.caches.sensor_caches import *
from sauronlab.caches.stim_caches import *
from sauronlab.caches.wf_caches import *

# core
from sauronlab.core.core_imports import *
from sauronlab.core.tools import *
from sauronlab.lookups.fuzzy import *

# lookups
from sauronlab.lookups.layouts import *
from sauronlab.lookups.lookups import *
from sauronlab.lookups.mandos import *
from sauronlab.lookups.submissions import *
from sauronlab.lookups.templates import *

# ml
from sauronlab.ml import ClassifierPath
from sauronlab.ml.accuracy_frames import *
from sauronlab.ml.classifiers import *
from sauronlab.ml.confusion_matrices import *
from sauronlab.ml.decision_frames import *
from sauronlab.ml.multi_trainers import *
from sauronlab.ml.spindles import *
from sauronlab.ml.transformers import *

# model
from sauronlab.model import *
from sauronlab.model.app_frames import *
from sauronlab.model.well_names import *
from sauronlab.model.assay_frames import *
from sauronlab.model.audio import *
from sauronlab.model.case_control_comparisons import *
from sauronlab.model.compound_names import *
from sauronlab.model.concerns import *
from sauronlab.model.features import *
from sauronlab.model.metrics import *
from sauronlab.model.plate_frames import *
from sauronlab.model.responses import *
from sauronlab.model.roi_tools import *
from sauronlab.model.sensors import *
from sauronlab.model.stim_frames import *
from sauronlab.model.treatment_names import *
from sauronlab.model.treatments import *
from sauronlab.model.well_frames import *
from sauronlab.model.well_names import *
from sauronlab.model.wf_builders import *
from sauronlab.model.wf_tools import WellFrameColumns

# root
from sauronlab.quick import *
from sauronlab.viz import plt
from sauronlab.viz.accuracy_plots import *
from sauronlab.viz.breakdown_plots import *
from sauronlab.viz.confusion_plots import *
from sauronlab.viz.figures import *

# viz
from sauronlab.viz.heatmaps import *
from sauronlab.viz.importance_plots import *
from sauronlab.viz.kvrc import KvrcDefaults, sauronlab_rc
from sauronlab.viz.response_plots import *
from sauronlab.viz.stim_plots import *
from sauronlab.viz.timeline_plots import *
from sauronlab.viz.trace_plots import *
from sauronlab.viz.well_plots import *

################################
# package overrides
################################

# and this was reset
logging.getLogger().setLevel(sauronlab_env.global_log_level)

# I don't know why this needs to happen twice
__filterer.substring_never(".*libuv only supports.*")

# numexpr's default is 8, which is excessive for most applications
# let's keep it between 1 and min(6, nCPU-1)
# setting this has the advantage of silencing the "NumExpr defaulting to 8 threads." logging
os.environ.setdefault("NUMEXPR_MAX_THREADS", str(max(1, min(6, os.cpu_count() - 1))))


################################
# startup messages
################################

logger.notice(
    f"Sauronlab version {sauronlab_version.strip()}. Started in {round(time.monotonic() - sauronlab_start_clock)}s."
)
logger.debug(f"Figure dimensions: {sauronlab_rc.height}×{sauronlab_rc.width}")
logger.info("Severity key: " + Severity.key_str())
logger.debug(f"Using backend  {matplotlib.get_backend()}")
