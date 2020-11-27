from environment import Environment


def test_init_state():
    env = Environment()
    env.env_init()
    start_state = env.env_start()
    assert start_state == [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_init_defined_state():
    env = Environment()
    init_state = [0] * 15
    env.env_init(init_state)
    start_state = env.env_start()
    assert start_state == init_state
