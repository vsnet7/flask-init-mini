import pytest

from run import app

@pytest.fixture
def client():
  app.config
