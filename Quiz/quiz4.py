"""This quiz is a simplified version of 2020 presidential election. Write a definition for a class named Candidate
with the following methods:

1, An __init__ method that initializes name, winning_states and number of votes.
2, A __str__ method that returns a string representation of this candidate, including name and winning state(s).
3, A method named win_state that takes a string of state abbreviation, adds it to winning_states and update votes.
4, A special method that overloads the operator '>' to compare votes of two candidates.

DO NOT change code in main method!

--------------------------------------------------------------
--------------------------------------------------------------
The expected outputs should be like below :


Donald Trump has not won any state yet.
Elizabeth Warren has won MA.

After election:
Donald Trump has won FL, TX.
Elizabeth Warren has won MA, CA.

Does Trump win?
True
--------------------------------------------------------------
--------------------------------------------------------------
"""

ELECTORS = {"CA": 55, "TX": 38, "FL": 29, "MA": 11}

class Candidate:
    """
    The presidential candidate


    attributes: name, winning_states, votes
    """

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate, including name, winning_states and votes

        name: string
        winning_states: a list of strings representing initial winning state(s).
        """
        self.name = name
        self.winning_states = winning_states or []
        self.votes = votes
        if winning_states == None:
            self.votes = votes
        else:
            for i in winning_states:
                self.votes += ELECTORS[i]

    def __str__(self):
        """Return a string representation of this candidate,
        including name and winning state(s).
        """
        if self.votes == 0:
            return f'{self.name} has not won any state yet.'
        else:
            states_string = ''
            for i, state in enumerate(self.winning_states):
                states_string += state
                if i != len(self.winning_states) - 1:
                    states_string += ', '
            return f'{self.name} wins {states_string}'

    def __gt__(self, other):
        """Greater than function"""
        return self.votes > other.votes

    def win_state(self, state):
        """Adds a tate to winning_states and updates votes.

        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORS[state]


def main():
    trump = Candidate("Donald Trump")
    warren = Candidate(
        "Elizabeth Warren", winning_states=["MA"]
    )  # of course she wins MA
    print(trump)
    print(warren)
    print()
    print("After election:")
    trump.win_state("FL")
    trump.win_state("TX")
    warren.win_state("CA")
    print(trump)
    print(warren)
    print()
    print("Does Trump win?")
    print(trump > warren)

if __name__ == '__main__':
    main()
