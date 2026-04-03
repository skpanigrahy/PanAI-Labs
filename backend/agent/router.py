from agent.agent import run_agent
from agent.rag_agent import run_rag_agent

def route_query(intent, messages):
    # For now, all go to same agent
    # Later we plug multiple agents here

    if intent == "general":
        return run_agent(messages)

    elif intent == "math":
        return run_agent(messages)

    elif intent == "search":
        return run_rag_agent(messages)

    else:
        return run_agent(messages)