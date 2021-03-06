import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def compute_prob(name, num_genes, people, one_gene, two_genes):
    """
    Compute the probability of {name} having {num_genes} genes.
    """
    if people[name]['mother'] is None:
        return PROBS['gene'][num_genes]

    mother = people[name]['mother']
    father = people[name]['father']

    num_genes_mother = 1 if mother in one_gene else 2 if mother in two_genes else 0
    num_genes_father = 1 if father in one_gene else 2 if father in two_genes else 0

    prob_from_mother = num_genes_mother/2
    prob_from_father = num_genes_father/2

    if num_genes == 0:
        not_from_mother = (prob_from_mother * PROBS['mutation']
                           + (1 - prob_from_mother) * (1 - PROBS['mutation']))
        not_from_father = (prob_from_father * PROBS['mutation']
                           + (1 - prob_from_father) * (1 - PROBS['mutation']))
        return not_from_mother*not_from_father

    if num_genes == 1:
        not_from_mother = (prob_from_mother * PROBS['mutation']
                           + (1 - prob_from_mother) * (1 - PROBS['mutation']))
        not_from_father = (prob_from_father * PROBS['mutation']
                           + (1 - prob_from_father) * (1 - PROBS['mutation']))
        from_mother = (prob_from_mother * (1 - PROBS['mutation'])
                       + (1 - prob_from_mother) * PROBS['mutation'])
        from_father = (prob_from_father * (1 - PROBS['mutation'])
                       + (1 - prob_from_father) * PROBS['mutation'])
                        
        return not_from_mother*from_father + from_mother*not_from_father

    if num_genes == 2:
        from_mother = (prob_from_mother * (1 - PROBS['mutation'])
                       + (1 - prob_from_mother) * PROBS['mutation'])
        from_father = (prob_from_father * (1 - PROBS['mutation'])
                       + (1 - prob_from_father) * PROBS['mutation'])
        return from_mother*from_father

    return 0
    


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    jp = 1
    
    for name in people:
        num_genes = 1 if name in one_gene else 2 if name in two_genes else 0
        trait = name in have_trait
        prob_gene = compute_prob(name, num_genes, people, one_gene, two_genes)
        prob_trait = PROBS['trait'][num_genes][trait]
        jp *= prob_gene*prob_trait

    return jp


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for name in probabilities:
        num_genes = 1 if name in one_gene else 2 if name in two_genes else 0
        trait = name in have_trait
        probabilities[name]['gene'][num_genes] += p
        probabilities[name]['trait'][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for name in probabilities:
        gene = probabilities[name]['gene']

        n = sum(gene.values())

        for k in gene:
            gene[k] /= n
        
        trait = probabilities[name]['trait']

        n = sum(trait.values())

        for k in trait:
            trait[k] /= n


if __name__ == "__main__":
    main()
