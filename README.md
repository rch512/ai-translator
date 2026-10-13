# Containerized AI Translation Agent

## Overview
A lightweight, containerized AI agent built to automate Japanese-to-English translation and summarization workloads. This project demonstrates secure LLM integration using the DeepSeek API, Python, and Docker, specifically focusing on stateless execution and secure credential management.

## Architecture & Tech Stack
- Language: Python 3.10
- Containerization: Docker (Isolated execution environment)
- LLM Provider: DeepSeek (deepseek-chat) via the OpenAI SDK wrapper
- Configuration: Environment Variables (.env, .dockerignore, .gitignore)

## Repository Structure
```text
ai-translator/
├── .env                 # Local API keys (Excluded from version control)
├── .dockerignore        # Prevents secret leakage into the Docker image
├── .gitignore           # Prevents secret leakage into GitHub
├── app.py               # Application logic and API integration
├── Dockerfile           # Multi-layer container blueprint
├── input.txt            # Raw text ingestion source
└── requirements.txt     # Dependency list (openai)
```

## Security Implementation
The DeepSeek API key is kept completely separate from the code. Instead of being typed directly into the script, the key is loaded from a local .env file only when the program runs. This guarantees the secret is never accidentally uploaded to GitHub or permanently saved inside the Docker image.

##Local Deployment Setup
1. Build the Container Image
The Dockerfile pulls a lightweight Python runtime, installs dependencies, and packages the application logic.
```bash
docker build -t translator-app .
```
2. Execute the Workload
The container runs the AI agent using a volume mount (-v). This maps the host directory to the container's working directory, allowing the stateless container to read input.txt and successfully write the generated output.txt back to the host machine.

(PowerShell Execution):
```powershell
docker run --env-file .env -v "${PWD}:/app" translator-app
```
## Execution Visuals
# Container Execution Lifecycle
Successful runtime execution showing the container booting, processing the AI workload, saving the output, and cleanly exiting.
![Alt Text](https://github.com/rch512/ai-translator/blob/main/Docs/terminal.png)
# Payload Transformation (Input vs. Output)
Side-by-side comparison of the ingested Japanese text (input.txt) and the LLM-generated translation and summarization (output.txt).
![Alt Text](https://github.com/rch512/ai-translator/blob/main/Docs/text_output.png)
