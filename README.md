# 🧠 PaperMind-Agent

> An Open-Source Agentic Workflow for tracking AI research lineage.

PaperMind-Agent is a multi-agent system designed to prevent researchers from drowning in the daily flood of AI papers. It automatically searches, analyzes, and maps the chronological flow of state-of-the-art research (such as SNNs, probabilistic modeling, and generative architectures) using open-source LLMs.

## Features
- **Search Agent:** Fetches latest papers via arXiv API.
- **Analyst Agent:** Extracts core contributions and method adaptations.
- **Writer Agent:** Generates a comprehensive markdown report.

## How to use
pip install -r requirements.txt
python src/main.py
