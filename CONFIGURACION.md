# Configuración opcional

Para empezar completa `GITHUB_OWNER`, `GITHUB_REPO` y el número de
`GITHUB_ISSUE` en `.env`. El issue delimita el trabajo; si lo dejas vacío,
el flujo analiza el repositorio sin ese alcance.

Los valores siguientes ya tienen un valor predeterminado. Agrégalos a `.env`
solo cuando necesites cambiarlos.

| Variable | Valor predeterminado | Para qué sirve |
| --- | --- | --- |
| `COPILOT_MODEL` | `gpt-6-luna` | Modelo de Copilot. |
| `COPILOT_REASONING_EFFORT` | `high` | Esfuerzo de razonamiento. |
| `COPILOT_USE_LOGGED_IN_USER` | `true` | Usa la sesión iniciada con `/login` en Copilot CLI. |
| `GIT_BASE_BRANCH` | `main` | Rama destino del PR de producto. |
| `GIT_HEAD_BRANCH` | Generada por el flujo | Rama donde publica los cambios. |
| `MAX_REVIEW_ROUNDS` | `3` | Límite de rondas de revisión del Chapter. |
| `GUARDRAILS_INCLUDE_DATA` | `false` | Activa Datos para el equipo de siete. |

Para repositorios privados, autentica Git con `gh auth setup-git`.
El flujo también admite `GITHUB_TOKEN` para clonar.

## Evaluaciones HTTP

`python evals/contract_evals.py` requiere los servicios del producto levantados.
Estas opciones pertenecen a esa evaluación; no son necesarias para `main.py`.

```dotenv
BACKEND_BASE_URL=http://localhost:8080
API_BASE_URL=http://localhost:8000
HTTP_TIMEOUT=30
TEST_USER=student
TEST_USER_PASSWORD=Workshop123!
LOGIN_USER_FIELD=username
```

## Cliente MCP opcional

`main.py` usa Git y GitHub CLI directamente. Si trabajas con el cliente
independiente `mcp_git.py`, sus opciones son:

```dotenv
GIT_MCP_URL=http://localhost:8082
MCP_TIMEOUT=60
MCP_VERBOSE=false
FRONTEND_REPO=workshop-login-frontend
BACKEND_REPO=workshop-auth-backend
API_REPO=workshop-requirements-api
```

`MCP_GIT_URL` es un alias que se usa si no defines `GIT_MCP_URL`.
