def supervisor(state):
    iteration = state.get("iteration", 0) + 1

    # HARD STOP CONDITION
    if iteration >= 5:
        return {
            **state,
            "iteration": iteration,
            "stop": True
        }

    return {
        **state,
        "iteration": iteration,
        "stop": False
    }



