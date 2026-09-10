from modelkey.adapters.mock import MockAdapter


def test_mock_adapter_reports_connected_part():
    health = MockAdapter().health()
    assert health.connected is True
    assert health.active_part is not None
    assert health.active_part.name == "alpha_test.prt"
    assert health.active_part.feature_count == 3


def test_mock_adapter_can_report_unavailable():
    health = MockAdapter(connected=False).health()
    assert health.connected is False
    assert health.active_part is None
