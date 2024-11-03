"""
Product analyst agent for detailed product analysis
"""
from .base_agent import BaseAgent

class ProductAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Product Analyst",
            role="Product Analysis Specialist",
            goal="Analyze product features, pricing, and performance metrics"
        )
