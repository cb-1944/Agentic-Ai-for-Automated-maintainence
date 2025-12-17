from langgraph.graph import StateGraph, END
from app.state import AgentState

from app.agents.anomaly import detect_anomaly
from app.agents.diagnosis import run_diagnosis
from app.agents.engagement import engage_customer


# -------------------------
# Anomaly Detection Node
# -------------------------
def anomaly_node(state: AgentState):
    """
    Detect anomalies from telemetry data.
    """
    state["anomaly_result"] = detect_anomaly(state["telemetry"])
    return state


# -------------------------
# Diagnosis Node (LLM)
# -------------------------
def diagnosis_node(state: AgentState):
    """
    Diagnose root cause based on detected anomalies.
    """
    anomalies = state["anomaly_result"]["anomalies"]
    state["diagnosis"] = run_diagnosis(state["telemetry"], anomalies)
    return state


# -------------------------
# Customer Engagement Node
# -------------------------
def engagement_node(state: AgentState):
    """
    Notify customer via WhatsApp with diagnosis and health score.
    """
    state["engagement_status"] = engage_customer(
        telemetry=state["telemetry"],
        diagnosis=state["diagnosis"],
       
    )
    return state


# -------------------------
# Conditional Routing
# -------------------------
def route_after_anomaly(state: AgentState):
    """
    Route execution based on anomaly presence.
    """
    if state["anomaly_result"]["is_anomaly"]:
        return "diagnosis"
    return END


# -------------------------
# Build LangGraph
# -------------------------
builder = StateGraph(AgentState)

builder.add_node("anomaly", anomaly_node)
builder.add_node("diagnosis", diagnosis_node)
builder.add_node("engagement", engagement_node)

builder.set_entry_point("anomaly")

builder.add_conditional_edges(
    "anomaly",
    route_after_anomaly,
    {
        "diagnosis": "diagnosis",
        END: END
    }
)

builder.add_edge("diagnosis", "engagement")
builder.add_edge("engagement", END)

graph = builder.compile()
