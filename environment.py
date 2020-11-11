class Environment:
    """ Implementation of the triange checkers puzzle environment """

    def __init__(self):
        pass

    def env_init(self):
        """ Setup the environment to initial state """
        pass

    def env_start(self):
        """ The first method when environment starts, before first action

        Returns:
            The first state observed
        """
        pass


    def env_step(self, action):
        """ Interact with the environment by selecting given action
        Args:
            action: The action taken
        Returns:
            (float, state, Boolean): tuple of the reward, new state,
                and boolean indicating if it's terminal.
        """
        pass
