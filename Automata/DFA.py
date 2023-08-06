# DFA

def run_dfa(dfa, initial_state, accepting_states, input_string):
    current_state = initial_state
    for symbol in input_string:
        if symbol not in dfa[current_state]:
            return False
        current_state = dfa[current_state][symbol]

    return current_state in accepting_states


if __name__ == '__main__':
    dfa = {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q2', 'b': 'q0'},
        'q2': {'a': 'q2', 'b': 'q2'}
    }

    initial_state = 'q0'
    accepting_states = ['q2']

    inputs = ['aa', 'bb', 'ab', 'ba', 'aba']
    for input in inputs:
        if run_dfa(dfa, initial_state, accepting_states, input):
            print(f"Accepted {input}")
        else:
            print(f"Rejected {input}")
