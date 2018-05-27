user_programm = {
    "q1" : {
        's_0': ("q0", '1', 'L'),
        '0': ("q3", '1', 'R'),
        '1': ("q1", '2', 'R'),
        '2': ("q3", '0', 'R'),
    },
    "q2" : {
        's_0': ("q0", '2', 'C'),
        '0': ("q2", '2', 'R'),
        '1': ("q1", '0', 'R'),
        '2': ("q2", '1', 'R'),
    },
    "q3" : {
        's_0': ("q0", '0', 'R'),
        '0': ("q2", '2', 'L'),
        '1': ("q3", '2', 'C'),
        '2': ("q1", '2', 'L'),
    },
}


user_tape = ['s_0', '0','1', '2', '0', '1', '2', '0', '1', '2', "s_0"]


class Tape():
    tape = []
    head_position = 0
    
    def print_tape(self):
        output = (" ").join(self.tape)
        print(output)

    def move_head(self, direction):
        if direction == 'R':
            self.head_position = self.head_position + 1
        elif direction == 'L':
            self.head_position = self.head_position - 1
        elif direction == 'C':
            self.head_position = self.head_position

        if self.head_position < 0:
            self.tape.insert(0, 's_0')
            self.head_position = 0
        elif self.head_position >= len(self.tape):
            self.tape.insert(self.head_position, 's_0')


    def write(self, head_position, new_obj):

        alphabet= ['0', '1', '2', 's_0']

        if new_obj in alphabet:
            self.tape[head_position] = new_obj
        else:
            return False

class State():
    state = 'q1'
    all_states = ['q0', 'q1', 'q2', 'q3']
    def change_state(self, new_state):
        if new_state in self.all_states:
            self.state = new_state
        else:
            return False

def t_m(user_tape, user_programm):
    new_tape = Tape()
    new_state = State()
    new_tape.tape = user_tape
    prog = user_programm

    while True:
        current_obj = new_tape.tape[new_tape.head_position]
        current_prog_line = prog[new_state.state]

        print(" current obj " + new_tape.tape[new_tape.head_position])
        new_tape.write(new_tape.head_position, current_prog_line[current_obj][1])
        print(" new obj " + new_tape.tape[new_tape.head_position])
        new_tape.move_head(current_prog_line[current_obj][2])

        if current_prog_line[current_obj][0] == 'q0':
            break
        else:
            new_state.change_state(current_prog_line[current_obj][0])

    new_tape.print_tape()
