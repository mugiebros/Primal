"""
utilitaires partagés entre les fichiers de test
"""

import re
from typing import Callable, List

PREMIERS = [2, 3, 5, 7, 11, 13, 43, 97, 101, 1009, 9901, 10007]
COMPOSÉS = [1, 4, 6, 9, 15, 49, 99, 1849, 10201, 55698]
PREMIER_TRES_LONG = 1_000_000_000_000_000_003               # 40 sec sur ma machine
PREMIER_TROP_LONG = 11_111_111_111_111_111_111_111          # Très très long

# From: https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
ANSI_ESCAPE = re.compile(r'''
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
''', re.VERBOSE)


def capt_main(mainfn: Callable[[List[str]], None], capsys, args: str) -> (str, str, int):
    """
    Évalue la fonction main et capture stdout et stderr

    Le retour est en minuscules et purgé des séquences de coloriage ANSI.

    Retourne la capture de stdout, stderr et l'exitcode
    """
    exit_code = None
    try:
        mainfn(["test", *(args.split(' ') if args else [])])
    except SystemExit as ex:
        exit_code = ex.code
    captured = capsys.readouterr()
    out = ANSI_ESCAPE.sub('', captured.out.lower())
    err = ANSI_ESCAPE.sub('', captured.err.lower())
    print(out)
    if err:
        print('--------------- stderr ---------------')
        print(err)
    return out, err, exit_code


def vérifier_range(out: str, upto: int, nombre: int) -> None:
    """
    Vérifier que les ranges afficher pour chaque processus sont corrects
    Le nombre de ranges est le nombre de processus.
    """
    if nombre < 100 or nombre % 2 == 0:
        assert "range" not in out
    else:
        compte = (upto - 1) // 2
        upto += 2
        for i in range(3, upto, 2):
            assert f"range({i}" in out
        assert f"range({upto}" not in out
        assert compte == out.count("range(")
