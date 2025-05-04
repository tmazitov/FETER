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
[Link to demo video](https://github.com/rrangwan/Fetch.AI_Hackathon_Dubai_2025_submission-/blob/main/docs/demo.mp4)

### Screenshots
[screenshots showcasing agent in action](https://github.com/rrangwan/Fetch.AI_Hackathon_Dubai_2025_submission-/blob/main/docs/screenshots.pdf)

## 💼 Business Potential

Our celebrity voice agent platform unlocks significant market opportunities with diverse revenue streams:

### **Target Audience**
- Celebrities, public figures, and content creators seeking enhanced fan engagement.
- Entertainment companies managing artist portfolios.
- Sports personalities and fans desiring personalized interactions.

### **Revenue Streams**
- Subscription plans for celebrities based on interaction volume.
- Sharing of royalties from musical content generation.
- Premium fan experiences (e.g., personalized messages, custom content).
- Sponsored interactions via brand partnerships.
- White-label solutions for entertainment companies.

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

- [ Link to your project presentation/pitch deck](https://github.com/rrangwan/Fetch.AI_Hackathon_Dubai_2025_submission-/blob/main/docs/CelebrityAI.pdf)
- [Link to one-page project summary](https://github.com/rrangwan/Fetch.AI_Hackathon_Dubai_2025_submission-/blob/main/docs/CelebrityAI.pptx)
- [Summary](https://github.com/rrangwan/Fetch.AI_Hackathon_Dubai_2025_submission-/blob/main/docs/summary.pdf)

## 📊 Track-Specific Information

### For Creator Economy Track

We collaborated with N1yah, a celebrity who aspired to connect with her fans more effectively through a digital presence. She envisioned a solution that could replicate her voice and personality, enabling her to engage with her audience at scale while maintaining authenticity. After brainstorming together, we conceptualized and developed a digital voice clone powered by AI.

This AI-driven voice clone not only captures Niyah's tone and style but also performs a variety of tasks, including:
- Responding to fan messages in her voice.
- Delivering personalized content such as greetings or shoutouts.
- Creating an immersive and authentic fan experience.

Using Fetch.AI's agent framework, ASI-1 Mini and the F5-TTS model, we brought this vision to life. The agent performs ethical checks, generates celebrity-style responses, and converts them into a realistic voice using advanced voice synthesis. This solution allows Niyah to maintain a meaningful connection with her fans while saving time and effort, showcasing how digital clones can transform fan engagement in the creator economy.
### For ASI-1 Mini Challenge

During development, we faced challenges due to the lack of sample data for ASI-1 Mini. With guidance from mentors, we successfully integrated ASI-1 Mini for:
- Ethical text filtering to ensure guideline compliance.
- Celebrity-style text generation for engaging responses.

This integration showcases ASI-1 Mini's reasoning capabilities, enabling precise and efficient multi-step task execution.
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
