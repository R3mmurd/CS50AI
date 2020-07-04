# PageRank

## Background

When search engines like Google display search results, they do so by placing more “important”
and higher-quality pages higher in the search results than less important pages. But how does the
search engine know which pages are more important than other pages?

One heuristic might be that an “important” page is one that many other pages link to, since it’s
reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage.
We could therefore imagine a system where each page is given a rank according to the number of incoming
links it has from other pages, and higher ranks would signal higher importance.

But this definition isn’t perfect: if someone wants to make their page seem more important, then under this
system, they could simply create many other pages that link to their desired page to artificially inflate its rank.

For that reason, the PageRank algorithm was created by Google’s co-founders (including Larry Page, for whom
the algorithm was named). In PageRank’s algorithm, a website is more important if it is linked to by other
important websites, and links from less important websites have their links weighted less. This definition
seems a bit circular, but it turns out that there are multiple strategies for calculating these rankings.

## Usage

```bash
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
  ```

## Demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=20-5o3nFMQM
" target="_blank"><img src="http://img.youtube.com/vi/20-5o3nFMQM/0.jpg"
alt="Demo PageRank" width="240" height="180" border="10" /></a>
