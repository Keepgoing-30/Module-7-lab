"""
Task 1: AI Search & Optimization Paradigm
Implement the genetic operators to optimize power line allocations.
"""
import random

def genetic_crossover(parent_a: list[int], parent_b: list[int]) -> tuple[list[int], list[int]]:
    """
    TODO: Implement Single-Point Crossover.
    Find the midpoint of the parent arrays. Create two children where:
    Child 1 gets Parent A's first half and Parent B's second half.
    Child 2 gets Parent B's first half and Parent A's second half.
    """
    if len(parent_a) != len(parent_b):
        raise ValueError("Parent chromosomes must be the same length.")

    midpoint = len(parent_a) // 2
    child_1 = parent_a[:midpoint] + parent_b[midpoint:]
    child_2 = parent_b[:midpoint] + parent_a[midpoint:]
    return child_1, child_2


def genetic_mutation(chromosome: list[int], mutation_rate: float) -> list[int]:
    """
    TODO: For each bit/gene in the chromosome list, roll a random float between 0 and 1.
    If the roll is less than mutation_rate, flip the bit (0 becomes 1, 1 becomes 0).
    Return the mutated chromosome list.
    """
    mutated = []
    for gene in chromosome:
        if random.random() < mutation_rate:
            mutated.append(1 - gene)
        else:
            mutated.append(gene)
    return mutated
