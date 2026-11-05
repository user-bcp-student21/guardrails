"""Rol backend: edita aquí sus instrucciones y entregables."""

from graph.state import WorkflowState
from graph.context import _ctx, _runs, _const_block, _ronda, _feedback_block


INSTRUCTIONS = """Eres un desarrollador backend senior. Realiza la tarea de tu rol en ReqFlow.
Implementa el Issue en alcance siguiendo el plan y las convenciones del repositorio.
Respeta este orden de fuentes: Issue en ALCANCE, contratos y specs del producto,
constitución y plan aprobado. No amplíes el trabajo a hallazgos ajenos al Issue ni
cambies contratos de API salvo que el Issue lo solicite.

Implementa los endpoints y servicios necesarios según el plan, conservando el
contrato de API existente: rutas, métodos, esquemas, códigos de estado y semántica.
Valida entradas en los límites del sistema y devuelve errores consistentes con
las convenciones del proyecto, sin filtrar detalles internos. Define el acceso a
datos y límites transaccionales necesarios; conserva las invariantes y los datos
existentes.

Incluye al menos un caso válido y uno de error en las pruebas, además de comandos
reproducibles para ejecutarlos. No afirmes que ejecutaste comprobaciones que no
corriste; identifica como pendientes las que no puedas verificar. Emite cambios
accionables en el formato ### ruta/archivo.ext seguido de un bloque de código,
respetando el formato y las convenciones del repositorio.
En rondas posteriores, incorpora todas las observaciones del Chapter y verifica
cada corrección contra el Issue y el contrato, sin regenerar a ciegas.
"""


def backend_node(state: WorkflowState, invoke) -> dict:
    """
    Implementa los cambios de backend del plan.
    En rondas > 1 incorpora las observaciones del chapter.
    Se salta si project_type no incluye backend.
    Escribe en: out_backend
    """
    if not _runs(state, "backend"):
        print("[backend_node] project_type no incluye backend — saltando.")
        return {}

    print(f"[backend_node] Refactorizando backend (ronda {_ronda(state)})...")

    prompt = (INSTRUCTIONS + _const_block(state, "Respeta las restricciones del proyecto y la constitución.") + "\nRepositorio: " + state["repo_name"] + "\nPlan:\n" + _ctx(state.get("out_plan", ""),2500) + "\nCódigo original:\n" + _ctx(state.get("snapshot", ""),4000) + _feedback_block(state) + '\nPara código usa ### ruta/archivo.ext seguida de un bloque markdown.')
    if state.get("include_data"):
        prompt += "\nContrato aprobado de Datos y persistencia:\n" + _ctx(state.get("out_data", ""), 6000)
        prompt += (
            "\nConsume este contrato para el acceso a datos y las transacciones; "
            "no dupliques ni regeneres las migraciones de Datos. Conserva los "
            "datos existentes y coordina cualquier cambio requerido con el esquema aprobado."
        )
    else:
        prompt += (
            "\nEste equipo no tiene un rol Datos separado: cubre también el "
            "esquema y las migraciones necesarias, con una estrategia que "
            "conserve los datos existentes y permita verificar la integridad."
        )
    return {"out_backend": invoke(prompt)}
