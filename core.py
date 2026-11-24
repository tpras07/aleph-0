import json
from collections import Counter

with open("data/arxiv-metadata-oai-snapshot.json", "r", encoding ="utf-8") as file:
    all_categories = {}
    papers_per_year = {}
    paper_counter = 0
    author_count = {}
    abstract_mean = 0
    paper_revisions = {}
    for line in file:
        paper = json.loads(line)
        categories = paper.get('categories').split()
        for category in categories:
            all_categories[category] = all_categories.get('categories', 0)+ 1
                
        abstract_count = (paper_counter * abstract_mean)
        paper_counter += 1
        abstract_mean = (abstract_count + len(paper.get("abstract").strip()))/(paper_counter)
        author_count[len(paper.get('authors').split(','))] = author_count.get(len(paper.get('authors').split(',')), 0) + 1
        paper_revisions[len(paper.get('versions'))] = paper_revisions.get(len(paper.get('versions')),0) + 1

        for year in range(2007, 2027):
            if str(year) in paper.get('versions')[0].get('created'):
                papers_per_year[year] =papers_per_year.get(year,0)  + 1


    print(paper_counter)
    counts = Counter(all_categories)
    print(counts.most_common(1))
    print(papers_per_year)
    print(Counter(papers_per_year).most_common(5))
    print(abstract_mean)
    print(author_count)
    print(paper_revisions)

        
        
