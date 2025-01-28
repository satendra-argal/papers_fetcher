import requests
from typing import List, Dict

def fetch_papers(query: str) -> List[Dict]:
    """Fetch papers from PubMed API based on the query."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Limit to 10 results for simplicity
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)  # Add timeout
        response.raise_for_status()
        data = response.json()
        ids = data.get("esearchresult", {}).get("idlist", [])
        
        if not ids:
            print("No papers found for the given query.")
            return []

        # Fetch details for up to 10 papers to avoid too many requests
        papers = []
        for paper_id in ids[:10]:  # Limit detailed fetch to 10 papers
            paper_details = fetch_paper_details(paper_id)
            if paper_details:  # Add only valid results
                papers.append(paper_details)

        return papers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers: {e}")
        return []

def fetch_paper_details(paper_id: str) -> Dict:
    """Fetch detailed information for a specific paper by PubMed ID."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "json"
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)  # Add timeout
        response.raise_for_status()
        data = response.json()
        paper_data = data.get("result", {}).get(paper_id, {})

        return {
            "PubmedID": paper_id,
            "Title": paper_data.get("title"),
            "PublicationDate": paper_data.get("pubdate"),
            "Authors": paper_data.get("authors", [])
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for PubMed ID {paper_id}: {e}")
        return {}
