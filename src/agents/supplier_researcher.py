"""
Supplier researcher agent for analyzing potential suppliers
"""
from .base_agent import BaseAgent

class SupplierResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Supplier Researcher",
            role="Supplier Research Specialist",
            goal="Research and evaluate potential suppliers and manufacturing options"
        )
