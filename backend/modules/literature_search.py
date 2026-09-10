import json
import urllib.request
import urllib.parse
from typing import List
from ..models import LiteratureItem

def search_crossref_literature(query: str, max_results: int = 5) -> List[LiteratureItem]:
    """
    Search real literature from Crossref API (Open Access metadata).
    No fake or fabricated citations are produced!
    """
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://api.crossref.org/works?query={encoded_query}&rows={max_results}&select=DOI,title,author,published,container-title,URL"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "ResearchProfessionalizerAI/1.0 (mailto:support@antigravity.local)"}
        )
        with urllib.request.urlopen(req, timeout=7) as response:
            data = json.loads(response.read().decode('utf-8'))
            items = data.get("message", {}).get("items", [])
            
            literature_list = []
            for item in items:
                title_list = item.get("title", [])
                title = title_list[0] if title_list else "Untitled Work"
                
                authors = []
                for auth in item.get("author", [])[:3]:
                    given = auth.get("given", "")
                    family = auth.get("family", "")
                    authors.append(f"{given} {family}".strip())
                if not authors:
                    authors = ["Anonymous / Institutional"]
                    
                year = None
                published = item.get("published", {}).get("date-parts", [[]])
                if published and published[0]:
                    year = str(published[0][0])
                    
                journal_list = item.get("container-title", [])
                journal = journal_list[0] if journal_list else "Academic Publication / Proceeding"
                
                doi = item.get("DOI", "")
                doi_url = item.get("URL", f"https://doi.org/{doi}" if doi else "#")
                
                literature_list.append(LiteratureItem(
                    title=title,
                    authors=authors,
                    year=year,
                    doi=doi,
                    url=doi_url,
                    journal=journal,
                    relevance="Studi pembanding empiris terdahulu mengenai interaksi variabel sejenis dalam domain literatur terkait."
                ))
            if literature_list:
                return literature_list
    except Exception as e:
        # Fallback graceful behavior without hallucinating fake DOIs
        pass
        
    # If network fails or no matches, explicitly declare this without making up citations
    return [
        LiteratureItem(
            title="Catatan: Penelusuran literatur real-time eksternal memerlukan koneksi internet aktif.",
            authors=["Sistem Verifikasi Literatur"],
            year="2026",
            doi="N/A",
            url="#",
            journal="Research Topic Diagnostic Engine",
            relevance="Sesuai prinsip No Fake Academia, sistem tidak memalsukan nama penulis, DOI, atau jurnal jika API eksternal belum diakses."
        )
    ]
