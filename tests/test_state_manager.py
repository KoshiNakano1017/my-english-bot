import services.state_manager as state_manager


def test_state_manager_exports():
    assert hasattr(state_manager, "get_state")
    assert hasattr(state_manager, "update_state")
    assert hasattr(state_manager, "increment_turn")
    assert hasattr(state_manager, "get_user_state")
    assert hasattr(state_manager, "update_user_setting")
