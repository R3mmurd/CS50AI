import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = corpus[page]
    num_links = len(links)
    corpus_size = len(corpus) 

    if num_links == 0:
        return {
            page: 1/corpus_size for page in corpus
        }
    
    tm = {
        link: damping_factor/num_links for link in links
    }
    sum_p = 0
    for page in corpus:
        p = (1 - damping_factor)/corpus_size
        if page in tm:
            tm[page] += p
        else:
            tm[page] = p
            
        sum_p += tm[page]

    assert abs(1 - sum_p) < 10e-6
    return tm


def weighted_choice(table):
    """
    Return a random selection of an element based in its probability of
    being chosen.
    """
    r = random.random()
    for page, prob in table.items():
        if r < prob:
            return page
        r -= prob
        

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    counter = { page: 0 for page in corpus }
    page = random.choice(list(corpus))
    for i in range(n):
        counter[page] += 1
        tm = transition_model(corpus, page, damping_factor)
        page = weighted_choice(tm)

    return { k: v/n for k, v in counter.items() }       


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    def pr(page, corpus, d, ranks):
        corpus_size = len(corpus)

        sl = 0

        for corpus_page in corpus:
            links = corpus[corpus_page]
            num_links = len(links)

            if num_links == 0:
                sl += ranks[corpus_page]/n
            elif page in links:
                sl += ranks[corpus_page]/num_links
            
        return (1 - d)/n + d*sl

    n = len(corpus)
    ranks = { page: 1/n for page in corpus }

    change = True
    while change:
        change = False
        for page in corpus:
            new_rank = pr(page, corpus, damping_factor, ranks)
            diff = abs(new_rank - ranks[page])
            change = change or diff > 0.001
            ranks[page] = new_rank

    return ranks

if __name__ == "__main__":
    main()
