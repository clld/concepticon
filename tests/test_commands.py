import pytest

from pyconcepticon.test_util import TEST_REPOS

from concepticon.__main__ import main


@pytest.mark.full
def test_init():
    main(['--repos', str(TEST_REPOS), 'init', '--dry-run', '--test'])
