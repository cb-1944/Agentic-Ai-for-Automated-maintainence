from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import json

llm = OllamaLLM(
   model = "gpt-oss:120b-cloud" , 
   base_url="http://localhost:11434",
   temperature = 0,  
)

prompt = ChatPromptTemplate.from_template("""
You are an automotive diagnostic expert.

Vehicle telemetry:
- RPM: {rpm}
- Engine Temperature: {temp}
- Speed: {speed}
                                        
- Detected anamolies : {anomalies}
                                          
These anamolies were detected by an ML model you just have to diagnose based on these anomalies given . 
Analyze the data and return a JSON object with:
- fault
- fault components                                   
- severity (LOW / MEDIUM / HIGH)

""")

def run_diagnosis(telemetry: dict, anomalies: list):
    chain = prompt | llm
    response = chain.invoke({
        "rpm": telemetry["rpm"],
        "temp": telemetry["temp"],
        "speed": telemetry["speed"],
        "anomalies": ", ".join(anomalies),
    })
    return response
