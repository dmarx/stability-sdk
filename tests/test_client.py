import pytest

from stability_sdk import client


def test_client_import():
    from stability_sdk import client
    assert True

def test_StabilityInference_init():
    class_instance = client.StabilityInference(key='thisIsNotARealKey')
    assert True

def test_StabilityInference_init_nokey_error():
    try:
        class_instance = client.StabilityInference()
        assert False
    except ValueError:
        assert True

def test_StabilityInference_init_nokey_insecure_host():
    class_instance = client.StabilityInference(host='foo.bar.baz')
    assert True

@pytest.mark.parametrize("sampler_name", client.algorithms.keys())
def test_get_sampler_from_str_valid(sampler_name):
    client.get_sampler_from_str(s=sampler_name)
    assert True
