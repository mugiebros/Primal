#!/usr/bin/env python3
import est_premier_seq
import sys
from multiprocessing import Process, Value
from typing import NoReturn, List
import math
import setproctitle
from typing import NoReturn, List
import colorama
from colorama import Fore
colorama.init()
import time
from timeit import default_timer as timer
"""
programme multi-process pour déterminer si un nombre est premier

2020, austin brodeur
"""
def exexit(ex: BaseException, exit_code: int = 2) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print(Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')

def est_premier_mp(nombre: int,rangnumb: int) -> None:
    """determine  si premier ou pas"""
    setproctitle.setproctitle(f"AB range({rangnumb}, {math.isqrt(nombre) + 1}, 8)")
    try:
        if nombre < 1:
            raise(ValueError("Le nombre doit être positif"))

        if nombre == 1:
            sys.exit(1)

        if nombre <= 3:
            sys.exit(0)

        if nombre % 2 == 0:
            sys.exit(1)
        racine = math.isqrt(nombre)

        for n in range(rangnumb, racine + 1,8):
                if nombre % n == 0:
                    sys.exit(1)
        sys.exit(0)
    except KeyboardInterrupt:
        pass
def main(argv: List[str]) -> None:
    début = timer()
    if int(''.join(argv[1:])) <= 100 or int(''.join(argv[1:])) % 2 == 0:
        est_premier_seq.main(argv)
    else:
        try:
            ps1 = Process(target=est_premier_mp,args=(int(''.join(argv[1:])),3))
            ps2 = Process(target=est_premier_mp, args=(int(''.join(argv[1:])), 5))
            ps3 = Process(target=est_premier_mp, args=(int(''.join(argv[1:])), 7))
            ps4 = Process(target=est_premier_mp, args=(int(''.join(argv[1:])), 9))
            ps1.start()
            print(" * pid ", ps1.pid, " -- range(", 3, ",", math.isqrt(int(''.join(argv[1:]))) + 1, ",", 8, ")")
            ps2.start()
            print(" * pid ", ps2.pid, " -- range(", 5, ",", math.isqrt(int(''.join(argv[1:]))) + 1, ",", 8, ")")
            ps3.start()
            print(" * pid ", ps3.pid, " -- range(", 7, ",", math.isqrt(int(''.join(argv[1:]))) + 1, ",", 8, ")")
            ps4.start()
            print(" * pid ", ps4.pid, " -- range(", 8, ",", math.isqrt(int(''.join(argv[1:]))) + 1, ",", 8, ")")
            ps1.join(5)
            ps2.join(5)
            ps3.join(5)
            ps4.join(5)
            if ps1.is_alive() or ps1.is_alive() or ps1.is_alive() or ps1.is_alive():
                raise TimeoutError(f"Le delai de {DELAI_SEC} secondes est écoulé")
            else:
                if ps1.exitcode == 0 and ps2.exitcode == 0 and ps3.exitcode == 0 and ps4.exitcode == 0:
                    print(Fore.CYAN + "Selon Austin Brodeur: " + Fore.RESET + "Oui")
                    print(Fore.YELLOW + "Durée:", timer() - début, "sec")
                else:
                    print(Fore.CYAN + "Selon Austin Brodeur: " + Fore.RESET + "Non")
                    print(Fore.YELLOW + "Durée:", timer() - début, "sec")
        except KeyboardInterrupt:
            exexit(KeyboardInterrupt("Interruption Clavier"))
            print(Fore.MAGENTA + "Durée:", timer() - début, "sec")
        except Exception as ex:
            exexit(ex)





if __name__ == '__main__':
    main(sys.argv)