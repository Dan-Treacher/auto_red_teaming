# filepath: ai-safety-redteam/src/main.py
from models.model_a import ModelA
from models.model_b import ModelB
from redteam.redteam import RedTeam

def main():
    model_a = ModelA()
    model_b = ModelB()
    
    red_team = RedTeam(model_a, model_b)
    vulnerabilities_report = red_team.evaluate()
    print(vulnerabilities_report)

if __name__ == "__main__":
    main()