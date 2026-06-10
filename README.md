# 🧠 PaperMind-Agent

> An Open-Source Agentic Workflow for tracking AI research lineage.

## Introduction
This project is an open-source, multi-agent system designed to track AI research lineage. It helps researchers avoid drowning in the daily flood of AI papers by automatically searching, analyzing, and mapping the chronological flow of state-of-the-art research (such as SNNs, probabilistic modeling, and generative architectures) using open-source LLMs.

## Key Features
- **Search Agent:** Fetches latest papers via arXiv API.
- **Analyst Agent:** Extracts core contributions and method adaptations.
- **Writer Agent:** Generates a comprehensive markdown report.

## How to use
1. Download / Install Requirements Install the necessary dependencies to set up your environment:
pip install -r requirements.txt
2. Run the Application Execute the main script to start the multi-agent workflow:
python src/main.py

## License
MIT License
