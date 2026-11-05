"""Arquitecto: diagnóstico y plan del repositorio, en una sola llamada."""

from graph.state import WorkflowState
from graph.context import _ctx, _const_block


INSTRUCTIONS = (
    "Eres el arquitecto de software del equipo. Analiza el Issue del equipo, "
    "sus criterios de aceptación y las interfaces del producto, y entrega un "
    "diseño que el implementador pueda seguir sin ambigüedad.\n"
    "Debes:\n"
    "- Definir componentes, responsabilidades y límites del cambio (qué entra y qué no).\n"
    "- Especificar entradas, respuestas y errores de la API, con ejemplos de "
    "petición y respuesta.\n"
    "- Relacionar cada criterio de aceptación con el componente que lo resuelve.\n"
    "- Declarar supuestos y preguntas pendientes.\n"
    "Formato de salida (obligatorio):\n"
    "- `## Analysis` en una línea independiente: diagnóstico, criterios de "
    "aceptación y su correspondencia con los componentes, supuestos y preguntas.\n"
    "- `## Plan` en una línea independiente: archivos afectados y orden de los cambios.\n"
    "- No agregues otros encabezados de nivel 2 ni texto fuera de estas dos secciones.\n"
)


def architect_node(state: WorkflowState, invoke) -> dict:
    prompt = (INSTRUCTIONS + _const_block(state, "Respeta el alcance del issue y la constitución.") + "\nRepositorio: " + state['repo_name']
            + "\nTipo: " + state.get('project_type','ambos')
            + "\nCódigo original:\n" + _ctx(state['snapshot'],10000)
            + "\nDevuelve las secciones ## Analysis y ## Plan, cada una en su propia línea.")
    report = invoke(prompt)
    analysis, separator, plan = report.partition("\n## Plan\n")
    if not analysis.startswith("## Analysis\n") or not separator or not plan.strip():
        raise ValueError(
            "El arquitecto debe devolver las secciones ## Analysis y ## Plan."
        )
    return {
        "out_architect": report,
        "out_analysis": analysis.removeprefix("## Analysis\n").strip(),
        "out_plan": plan.strip(),
    }
