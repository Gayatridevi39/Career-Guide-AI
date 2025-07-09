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
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API Key

Create a `.env` file in your root project folder with the following line:
```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```
✅ Optional: For Streamlit Cloud, use Secrets Manager instead of `.env`.

### ▶️ How to Run

```bash
streamlit run app.py
```

## ✨ Sample Usage

###🔍 Ask:
> _“What roles are suitable for someone skilled in Python and data visualization?”_

---

### 📄 Upload:
> Upload a **career roadmap PDF** and ask:  
> _“Which roadmap should I follow for a career in data science?”_

---

### 🎯 Input your skills:
> Enter:  
> `Python, SQL, NLP`  
> → Get suggestions like: **Data Analyst**, **AI Research Assistant**, **LLM Engineer**

--- 

## 📚 Knowledge Base Source
- `career_docs/software_guide.txt` - Default sample career knowledge
- ✅ You can upload your own PDFs to customize the assistant's knowledge base.

---

## 🔮 Future Roadmap

- 🗣️ Voice input + text-to-speech for accessibility
- 🧠 Career clustering using unsupervised machine learning
- 🔗 Resume matcher and skill gap analyzer
- 🧾 Export recommendations to PDF/email

---

## 📬 Contact

Gayatri Devi Kajuluri
📧 [kajulurigayatridevi@gmail.com](mailto:kajulurigayatridevi@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/gayatri-devi-kajuluri/)

---

## 📢 Disclaimer
Career Guide AI is intended for educational and demonstration purposes only.
Always consult qualified career experts before making important decisions.
