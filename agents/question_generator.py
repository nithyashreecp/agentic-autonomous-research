from tools.llm import llm

def question_generator(state):
    prompt = f"""
From the following domains:
{state['domains']}

Generate 3 concise research questions.
Return only a numbered list.
"""
    response = llm.invoke(prompt).content
    questions = [q for q in response.split("\n") if q.strip().startswith(("1","2","3"))]
    return {**state, "questions": questions}

