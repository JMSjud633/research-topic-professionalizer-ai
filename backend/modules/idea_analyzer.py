import re
from typing import Dict, Any, List
from ..models import ScopeDiagnosis

DOMAIN_KEYWORDS = {
    "Natural Sciences / Environmental Science": ["cuaca", "iklim", "lingkungan", "polusi", "tanah", "air", "hutan", "ekosistem", "weather", "climate", "environment", "biodiversity", "suhu"],
    "Biology / Health Sciences": ["kesehatan", "penyakit", "bakteri", "virus", "tanaman", "fisiologi", "imun", "sel", "nutrisi", "genetika", "darah", "jantung", "health", "disease", "biology"],
    "Computer Science / AI / Data Science": ["ai", "machine learning", "deep learning", "algoritma", "aplikasi", "sistem", "iot", "website", "klasifikasi", "prediksi", "computer", "data", "model", "neural"],
    "Education": ["siswa", "guru", "pembelajaran", "kurikulum", "sekolah", "hasil belajar", "metode mengajar", "motivasi belajar", "student", "teacher", "learning", "education", "akademik"],
    "Social Sciences / Sociology": ["sosial", "masyarakat", "budaya", "perilaku", "interaksi", "komunitas", "gender", "norma", "social", "society", "culture"],
    "Economics & Business": ["ekonomi", "harga", "pasar", "keuangan", "pemasaran", "umkm", "investasi", "pendapatan", "economic", "financial", "market", "bisnis"],
    "Physics & Engineering": ["energi", "getaran", "arus", "voltase", "mekanika", "material", "sensor", "konstruksi", "mesin", "physics", "engineering"]
}

def classify_domain(raw_idea: str, user_hint: str = "") -> str:
    if user_hint and user_hint != "Auto-detect":
        return user_hint
    
    text = raw_idea.lower()
    matches = {}
    for domain, kws in DOMAIN_KEYWORDS.items():
        score = sum(1 for kw in kws if re.search(r'\b' + re.escape(kw) + r'\b', text))
        if score > 0:
            matches[domain] = score
            
    if matches:
        return max(matches, key=matches.get)
    return "Interdisciplinary / Applied Sciences"

def diagnose_scope(raw_idea: str, domain: str) -> ScopeDiagnosis:
    text = raw_idea.strip()
    words = text.split()
    
    # Heuristic checks
    broad_indicators = ["pengaruh", "dampak", "analisis", "faktor", "efek", "hubungan"]
    is_very_short = len(words) < 7
    has_vague_terms = any(t in text.lower() for t in ["kesehatan", "masyarakat", "kinerja", "kualitas", "cuaca", "ai", "teknologi"])
    
    if is_very_short or (len(words) <= 8 and has_vague_terms):
        return ScopeDiagnosis(
            status="Too broad",
            explanation=f"Ide '{raw_idea}' masih terlalu luas. Istilah-istilah kunci seperti konsep subjek dan objeknya belum terdefinisi secara operasional. Belum jelas parameter spesifik apa yang diukur dan populasi mana yang diteliti.",
            recommended_focus="Persempit dengan membedah komponen: ubah konsep payung menjadi indikator terukur (misal: 'cuaca' -> suhu udara & kelembapan ruang kelas; 'kesehatan' -> keluhan respiratory atau tingkat presensi)."
        )
    elif len(words) > 25:
        return ScopeDiagnosis(
            status="Too narrow",
            explanation="Deskripsi ide sangat spesifik dan berpotensi over-constrained pada satu kasus unik yang sulit digeneralisasi.",
            recommended_focus="Pertahankan fokus inti namun pastikan konteks permasalahan masih relevan dan memiliki kontribusi teoritis/praktis yang memadai."
        )
    else:
        return ScopeDiagnosis(
            status="Appropriate",
            explanation="Cakupan ide sudah memiliki arah hubungan yang jelas, namun membutuhkan ketegasan metodologis dan definisi operasional variabel.",
            recommended_focus="Pertajam indikator pengukuran, desain kontrol terhadap variabel pengganggu (confounding variables), dan teknik sampling."
        )

def generate_critical_questions(raw_idea: str, domain: str) -> List[str]:
    text = raw_idea.lower()
    questions = []
    
    if "cuaca" in text or "iklim" in text:
        questions.append("Parameter cuaca spesifik apa yang akan diukur secara objektif? (Suhu ekstrem, indeks panas/heat index, kelembapan relatif, atau curah hujan?)")
    if "kesehatan" in text:
        questions.append("Bagaimana indikator 'kesehatan' dioperasionalkan? (Tingkat absensi akibat sakit, gejala ISPA/respirasi, fatigue level, atau pemeriksaan vital sign?)")
    if "ai" in text or "teknologi" in text:
        questions.append("Bagaimana 'penggunaan AI' diukur secara kuantitatif? (Frekuensi pemakaian, jenis prompt, durasi jam/minggu, atau adopsi tools tertentu?)")
    if "siswa" in text or "mahasiswa" in text:
        questions.append("Kelompok usia atau jenjang spesifik mana yang dijadikan populasi target, dan bagaimana mengontrol faktor latar belakang sosioekonomi/nutrisi mereka?")
        
    questions.append("Apakah Anda bermaksud menguji hubungan kausal (sebab-akibat eksperimental) atau sekadar korelasi/asosiasi temporal?")
    questions.append("Bagaimana cara Anda memitigasi variabel pengganggu (confounding variables) yang juga memengaruhi hasil?")
    
    return questions[:4]
