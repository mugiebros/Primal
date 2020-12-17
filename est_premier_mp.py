#!/usr/bin/env python3
import est_premier_seq
import sys
import multiprocessing as mp
from multiprocessing import Process, Value
from typing import NoReturn, List
import math
import argparse
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
def parse_arg() -> argparse.Namespace:
    """
    parse les arguments
    """
    parser = argparse.ArgumentParser(description="Commande de nombres premiers -- @2020, Par Austin Brodeur")
    parser.add_argument('nombre', help='nombre à traiter pour connaitre sa primalité', nargs='?',type=int)
    parser.add_argument('-d', '--délai',metavar='DÉLAI', help='delai du calcul (Défaut 10 sec)',default=10)
    parser.add_argument('-e', '--explication',metavar='', help="Expliquer pourquoi non premier")
    parser.add_argument('-p', '--processus', type=int, metavar='PROCESSUS',default=mp.cpu_count(),
                        help='nombres de processus à utiliser')
    parser.add_argument('-t','--tarce',action='store_true',help="Activer la trace d'éxecution")
    parser.add_argument('-q','--quiet',action='store_true',help="Ne pas afficher les processus")

    args = parser.parse_args()
    return args

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
    parse_arg()
    processus = []
    if parse_arg().nombre <= 100 or parse_arg().nombre % 2 == 0:
        est_premier_seq.main(argv)
    else:
        try:
            process = parse_arg().processus
            rendu = 3
            ouiounon = True
            if parse_arg().processus == 0:
                process = mp.cpu_count()
            if parse_arg().processus < 0:
                process = mp.cpu_count() + parse_arg().processus
            for i in range(0,process):
                pro = Process(target=est_premier_mp, args=(parse_arg().nombre, rendu))
                pro.start()
                processus.append(pro)
                rendu+=2
            rendu = 3
            for i in processus:
                i.join(parse_arg().délai)
                if not parse_arg().quiet:
                    print(" * pid ", i.pid, " -- range(", rendu, ",", math.isqrt(parse_arg().nombre) + 1, ",", 8,
                            ")")
                if i.is_alive():
                    raise TimeoutError(f"Le delai de {parse_arg().délai} secondes est écoulé")
                if i.exitcode == 1:
                    ouiounon = False
                rendu+=3

            if ouiounon:
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