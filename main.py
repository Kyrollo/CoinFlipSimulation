import random

def coin_flip():
    """Simulate a coin flip and return 'H' for heads or 'T' for tails."""
    return random.choice(('H', 'T'))

def calculate_percentages(outcome_list):
    """
    Calculate the percentage of heads and tails in the given list of outcomes.
    
    Parameters:
    outcome_list (list): A list of 'H' and 'T' representing coin flip outcomes.
    
    Returns:
    dict: A dictionary with the percentage of heads ('H') and tails ('T').
    """
    length = len(outcome_list)
    heads_count = outcome_list.count('H')
    return {'H': heads_count / length * 100, 'T': (length - heads_count) / length * 100}

def run_trials(num_trials, flips_per_trial):
    """
    Run a specified number of trials of coin flips and print the average percentages of heads and tails.
    
    Parameters:
    num_trials (int): The number of trials to run.
    flips_per_trial (int): The number of coin flips per trial.
    """
    head_percents = []
    tail_percents = []

    for _ in range(num_trials):
        outcomes = [coin_flip() for _ in range(flips_per_trial)]
        percentages = calculate_percentages(outcomes)
        head_percents.append(percentages['H'])
        tail_percents.append(percentages['T'])

    avg_head_percent = sum(head_percents) / len(head_percents)
    avg_tail_percent = sum(tail_percents) / len(tail_percents)

    print(f"Average Head Percentage: {avg_head_percent:.2f}%")
    print(f"Average Tail Percentage: {avg_tail_percent:.2f}%")

# Example usage: Run 100 trials with 1000 coin flips each
run_trials(100, 1000)
