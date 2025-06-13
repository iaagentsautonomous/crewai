#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
load_dotenv()

from datetime import datetime

from ai_development.crew import AiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Open source AI agents frameworks',
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = AiDevelopment().crew().kickoff(inputs=inputs)

         # Salvar o artefato em um arquivo
        with open("relatorio_frameworks_ai.txt", "w", encoding="utf-8") as f:
            f.write(result)
            
        print("✅ Artefato gerado e salvo como relatorio_frameworks_ai.txt")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        AiDevelopment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiDevelopment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        AiDevelopment().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
