import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import argparse
import json
import sys

def search_arxiv(query, max_results=5):
    """
    A basic fallback literature search using the public arXiv API.
    """
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'search_query=all:{urllib.parse.quote(query)}&start=0&max_results={max_results}'
    
    try:
        response = urllib.request.urlopen(base_url + search_query)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        namespace = {'atom': 'http://www.w3.org/2005/Atom'}
        results = []
        
        for entry in root.findall('atom:entry', namespace):
            title = entry.find('atom:title', namespace).text.strip()
            summary = entry.find('atom:summary', namespace).text.strip()
            link = entry.find('atom:id', namespace).text.strip()
            
            results.append({
                "title": title.replace('\n', ' '),
                "summary": summary.replace('\n', ' '),
                "url": link
            })
            
        return {"status": "success", "query": query, "results": results}
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Fallback Local Literature Search (arXiv)")
    parser.add_argument("--query", required=True, help="Search keywords (e.g., 'attention memory trace')")
    parser.add_argument("--output", required=True, help="Path to save the JSON results")
    parser.add_argument("--max_results", type=int, default=5, help="Number of papers to fetch")
    
    args = parser.parse_args()
    
    print(f"Searching arXiv for: {args.query}")
    data = search_arxiv(args.query, args.max_results)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    if "error" in data:
        print(f"Search failed: {data['error']}")
        sys.exit(1)
    else:
        print(f"Found {len(data['results'])} papers. Saved to {args.output}")

if __name__ == "__main__":
    main()
