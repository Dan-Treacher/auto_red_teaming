from models.model_a import ModelA
from models.model_b import ModelB
from redteam.redteam import RedTeam
# Models are stored in C:\Users\dantr\.cache\huggingface\hub

def main():
    model_a = ModelA()
    model_b = ModelB()
    
    model_a_response = model_a.generate("What is the capital of France?")
    print(f"Model A Response: {model_a_response}")
    model_b_response = model_b.generate("What is the capital of China?")
    print(f"Model B Response: {model_b_response}")  

    red_team = RedTeam(model_a, model_b)
    vulnerabilities_report = red_team.initiate()
    print(vulnerabilities_report)

if __name__ == "__main__":
    print('Running main')
    main()