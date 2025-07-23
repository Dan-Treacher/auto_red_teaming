# Automated red teaming

## Overview
Project aims to instantiate and access two open-source foundational models, using one to automatically red team the other

## Directory structure
```
auto_red_teaming
├── src
│   ├── main.py
│   ├── models
│   │   ├── model_a.py
│   │   └── model_b.py
│   ├── redteam
│   │   └── redteam.py
│   └── utils
│       └── helpers.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Setup
**Docker commands**
```bash
docker build -t ai-safety-redteam .
docker run -p 5000:5000 ai-safety-redteam
```

**AWS deployment**
Intending to do a containerised deployment to ECS at some point