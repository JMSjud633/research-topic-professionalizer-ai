# ResPro AI — AI Research Topic Professionalization System

An expert AI system that transforms rough, vague, overly broad, biased, or poorly formulated research ideas into **professional, academically defensible, feasible, and researchable topics**.

Built upon the 30 foundational principles of research professionalization:
- Clarity, Specificity, Researchability, Feasibility, and Objectivity
- Variable Operationalization (Independent, Dependent, Control, Confounders)
- 6-Dimensional Feasibility Engine (0–5 scale)
- 5 Categorized Academic Title Variations
- Comprehensive Research Blueprint Generator
- Real Crossref Academic Literature Search (Strictly No Fake Citations)

---

## 🌟 Key Features

1. **Scope & Diagnostic Engine**: Evaluates whether an idea is *Too Broad*, *Appropriate*, or *Too Narrow* and generates critical reviewer questions.
2. **Variable Matrix**: Decomposes ideas into operational indicators, metric measurement scales, and verified instruments/questionnaires.
3. **Feasibility & Risk Engine**: Evaluates Time, Resource, Data, Sample, Ethical, and Technical feasibility while pinpointing methodological risks (such as correlation vs. causation and presupposition bias).
4. **5 Categorized Academic Titles**:
   - Option A: Conservative Academic
   - Option B: More Specific
   - Option C: Method-Oriented
   - Option D: Advanced
   - Option E: Interdisciplinary
5. **Research Blueprint Generator**: Generates full academic specification (Background, Gap, Questions, $H_0/H_1$ Hypotheses, Sampling Design, and Recommended Statistical Tests).
6. **Workspace History & Iterative Refinement**: Retains evolution of research ideas (Version 1 → Version 2 → Version 3).
7. **Export Suite**: Export research blueprints directly to Markdown (`.md`), Plain Text (`.txt`), or Print/Save to PDF.

---

## 🏗️ Project Architecture

```
research_professionalizer/
├── backend/
│   ├── modules/
│   │   ├── idea_analyzer.py       # Domain classification & scope diagnostics
│   │   ├── variable_extractor.py  # Variable operationalization matrix
│   │   ├── feasibility_engine.py  # 6-dimension feasibility & bias detection
│   │   ├── title_generator.py     # 5 categorized titles & novelty analysis
│   │   ├── blueprint_generator.py # Comprehensive research blueprint generator
│   │   └── literature_search.py   # Real-time Crossref API literature fetcher
│   ├── ai_engine.py               # Analytical orchestrator
│   ├── models.py                  # Pydantic data schemas
│   └── main.py                    # FastAPI application & endpoints
├── frontend/
│   ├── index.html                 # Glassmorphic responsive UI
│   ├── style.css                  # Modern styling & animations
│   └── app.js                     # Client-side reactivity & export handlers
├── requirements.txt
├── run.bat                        # One-click Windows runner
└── README.md
```

---

## 🚀 Quick Start (Local Setup)

### 1. Prerequisites
- Python 3.10+
- Modern Web Browser (Chrome, Edge, Firefox)

### 2. Installation
Clone the repository:
```bash
git clone https://github.com/<YOUR_USERNAME>/research-topic-professionalizer-ai.git
cd research-topic-professionalizer-ai
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the FastAPI server:
```bash
python -m uvicorn backend.main:app --port 8088 --host 127.0.0.1
```
Or on Windows simply double-click:
```cmd
run.bat
```

Open your browser and navigate to:
```
http://127.0.0.1:8088/
```

---

## 🛡️ Principles & Ethics (No Fake Academia)
- **Zero Hallucinated Citations**: Real-time academic inquiries use open metadata from Crossref without inventing papers, DOIs, or author names.
- **Academic Rigor**: Focuses on research design, operational clarity, and empirical testability rather than sophisticated-sounding titles.

---

## 📄 License
MIT License. Open for students, researchers, educators, and academic institutions worldwide.
