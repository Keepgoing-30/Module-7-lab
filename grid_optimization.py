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
    # YOUR CODE HERE
    pass

def genetic_mutation(chromosome: list[int], mutation_rate: float) -> list[int]:
    """
    TODO: For each bit/gene in the chromosome list, roll a random float between 0 and 1.
    If the roll is less than mutation_rate, flip the bit (0 becomes 1, 1 becomes 0).
    Return the mutated chromosome list.
    """
    # YOUR CODE HERE
    pass
