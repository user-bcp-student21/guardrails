"""Nivel 1: comprobar la entrada antes de enviarla al agente."""

import argparse

from ejemplo import ENTRADA
from guardrails.input_check import validate_snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--caso", choices=("normal", "secreto"), default="normal")
    args = parser.parse_args()

    entrada = ENTRADA
    if args.caso == "secreto":
        entrada += "\nTOKEN_FICTICIO = 'ghp_" + "x" * 24 + "'\n"

    resultado = validate_snapshot(entrada)
    if not resultado.valid:
        print(f"BLOQUEADO: {resultado.reason}")
        return 1

    print("ENTRADA PERMITIDA. En el siguiente nivel llamaremos al agente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
