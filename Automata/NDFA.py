def process_input(input_string, transition_function, start_state, accept_states):
    current_states = {start_state}

    for input_char in input_string:
        next_states = set()
        for state in current_states:
            if (state, input_char) in transition_function:
                next_states.update(transition_function[(state, input_char)])
        current_states = next_states

    return any(state in accept_states for state in current_states)


if __name__ == '__main__':
    transition_function = {
        ('q0', 'a'): {'q0', 'q1'},
        ('q0', 'b'): {'q1'},
        ('q1', 'a'): {'q2'},
        ('q1', 'b'): {'q2'},
        ('q2', 'a'): {'q2'}
    }
    start_state = 'q0'
    accept_states = {'q2'}

    # Test input strings
    inputs = ['ab', 'a', 'abb', 'ba']

    for input_str in inputs:
        if process_input(input_str, transition_function, start_state, accept_states):
            print(f'Accepted: {input_str}')
        else:
            print(f'Rejected: {input_str}')
