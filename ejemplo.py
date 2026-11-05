"""Código ficticio usado en todos los niveles; no contiene credenciales reales."""

ENTRADA = '''### app.py
```python
tareas = []

def crear_tarea(titulo):
    # Este ejemplo acepta títulos vacíos: el agente propondrá una validación.
    tarea = {"id": len(tareas) + 1, "titulo": titulo}
    tareas.append(tarea)
    return tarea
```
'''
