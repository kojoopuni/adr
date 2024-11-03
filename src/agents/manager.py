"""
Manager agent responsible for coordinating other agents
"""
from .base_agent import BaseAgent

class ManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Manager",
            role="Senior Product Manager",
            goal="Coordinate research efforts and synthesize findings into actionable insights"
        )
