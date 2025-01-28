import pytest
from papers_fetcher.api import fetch_papers, fetch_paper_details

def test_fetch_papers():
    # Basic test to ensure the function returns a list
    query = "cancer"
    papers = fetch_papers(query)
    assert isinstance(papers, list)
    if papers:
        assert "PubmedID" in papers[0]
        assert "Title" in papers[0]
        assert "PublicationDate" in papers[0]

def test_fetch_paper_details():
    # Test fetching details for a known paper ID
    paper_id = "12345678"  # Replace with a real ID for integration testing
    details = fetch_paper_details(paper_id)
    assert isinstance(details, dict)
    assert "PubmedID" in details
    assert details["PubmedID"] == paper_id
