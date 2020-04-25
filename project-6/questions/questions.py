import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    filesmap = dict()
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath) as f:
            filesmap[filename] = f.read()

    return filesmap


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    return sorted(
        w for w in nltk.word_tokenize(document.lower())
        if w not in string.punctuation + "''"
        and w not in nltk.corpus.stopwords.words("english")
    )


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    # Extract words from corpus
    words = set()
    for document in documents:
        words.update(set(documents[document]))

    # Calculate IDFs
    idfs = dict()
    for word in words:
        f = sum(word in documents[document] for document in documents)
        idf = math.log(len(documents) / f)
        idfs[word] = idf

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    ranked_files = dict()

    for filename in files:
        s_tf_idf = sum(idfs[w]*files[filename].count(w) for w in query)
        ranked_files[filename] = s_tf_idf

    return sorted(
        list(ranked_files.keys()), key=lambda f: ranked_files[f],
        reverse=True
    )[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    ranked_sentences = dict()

    for s in sentences:
        ss = sentences[s]
        ranked_sentences[s] = (
            sum(idfs[w] for w in query if w in ss),
            sum(w in query for w in ss)/len(ss)
        )

    return sorted(
        list(ranked_sentences.keys()), key=lambda s: ranked_sentences[s],
        reverse=True
    )[:n]


if __name__ == "__main__":
    main()
