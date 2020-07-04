# Degrees

## Background

According to the Six Degrees of Kevin Bacon game, anyone in the Hollywood film industry can be connected
to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

In this problem, we’re interested in finding the shortest path between any two actors by choosing a sequence
of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is
2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon
is connected to Tom Hanks by both starring in “Apollo 13.”

We can frame this as a search problem: our states are people. Our actions are movies, which take us from one
actor to another (it’s true that a movie could take us to multiple different actors, but that’s okay for this problem).
Our initial state and goal state are defined by the two people we’re trying to connect. By using breadth-first search,
we can find the shortest path from one actor to another.

## Usage

```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=yRnkHhSkx-k
" target="_blank"><img src="http://img.youtube.com/vi/yRnkHhSkx-k/0.jpg"
alt="Demo Degrees" width="240" height="180" border="10" /></a>
