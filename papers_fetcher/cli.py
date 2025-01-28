import csv
import argparse
from papers_fetcher.api import fetch_papers
from papers_fetcher.filters import filter_non_academic_authors

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers with non-academic authors.")
    parser.add_argument("--query", required=True, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", help="Output CSV file.", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()

    if args.debug:
        print("Debug mode enabled.")

    papers = fetch_papers(args.query)
    results = []

    for paper in papers:
        authors = paper.get("Authors", [])
        non_academic_authors, companies = filter_non_academic_authors(authors)

        # Debugging missing data
        if not paper.get("PubmedID"):
            print("Warning: Missing PubmedID for paper.")
        if not paper.get("Title"):
            print("Warning: Missing Title for paper.")
        if not paper.get("PublicationDate"):
            print("Warning: Missing PublicationDate for paper.")

        corresponding_email = paper.get("CorrespondingAuthorEmail", "N/A")

        results.append({
            "PubmedID": paper.get("PubmedID", "N/A"),
            "Title": paper.get("Title", "N/A"),
            "PublicationDate": paper.get("PublicationDate", "N/A"),
            "NonAcademicAuthors": ", ".join(non_academic_authors) if non_academic_authors else "N/A",
            "CompanyAffiliations": ", ".join(companies) if companies else "N/A",
            "CorrespondingAuthorEmail": corresponding_email
        })

    if args.file:
        with open(args.file, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"Results saved to {args.file}.")
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()
