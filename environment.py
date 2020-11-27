class Environment:
    """ Implementation of the triange checkers puzzle environment """

    AVAILABLE_TRIPLES = [
        [0, 2, 5],
        [2, 5, 9],
        [5, 9, 14],
        [1, 4, 8],
        [4, 8, 13],
        [3, 7, 12],
        [0, 1, 3],
        [1, 3, 6],
        [3, 6, 10],
        [2, 4, 7],
        [4, 7, 11],
        [5, 8, 12],
        [3, 4, 5],
        [6, 7, 8],
        [7, 8, 9],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
    ]

    def __init__(self):
        pass

    def env_init(self, init_state=None):
        """ Setup the environment to initial state """
        if init_state:
            assert len(init_state) == 15, "State needs to have 15 positions"
            assert set(init_state) < set([0, 1]), "Only 1 and 0 are valid values"
            self.state = init_state
        else:
            self.state = [1] * 15
            self.state[4] = 0

    def env_start(self):
        """The first method when environment starts, before first action

        Returns:
            The first state observed
        """
        return self.state

    def env_step(self, action):
        """Interact with the environment by selecting given action
        Args:
            action: The action taken
        Returns:
            (float, state, Boolean): tuple of the reward, new state,
                and boolean indicating if it's terminal.
        """
        pass

    def available_actions():
        """Next available actions from given state
        Return:
            list of next valid actions
        """
        pass
