from papers_fetcher.filters import filter_non_academic_authors

def test_filter_non_academic_authors():
    authors = [
        {"name": "Dr. John Doe", "affiliation": "Doe Pharmaceuticals"},
        {"name": "Dr. Jane Smith", "affiliation": "University of Research"},
    ]
    non_academic_authors, companies = filter_non_academic_authors(authors)
    assert len(non_academic_authors) == 1
    assert non_academic_authors[0] == "Dr. John Doe"
    assert companies[0] == "Doe Pharmaceuticals"