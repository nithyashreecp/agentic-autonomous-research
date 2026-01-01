def uncertainty(state):
    iteration = state.get("iteration", 1)
    decision = state.get("decision", "REJECT")

    base = 0.6 + (iteration * 0.05)
    if decision == "ACCEPT":
        base += 0.1

    confidence = round(min(base, 0.95), 2)

    return {**state, "confidence": confidence}
