from modelkey.adapters.nx.adapter import NXAdapter


class FakeCollection(list):
    pass


class FakePart:
    Leaf = "test_part.prt"
    FullPath = "C:/tmp/test_part.prt"
    Features = FakeCollection([1, 2, 3, 4])
    Expressions = FakeCollection([1, 2])
    Sketches = FakeCollection([1])


class FakeParts:
    Work = FakePart()


class FakeSession:
    Parts = FakeParts()

    def GetEnvironmentVariableValue(self, key):
        return "NX-TEST-1.0" if key == "UGII_FULL_VERSION" else ""


class FakeNoPartSession(FakeSession):
    class Parts:
        Work = None


def test_nx_adapter_reports_active_part_from_injected_session():
    health = NXAdapter(session=FakeSession()).health()
    assert health.connected is True
    assert health.nx_version == "NX-TEST-1.0"
    assert health.active_part is not None
    assert health.active_part.name == "test_part.prt"
    assert health.active_part.feature_count == 4
    assert health.active_part.expression_count == 2
    assert health.active_part.sketch_count == 1


def test_nx_adapter_handles_connected_session_without_work_part():
    health = NXAdapter(session=FakeNoPartSession()).health()
    assert health.connected is True
    assert health.active_part is None
    assert "no work part" in health.message.lower()
