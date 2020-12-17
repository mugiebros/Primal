"""
Pour tester la partie 2 de l'exercice
"""

import pytest
from test_util import capt_main, PREMIERS, COMPOSÉS, vérifier_range
from est_premier_mp import main


@pytest.mark.parametrize("candidat", PREMIERS)
def test_candidat_premier(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert "oui" in out
    assert "non" not in out
    vérifier_range(out, 9, candidat)
    assert err == ""


@pytest.mark.parametrize("candidat", COMPOSÉS)
def test_candidat_composé(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert "non" in out
    assert "oui" not in out
    vérifier_range(out, 9, candidat)
    assert err == ""


@pytest.mark.parametrize("candidat", [0, -1, -99])
def test_candidat_zéro_ou_moins(capsys, candidat):
    out, err, code = capt_main(main, capsys, str(candidat))
    assert out == ""
    assert "valueerror" in err
    assert "doit être > 0" in err
