import random

def coin_flip():
    return random.choice(('H', 'T'))

def calculate_percentages(outcome_list):
    length = len(outcome_list)
    heads_count = outcome_list.count('H')
    return {'H': heads_count / length * 100, 'T': (length - heads_count) / length * 100}

def run_trials(num_trials):
    head_percents = []
    tail_percents = []

    for _ in range(num_trials):
        outcomes = [coin_flip() for _ in range(1000)] # Flip the coin 1000 times for each trial
        percentages = calculate_percentages(outcomes)
        head_percents.append(percentages['H'])
        tail_percents.append(percentages['T'])

    avg_head_percent = sum(head_percents) / len(head_percents)
    avg_tail_percent = sum(tail_percents) / len(tail_percents)

    print(f"Average Head Percentage: {avg_head_percent:.2f}%")
    print(f"Average Tail Percentage: {avg_tail_percent:.2f}%")

# Run 100 trials
run_trials(100)