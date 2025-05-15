from app.models.state import State

class Memory:
    def __init__(self):
        self.sessions = {}

    def get_state(self, session_id: str) -> State:
        if session_id not in self.sessions:
            self.sessions[session_id] = State(session_id=session_id, history=[])
        return self.sessions[session_id]

    def update_state(self, session_id: str, message: str, response: str):
        state = self.get_state(session_id)
        state.history.append({"user": message, "agent": response})

# Create a single, shared instance of Memory
memory = Memory()