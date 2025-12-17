from typing import TypedDict, Dict

class AgentState(TypedDict):
    telemetry: Dict
    anomaly_result: Dict
    diagnosis: str
    engagement_status: str
    scheduling_status: str


