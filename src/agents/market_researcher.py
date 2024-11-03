"""
Market researcher agent for analyzing market trends and opportunities
"""
from .base_agent import BaseAgent

class MarketResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Market Researcher",
            role="Market Research Specialist",
            goal="Analyze market trends, competition, and identify market opportunities"
        )
