# El laboratorio en equipo

Usen un solo issue pequeño del producto. Acuerden qué debe pasar en un caso
válido y en uno inválido antes de repartir el trabajo.

## 1. El líder prepara el repo del equipo

```bash
gh repo create guardrails --template NTTData-Academy/guardrails --public --clone
cd guardrails
cp team.example.json team.json
```

Agrega a los compañeros como colaboradores con permiso de escritura.
En `team.json`, reemplaza los usuarios de ejemplo por los usuarios reales de
GitHub, uno distinto por rol. Publica el archivo en `main`.

Los demás clonan ese repo:

```bash
gh repo clone <CAPTAIN>/guardrails
cd guardrails
```

## 2. Cada integrante mejora un rol

| Rol | Archivo | Responsabilidad |
| --- | --- | --- |
| Arquitectura | `agents/architect.py` | Solución y contrato de API. |
| Backend | `agents/backend.py` | Código y validaciones del servidor. |
| Frontend | `agents/frontend.py` | Interacción y consumo de API. |
| Pruebas | `agents/testing.py` | Casos, tests y comandos para comprobar el cambio. |
| Seguridad | `agents/security.py` | Riesgos, evidencia y correcciones. |
| Chapter | `agents/chapter.py` | Revisión conjunta y veredicto final. |

Cada persona prepara su entorno con la [guía de ejecución](EJECUCION.md), crea una rama y
mejora las instrucciones de su agente para el mismo issue. Conserva las firmas,
los campos de estado y los formatos de salida. Elige un entregable concreto
con la guía [Mejora tu agente](MEJORA_TU_AGENTE.md).

Por ejemplo, para Backend:

```bash
git switch -c agents/backend
# Edita agents/backend.py y luego verifica el flujo.
python tools/verify.py
git add agents/backend.py
git commit -m "Mejorar instrucciones de backend"
git push -u origin agents/backend
gh pr create --base main
```

El PR va al repo del líder. Un compañero lo revisa antes de integrarlo.
Repitan el proceso para cada rol.

## 3. Una persona ejecuta con el equipo

Cuando los PR de los agentes estén integrados, la persona que ejecutará el
flujo actualiza su copia:

```bash
git switch main
git pull --ff-only
python tools/verify.py
python avanzado.py
```

Su `.env` debe apuntar al producto y al issue acordados. Sigue las indicaciones
de la terminal y consulta con el responsable de cada rol antes de aprobar.
Usa `v` para leer todo, `s` para aprobar, `r` para reintentar y `n` para detener.
Para continuar otro día, ejecuta de nuevo `python avanzado.py` y acepta retomar.
Cada persona conserva su propia autenticación, `.env` y entorno virtual;
el checkpoint se retoma en la misma computadora.

## 4. El equipo comprueba y entrega

El flujo publica un PR en el repo del producto. Ese PR es distinto de los PR
que usaron para mejorar las instrucciones de los agentes.

Ejecuten las pruebas propuestas sobre los cambios del producto, adjunten su
salida real al PR y revisen los criterios del issue antes de integrarlo.
El informe de Pruebas es una propuesta; no demuestra que las pruebas pasaron.
Consulten el resultado del equipo desde «Mi equipo» en el portal.

## Solo para el equipo de siete

Añadan el responsable de `agents/data.py` en `team.json`, dentro de `roles`,
con la clave `data` y un usuario distinto. El líder activa
`GUARDRAILS_INCLUDE_DATA=true` en `.env` antes de una ejecución nueva.
Datos participa entre Arquitectura y Backend y entrega `output/data_report.md`.
Las responsabilidades y el formato SQL están en [Mejora tu agente](MEJORA_TU_AGENTE.md).

El flujo extrae el SQL aprobado, pero no ejecuta migraciones. Verifiquen respaldo,
integridad y reversión en una copia del producto antes de ejecutarlas.
Conserven `output/` con otro nombre antes de cambiar entre seis y siete agentes.
