"""
Base agent implementation with common functionality
"""
from crewai import Agent

class BaseAgent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal
        
    def create(self):
        """
        Create a CrewAI agent with the specified configuration
        """
        return Agent(
            name=self.name,
            role=self.role,
            goal=self.goal,
            verbose=True,
            allow_delegation=False
        )
