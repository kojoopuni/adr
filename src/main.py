"""
Main entry point for the Amazon research application
"""
import os
from dotenv import load_dotenv
from crews.amazon_crew import AmazonCrew

def main():
    # Load environment variables
    load_dotenv()

    # Initialize the Amazon research crew
    crew = AmazonCrew().create()

    # Execute the research process
    result = crew.kickoff()
    
    return result

if __name__ == "__main__":
    main()
