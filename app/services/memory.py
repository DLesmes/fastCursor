from app.models.state import State

class Memory:
    def __init__(self):
        self.sessions = {}

    def get_state(self, session_id: str) -> State:
        return self.sessions.get(session_id, State(session_id=session_id, history=[]))

    def update_state(self, session_id: str, message: str, response: str):
        state = self.get_state(session_id)
        state.history.append({"user": message, "agent": response})
        self.sessions[session_id] = state