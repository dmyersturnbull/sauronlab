from sauronlab.core._tools import *
from sauronlab.core.valar_singleton import *


class TestInternalTools:
    def test_well(self):
        well = Wells.fetch(1)
        print(well)
