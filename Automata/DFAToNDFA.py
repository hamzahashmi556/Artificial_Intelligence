def epsilon_closure(states, transition_function):
    closure = set(states)
    stack = list(states)

    while stack:
        current_state = stack.pop()
        if (current_state, '') in transition_function:
            for next_state in transition_function[(current_state, '')]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)

    return frozenset(closure)


def move(states, input_char, transition_function):
    next_states = set()

    for state in states:
        if (state, input_char) in transition_function:
            next_states.update(transition_function[(state, input_char)])

    return frozenset(next_states)


def nfa_to_dfa(nfa_states, nfa_alphabet, nfa_transition_function, nfa_start_state, nfa_accept_states):
    dfa_states = set()
    dfa_alphabet = set(nfa_alphabet)
    dfa_transition_function = dict()
    dfa_start_state = epsilon_closure({nfa_start_state}, nfa_transition_function)
    dfa_accept_states = set()

    queue = [dfa_start_state]
    state_mapping = {dfa_start_state: 'q0'}
    dfa_counter = 0

    while queue:
        current_states = queue.pop(0)

        if current_states not in dfa_states:
            dfa_states.add(current_states)

            if nfa_accept_states.intersection(current_states):
                dfa_accept_states.add(current_states)

            for input_char in dfa_alphabet:
                next_states = epsilon_closure(move(current_states, input_char, nfa_transition_function),
                                              nfa_transition_function)

                if next_states:
                    if next_states not in state_mapping:
                        dfa_counter += 1
                        state_mapping[next_states] = f'q{dfa_counter}'
                        queue.append(next_states)

                    dfa_transition_function[(state_mapping[current_states], input_char)] = state_mapping[next_states]

    return dfa_states, dfa_alphabet, dfa_transition_function, 'q0', dfa_accept_states


if __name__ == '__main__':
    nfa_states = {'q0', 'q1', 'q2'}
    nfa_alphabet = {'a', 'b'}
    nfa_transition_function = {
        ('q0', 'a'): {'q1'},
        ('q0', ''): {'q2'},
        ('q1', 'b'): {'q2'},
        ('q2', 'a'): {'q0'},
        ('q2', 'b'): {'q1'}
    }
    nfa_start_state = 'q0'
    nfa_accept_states = {'q1'}

    dfa_states, dfa_alphabet, dfa_transition_function, dfa_start_state, dfa_accept_states = \
        nfa_to_dfa(nfa_states, nfa_alphabet, nfa_transition_function, nfa_start_state, nfa_accept_states)

    # Test input strings
    inputs = ['ab', 'a', 'abb', 'ba']

    for input_str in inputs:
        current_state = dfa_start_state
        for char in input_str:
            if (current_state, char) in dfa_transition_function:
                current_state = dfa_transition_function[(current_state, char)]
            else:
                current_state = None
                break

        if current_state and current_state in dfa_accept_states:
            print(f'Accepted: {input_str}')
        else:
            print(f'Rejected: {input_str}')
