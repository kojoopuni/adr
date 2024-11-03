"""
Agents module containing different specialized agents for Amazon research
"""
from .base_agent import BaseAgent
from .manager import ManagerAgent
from .market_researcher import MarketResearcherAgent
from .product_analyst import ProductAnalystAgent
from .supplier_researcher import SupplierResearcherAgent

__all__ = [
    'BaseAgent',
    'ManagerAgent',
    'MarketResearcherAgent',
    'ProductAnalystAgent',
    'SupplierResearcherAgent'
]
