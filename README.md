# Nivel 1: guardrail de entrada

Un guardrail es una regla ejecutada por código. Si la entrada incumple la regla,
el programa se detiene antes de enviarla a un agente.

## Prueba

Necesitas Python 3.11 a 3.13. Este nivel no necesita instalar dependencias,
Copilot, `.env` ni GitHub. Ejecuta desde la raíz del repo:

```bash
python main.py
python main.py --caso secreto
```

El primer caso permite continuar. El segundo añade un token ficticio y termina
con `BLOQUEADO`. El secreto nunca se envía a un modelo; este nivel aún no llama
agentes. Si tu Python se llama `python3.12`, úsalo en los comandos.

## Lee el código

1. `ejemplo.py` contiene un código de tareas ficticio, igual para todos los niveles.
2. `main.py` llama a `validate_snapshot(entrada)`.
3. `guardrails/input_check.py` comprueba entrada vacía, tamaño y patrones de
   secretos o datos sensibles. Devuelve `valid` y `reason`.
4. Si `valid` es falso, el programa termina con código 1. Si es verdadero, continúa.

Cambia la entrada por texto vacío y observa qué regla falla. Estas reglas no
comprueban que el código funcione ni detectan todos los secretos posibles.

## Siguiente nivel

```bash
git switch nivel-2
git diff nivel-1..nivel-2 -- main.py
```

El recorrido completo es `nivel-1` entrada → `nivel-2` salida → `nivel-3` HITL →
`nivel-4` equipo completo. Cada rama conserva lo aprendido en la anterior.
Los agentes originales se mantienen intactos en `agents/`.

Para comprobar este nivel sin servicios:

```bash
python -m unittest discover -s tests -p test_niveles.py -v
```

El flujo avanzado de clonación y PR se conserva en `avanzado.py`.
Su preparación está en [EJECUCION.md](EJECUCION.md); no es necesario para este nivel.
