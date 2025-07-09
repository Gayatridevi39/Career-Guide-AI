# 💼 Career Guide AI – Personalized AI Career Advisor

An AI-powered assistant that provides intelligent, specific, and personalized career guidance using **LangChain**, **Google Gemini**, and **Chroma VectorDB**. Designed to help students, career switchers, and professionals make informed career decisions.

---

## 🚀 Key Features

- 📄 Upload your own **career-related PDFs** (guides, resumes, brochures)
- 🧠 Ask **career-specific questions** and get expert-level answers
- 💬 Powered by **Google Gemini + LangChain** with a customized prompt
- 🧠 Uses **HuggingFace Embeddings** and **ChromaDB** for fast semantic search
- 🎯 Offers **personalized suggestions** based on your skills

---

## 🧠 What It Does

Career Guide AI simulates a **career advisor with 20+ years of experience**, using context-rich answers from a career knowledge base and optional uploaded documents.

You can:

- Ask targeted questions like “What should I focus on to become a backend engineer?”
- Upload a PDF career guide and get insights from its content
- Enter your skills and receive job role suggestions tailored to you

---

## 🛠️ Tech Stack

| Component                 | Role                                                  |
|--------------------------|-------------------------------------------------------|
| `Streamlit`              | Frontend web UI                                       |
| `LangChain`              | Orchestration of LLM + retrieval + prompt management |
| `Gemini (Google AI)`     | Generative model for answers                          |
| `Chroma VectorDB`        | Embedding-based document retrieval                    |
| `HuggingFace Embeddings` | Lightweight semantic search embeddings                |
| `dotenv`                 | Secure API key handling                               |
| `PyPDFLoader`            | Load and split uploaded career PDFs                   |

---

## 📸 Screenshot

![App Screenshot](assets/screenshot.png)

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/career-guide-ai.git
cd career-guide-ai

