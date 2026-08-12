"""
Task 3: Agentic AI & Generative AI Paradigm
Build a reliable, structured reasoning workflow for an LLM Agent without external API calls.
"""

def build_agent_emergency_prompt(raw_incident_report: str) -> str:
    """
    TODO: Construct a structured system prompt template for an LLM Agent.
    The prompt must instruct the LLM to output EXACTLY a valid JSON object 
    containing the keys: 'severity' (LOW, MEDIUM, CRITICAL) and 'dispatch_unit' (FIRE, POLICE, MEDICAL).
    
    Ensure you safely embed the raw_incident_report string within your prompt block.
    """
    return (
        "You are a city emergency dispatch assistant. "
        "Analyze the incident report and return EXACTLY one valid JSON object with keys: "
        "'severity' and 'dispatch_unit'. "
        "Allowed severity values are LOW, MEDIUM, or CRITICAL. "
        "Allowed dispatch_unit values are FIRE, POLICE, or MEDICAL. "
        "Do not include markdown, explanations, or extra keys. "
        "Example output: {'severity': 'CRITICAL', 'dispatch_unit': 'FIRE'}. "
        f"Incident report: {raw_incident_report}"
    )
