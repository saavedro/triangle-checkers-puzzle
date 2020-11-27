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


def test_available_moves_init_state():
    env = Environment()
    env.env_init()
    available_moves = env.available_actions()
    assert len(available_moves) == 2
    assert (11, 4) in available_moves
    assert (13, 4) in available_moves


def test_available_moves_end_of_game():
    env = Environment()
    env.env_init([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    available_moves = env.available_actions()
    assert len(available_moves) == 0
