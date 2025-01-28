from typing import Dict, List, Tuple

def filter_non_academic_authors(authors: List[Dict]) -> Tuple[List[str], List[str]]:
    """Filter out non-academic authors based on affiliations."""
    non_academic_authors = []
    companies = []
    
    academic_keywords = ["university", "lab", "institute", "college", "academy"] 
    for author in authors:
        name = author.get("name")
        affiliation = author.get("affiliation")
        
        if not name:
            continue  # Skip if author name is missing
        
        if affiliation and not any(keyword in affiliation.lower() for keyword in academic_keywords):
            non_academic_authors.append(name)
            companies.append(affiliation)

    return non_academic_authors, companies
