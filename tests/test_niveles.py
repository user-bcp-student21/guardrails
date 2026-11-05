"""Comprueba la interfaz del nivel actual sin modelo ni servicios externos."""

from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


class NivelTests(unittest.TestCase):
    def ejecutar(self, *args, respuesta=""):
        return subprocess.run(
            [sys.executable, "main.py", *args], input=respuesta,
            text=True, capture_output=True, cwd=ROOT, timeout=20,
        )

    def test_entrada_permitida(self):
        resultado = self.ejecutar()
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("ENTRADA PERMITIDA", resultado.stdout)

    def test_secreto_bloquea(self):
        resultado = self.ejecutar("--caso", "secreto")
        self.assertEqual(resultado.returncode, 1, resultado.stderr)
        self.assertIn("BLOQUEADO", resultado.stdout)
        self.assertNotIn("ENTRADA PERMITIDA", resultado.stdout)
