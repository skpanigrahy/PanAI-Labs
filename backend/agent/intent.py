def analyze_intent(query: str):
    query = query.lower()

    if any(word in query for word in ["calculate", "sum", "add"]):
        return "math"

    if any(word in query for word in ["document", "policy", "data", "search"]):
        return "search"

    return "general"