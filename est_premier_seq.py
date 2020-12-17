#!/usr/bin/env python3

"""
programme sequentielle pour déterminer si un nombre est premier

2020, austin brodeur
"""
import math
import sys
from typing import NoReturn
import colorama
from colorama import Fore
colorama.init()
from timeit import default_timer as timer
def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporter une erreur et terminer le programme"""
    print("\n",Fore.YELLOW,"[AB] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def est_premier_séq(nombre: int) -> bool:
    """determine  si premier ou pas"""
    if nombre < 1:
        raise(ValueError("Le nombre doit être positif"))

    if nombre == 1:
        return False

    if nombre <= 3:
        return True

    if nombre % 2 == 0:
        return False
    racine = math.isqrt(nombre)

    for n in range(3, racine + 1,2):
            if nombre % n == 0:
                return False
    return True
def main() -> None:
    début = timer()
    """Fonction principale"""
    if len(sys.argv[1:]) <= 0:
        exexit(IndexError("La commande doit avoir au moins un argument"))
    try:
        if est_premier_séq(int(''.join(sys.argv[1:]))):
            print(Fore.CYAN + "Selon Austin Brodeur: "+Fore.RESET+"Oui")
            print(Fore.YELLOW + "Durée:",timer() - début, "sec")
        else:
            print(Fore.CYAN + "Selon Austin Brodeur: " + Fore.RESET + "Non")
            print(Fore.YELLOW + "Durée:",timer() - début, "sec")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Durée:", timer() - début, "sec")
        exexit(KeyboardInterrupt("Interruption clavier"))
    except BaseException as ex:
        exexit(ex)





if __name__ == '__main__':
    main()