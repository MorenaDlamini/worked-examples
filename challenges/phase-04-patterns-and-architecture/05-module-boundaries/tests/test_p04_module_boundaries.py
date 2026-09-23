"""Acceptance test for 05-module-boundaries.

Phases 2 and later are graded black-box over HTTP, so this skips until the service is running
and `CHALLENGE_BASE_URL` is set. The contract below is a starting point: tighten it to the API
you actually design, in the same commit that makes it pass.
"""
import pytest

pytestmark = pytest.mark.acceptance

requests = pytest.importorskip("requests", reason="pip install requests to run acceptance tests")


def test_the_service_answers(base_url):
    r = requests.get(base_url + "/health", timeout=10)
    assert r.status_code == 200, "the service should report its own health before anything else"


@pytest.mark.xfail(reason="write this stage's real assertion, then remove the xfail")
def test_module_boundaries(base_url):
    raise AssertionError("not yet specified")
