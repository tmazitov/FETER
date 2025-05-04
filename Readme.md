# Fetch.AI Hackathon Dubai 2025 Submission

![tag : innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
[![Hackathon Link](https://img.shields.io/badge/Event-Fetch.AI_Hackathon_Dubai_2025-blue)](https://lu.ma/zjn0njeu?tk=p6Uvcy)

## 📋 Project Overview

**Project Name: Fetter**

**Agent Name:** Fetter**

**Agent Address:** [agent1q0pa630kqxx50sqyp5g2ht6nthxf6k0v8j5ekke2hvr980342xwgvfcycf7]

**Team Name:**  $Fetter
**Track:** [DevFin]

## 🌟 Problem Statement

Helping Investors decide to Buy, Sell, or Hold $FET coin based on recent market action.

## 💡 Solution

Use the capability of ASI:One LLM to analayze recent price data to determine trends and give advice.

### **🚀Agent Capabilities**
- **Ethical Text Filtering**:
  - The agent uses ASI-1 Mini to perform ethical checks on user-submitted text, ensuring that all interactions adhere to predefined ethical guidelines.
- **Celebrity-Style Text Generation**:
  - The agent generates personalized, celebrity-style responses using ASI-1 Mini's advanced language modeling capabilities.
- **Voice Synthesis**:
   - The `waver_generate_sound` function integrates the **F5-TTS model** (sourced from Hugging Face and GitHub under the MIT license) to convert text into a realistic celebrity voice.
- **Multi-Step Task Execution**:
  - The agent performs multi-step workflows, including ethical checks, text generation, and voice synthesis, ensuring seamless task execution.
- **Memory and Context Awareness**:
  - The agent stores and retrieves past interactions using a database, enabling personalized and context-aware responses.
- **ChatProtocol Integration**:
  - The agent uses `ChatProtocol v0.3.0` to handle structured conversational workflows, including message acknowledgments and multi-turn dialogues.



## 🎬 Demo

### Video Demo
[Link to demo video](https://github.com/tmazitov/FETER/blob/master/docs/demo.mp4)

### Screenshots
[screenshots showcasing agent in action](https://github.com/tmazitov/FETER/blob/master/docs/fetter_screenshots.pdf)

## 💼 Business Potential

Increase adoption of $FET coin

### **Target Audience**
Crypto Investors

### **Revenue Streams**
Pay per click/view or subscription

### **Scalability**
- Cloud-based architecture for rapid onboarding.
- Modular design for quick feature additions.
- API-first approach for seamless integration.
- Multi-language support for global reach.
- Automated training for cost-efficient voice profile creation.

## 👥 Team Information

### Team Members

- **[Member 1 Raj Rangwani]** - [Developer]
- **[Member 2 Joe Perinchery ]** - [Developer]
- **[Member 3 Timur Mazitov]** - [Developer]

## 📚 Additional Documentation

- [ Link to your project presentation/pitch deck](https://github.com/tmazitov/FETER/blob/master/docs/slides.pdf)



## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

*This project was developed for the Fetch.AI Hackathon Dubai 2025.*



# FETER Agent

FETER Agent is a lightweight analytics agent built on top of the `uagent` framework. 
It is designed for checking $FET coin statement.

## Features
- Built using the `uagent` framework for modularity and flexibility.
- Dependency management and packaging handled with `poetry`.
- Includes a `test.py` script for testing and validation.

## Getting Started
1. Install dependencies using `poetry install`.

2. Create .env and fill following this structure:
```bash
    ASI1_API_KEY="key_to_asi:one_ai"
    SEED="123456"
```

3. Run the agent: 
```bash
    poetry run python agent.py
```

4. Use test.py to test:
```bash
    poetry run python test.py
```
