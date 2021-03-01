from .. import Scaffold, logger

Scaffold.init().load_db().load_rows().connect()

from sauronlab.core.valar_singleton import *
from sauronlab.core.tools import Tools
from sauronlab.core.valar_tools import ValarTools


class TestMicro:
    def test_meta(self):
        users = list(Users.select())
        assert [user.username for user in users] == ["johnson", "annette"]

    def test_resources(self):
        solvents = ValarTools.known_solvent_names()
        assert solvents == {
            1: "water",
            2: "DMSO",
            3: "methanol",
            4: "ethanol",
            34330: "DMA",
            34492: "plutonium",
            34510: "M-Pyrol",
        }

    def test_controls_matching_all(self):
        matches = ValarTools.controls_matching_all()
        assert {m.name for m in matches} == {"neg", "pos", "gen-", "gen+"}
        matches = ValarTools.controls_matching_all(1)
        assert {m.name for m in matches} == {"neg"}
        matches = ValarTools.controls_matching_all([1, 2])
        assert {m.name for m in matches} == {"neg", "pos"}
        matches = ValarTools.controls_matching_all(positive=False)
        assert {m.name for m in matches} == {"neg", "gen-"}
        matches = ValarTools.controls_matching_all(positive=True)
        assert {m.name for m in matches} == {"pos", "gen+"}
        matches = ValarTools.controls_matching_all(positive=True, genetics_related=True)
        assert {m.name for m in matches} == {"gen+"}

    def test_controls_matching_any(self):
        matches = ValarTools.controls_matching_any()
        assert {m.name for m in matches} == {"neg", "pos", "gen-", "gen+"}
        matches = ValarTools.controls_matching_any(1)
        assert {m.name for m in matches} == {"neg"}
        matches = ValarTools.controls_matching_any([1, 2])
        assert {m.name for m in matches} == {"neg", "pos"}
        matches = ValarTools.controls_matching_any(positive=True, genetics_related=True)
        assert {m.name for m in matches} == {"pos", "gen-", "gen+"}
        matches = ValarTools.controls_matching_any("pos", genetics_related=True)
        assert {m.name for m in matches} == {"pos", "gen-", "gen+"}
