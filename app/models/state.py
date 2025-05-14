from langgraph.state import State

class State(State):
    session_id: str
    history: list  # You can refine this structure as needed
