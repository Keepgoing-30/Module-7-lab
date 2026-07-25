# Module 7 Lab: Nexus-Grid (The Autonomous AI City)

## 🎯 Objective & Overview
In this final lab, you will transition from classic deterministic algorithms to probabilistic AI Paradigms. You will write core components for **Nexus-Grid**, a simulated autonomous eco-city whose power grid, asset health, and emergency response pipelines are managed entirely by AI systems.

This assignment explores four foundational AI paradigms without the overhead of training massive models:
1. **AI Search & Optimization:** Using a Genetic Algorithm to find the optimal power layout.
2. **Supervised & Unsupervised Learning:** Writing the mathematical core of regression and clustering algorithms.
3. **GenAI & Agentic AI:** Structuring an autonomous agent loop to respond to simulated city infrastructure emergencies.

---

## 🚀 System Components to Complete

### Task 1: Grid Resource Selection via Genetic Algorithms (`grid_optimization.py`)
* **The Problem:** Optimizing energy distributions across neighborhoods is an NP-hard problem. Traditional search algorithms fail at scale.
* **Your Job:** Implement the **Crossover** and **Mutation** step of a Genetic Algorithm to evolve high-performing grid configurations.

### Task 2: Predictive Maintenance Math (`data_intelligence.py`)
* **The Problem:** We want to predict transformer failures and cluster sensor data. 
* **Your Job:** To understand the inner workings of ML, you will manually write the code for **Mean Squared Error (MSE)** loss calculation (Supervised) and a **Euclidean Distance** matching calculation (Unsupervised).

### Task 3: Emergency Dispatch Agent (`smart_agent.py`)
* **The Problem:** When an accident happens, an AI agent must parse the alert and pick the correct emergency response unit.
* **Your Job:** Complete an Agentic function that constructs a structured zero-shot prompt template to turn a raw text emergency alert into a clean, predictable JSON action sequence.
