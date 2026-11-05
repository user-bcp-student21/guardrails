# Ejecutar con agentes y un producto

Este laboratorio lee el código de un producto, propone cambios con los agentes
de `agents/` y abre un PR. Tú revisas y apruebas cada etapa.

Necesitas dos repositorios: este contiene los agentes; el de producto contiene
el código que quieres modificar.

## El recorrido del laboratorio

Trabajen con un solo issue pequeño, por ejemplo rechazar títulos vacíos al crear
tareas. El objetivo es completar ese cambio y comprobarlo en el producto.

| Momento | Quién | Qué entrega |
| --- | --- | --- |
| Preparar | Líder | Repo del equipo, responsables y un issue con criterios claros. |
| Mejorar instrucciones | Cada integrante | Un PR de su agente, revisado e integrado en el repo del equipo. |
| Ejecutar | Una persona, con el equipo | Entregas de los agentes revisadas paso a paso. |
| Comprobar y entregar | Equipo | Pruebas reales y revisión del PR en el repo de producto. |

Empieza por [TEAM.md](TEAM.md) para repartir el trabajo. Después, la persona que
ejecutará el flujo sigue estos tres pasos. Los detalles por rol están en
[Mejora tu agente](MEJORA_TU_AGENTE.md).

## 1. Prepara el entorno

Necesitas Python 3.11 a 3.13, Git, [GitHub CLI](https://cli.github.com/)
y [Copilot CLI](https://github.com/features/copilot/cli). Recomendamos Python 3.12.
Ejecuta los comandos en Bash; en Windows, usa Git Bash.

```bash
python -m venv .venv
if [ -f .venv/Scripts/activate ]; then
  source .venv/Scripts/activate
else
  source .venv/bin/activate
fi
python -m pip install -r requirements.txt
[ -f .env ] || cp .env.example .env
```

Si tu Python se llama `python3.12`, úsalo en el primer comando.
Después de activar el entorno, usa `python`.

Ejecuta `gh auth login` y `gh auth setup-git`. Abre `copilot`, ejecuta `/login`
y sal de Copilot para volver a la terminal.

## 2. Elige el producto y el issue

Completa `.env` con el repositorio de producto y el número del issue que van a resolver:

```dotenv
GITHUB_OWNER=tu-equipo
GITHUB_REPO=tu-producto
GITHUB_ISSUE=12
```

Necesitas permiso para publicar una rama y abrir un PR en ese repositorio.
Solo el equipo de siete cambia `GUARDRAILS_INCLUDE_DATA=true`.
Las demás opciones tienen valores predeterminados; consulta
[Configuración opcional](CONFIGURACION.md) si necesitas cambiarlas.

## 3. Ejecuta y revisa

```bash
python avanzado.py
```

Confirma el tipo de proyecto con Enter o escribe `backend`, `frontend` o `ambos`.
El flujo recorre Arquitectura → Backend → Frontend → Pruebas → Seguridad → Chapter.
En el equipo de siete, Datos participa después de Arquitectura.

Después de cada etapa:

| Tecla | Acción |
| --- | --- |
| `s` | Aceptar la salida y continuar. |
| `v` | Leer la salida completa antes de decidir. |
| `r` | Volver a ejecutar el agente. |
| `n` | Detener el flujo. |

Los archivos aprobados se guardan en `output/` y en el clon local del producto
dentro de `.tmp/`. Si Chapter pide correcciones, el flujo repite la implementación
y la revisión, hasta tres rondas. Al finalizar, valida la salida, publica la rama
y abre el PR. Revisa el código antes de aprobar cada etapa.

Cada llamada usa el plan de Copilot. Los agentes proponen pruebas; una persona
debe ejecutarlas en el producto y adjuntar la salida real al PR.

El ejercicio termina cuando el PR del producto cumple los criterios del issue,
tiene la salida real de las pruebas y fue revisado por el equipo. Abrir el PR
o agotar las rondas del Chapter no equivale a completar el ejercicio.

## Si detienes la ejecución

Vuelve a ejecutar `python avanzado.py` y acepta retomar la sesión.
El avance queda en `output/.checkpoint.json`; los informes, en `output/`;
las evidencias y la URL del PR, en `evidence/`.

Conserva `output/` con otro nombre antes de cambiar entre seis y siete agentes.
Los checkpoints de ambos modos no se mezclan. El agente de Datos propone SQL,
pero el flujo no ejecuta migraciones.

## Comprobar el laboratorio

```bash
python tools/verify.py
```

Comprueba el flujo con respuestas simuladas, sin usar Copilot ni GitHub.
Incluye aprobaciones, reintentos, reanudación y validaciones de entrada y salida.
Estas validaciones buscan contenido vacío, formatos incorrectos y patrones de
datos sensibles. No sustituyen la revisión del código ni las pruebas del producto.

## Trabajar con tu equipo

- [TEAM.md](TEAM.md): crear el repo del equipo, repartir roles y entregar cambios.
- [Mejora tu agente](MEJORA_TU_AGENTE.md): ejercicio y entregables por rol.
- [Configuración opcional](CONFIGURACION.md): modelo, ramas, evaluaciones HTTP y MCP.
- [SOURCE.md](SOURCE.md): origen de esta copia.

Para evaluar una ejecución con el modelo real, usa `python evals/eval_basic.py`.
Consume llamadas a Copilot y guarda el resultado en `evidence/eval_results.json`.
