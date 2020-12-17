"""
Pour tester la partie 1 de l'exercice
"""

import pytest
from test_util import capt_main, PREMIERS, COMPOSÉS
from est_premier_seq import main


@pytest.mark.parametrize("candidat", PREMIERS)
def test_candidat_premier(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert "oui" in out
    assert "non" not in out
    assert err == ""


@pytest.mark.parametrize("candidat", COMPOSÉS)
def test_candidat_composé(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert "non" in out
    assert "oui" not in out
    assert err == ""


def test_aucun_arg(capsys):
    out, err, code = capt_main(main, capsys, "")
    assert out == ""
    assert "indexerror" in err
    assert "au moins un argument" in err


@pytest.mark.parametrize("candidat", [0, -1, -99])
def test_candidat_zéro_ou_moins(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert out == ""
    assert "valueerror" in err
    assert "doit être positif" in err


@pytest.mark.parametrize("candidat", ["45x", 3.14])
def test_candidat_entier(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert out == ""
    assert "valueerror" in err
    assert "invalid literal for int" in err
