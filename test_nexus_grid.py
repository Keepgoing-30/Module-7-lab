import pytest
from grid_optimization import genetic_crossover, genetic_mutation
from data_intelligence import calculate_supervised_loss, calculate_euclidean_distance
from smart_agent import build_agent_emergency_prompt

def test_genetic_operators():
    p1 = [1, 1, 1, 1, 0, 0, 0, 0]
    p2 = [0, 0, 0, 0, 1, 1, 1, 1]
    
    c1, c2 = genetic_crossover(p1, p2)
    assert c1 == [1, 1, 1, 1, 1, 1, 1, 1]
    assert c2 == [0, 0, 0, 0, 0, 0, 0, 0]
    
    # Check deterministic mutation bound
    mutated = genetic_mutation([0, 0, 0, 0], mutation_rate=1.0)
    assert mutated == [1, 1, 1, 1]

def test_machine_learning_math():
    act = [10.0, 20.0, 30.0]
    pred = [12.0, 18.0, 30.0]
    
    # Errors: (2)^2 + (-2)^2 + (0)^2 = 4 + 4 + 0 = 8. Mean = 8 / 3 = 2.666...
    assert calculate_supervised_loss(act, pred) == pytest.approx(2.6666, rel=1e-3)
    
    # Distance: sqrt((3-0)^2 + (4-0)^2) = sqrt(9 + 16) = 5.0
    assert calculate_euclidean_distance([0.0, 0.0], [3.0, 4.0]) == 5.0

def test_agentic_prompt_structure():
    report = "Transformer blew up causing structural fires on 5th avenue."
    prompt = build_agent_emergency_prompt(report)
    
    assert "JSON" in prompt.upper()
    assert "severity" in prompt.lower()
    assert "dispatch_unit" in prompt.lower()
    assert report in prompt
