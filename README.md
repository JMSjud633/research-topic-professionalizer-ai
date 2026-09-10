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

## 🌐 Akses Langsung Online (Cloud Platform)

Aplikasi ini dapat diakses langsung melalui web tanpa perlu mengunduh (*clone/download*) atau menginstal Python di komputer pengguna.

### 🚀 Opsi Hosting Gratis & Otomatis (Tinggal Hubungkan GitHub):

#### Opsi 1: Render (Sangat Direkomendasikan - Gratis 100%)
1. Masuk ke **[Render.com](https://render.com/)** dengan akun GitHub Anda.
2. Klik **New +** > **Web Service**.
3. Pilih repository `research-topic-professionalizer-ai`.
4. Render akan otomatis mendeteksi konfigurasi [render.yaml](file:///c:/Users/ADVAN/.gemini/antigravity-ide/scratch/research_professionalizer/render.yaml) & [Procfile](file:///c:/Users/ADVAN/.gemini/antigravity-ide/scratch/research_professionalizer/Procfile).
5. Klik **Create Web Service**. Dalam 1-2 menit, URL publik Anda (misal: `https://respro-ai.onrender.com`) langsung aktif dan siap dibagikan ke pengguna!

#### Opsi 2: Hugging Face Spaces (Gratis & 24/7 Uptime)
1. Masuk ke **[Hugging Face Spaces](https://huggingface.co/spaces)**.
2. Buat Space baru, pilih **Docker** (atau Python SDK).
3. Hubungkan repository GitHub ini. File [Dockerfile](file:///c:/Users/ADVAN/.gemini/antigravity-ide/scratch/research_professionalizer/Dockerfile) akan otomatis membangun aplikasi dan memberikan link publik instan.

#### Opsi 3: Railway / Koyeb / Vercel
Aplikasi ini sudah dilengkapi [Dockerfile](file:///c:/Users/ADVAN/.gemini/antigravity-ide/scratch/research_professionalizer/Dockerfile) standar industri, sehingga kompatibel dengan semua platform cloud PaaS/Container modern secara instan.

---

## 💻 Jalankan Secara Lokal (Opsional bagi Developer)

Bagi pengembang yang ingin menjalankan atau memodifikasi kode secara offline di komputer lokal:

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
