import pytest

from APIlist.addbookapi import AddBook
from utilities.resultstatus import ResultStatus


class TestAddDelete:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ab = AddBook()
        self.ts = ResultStatus()

    def test_addbook(self):
        self.ab.updatebook()
        msgy = self.ab.validateaddbook()
        self.ts.marktestfinal(msgy, "AddBook", "test_addbook")

    def test_deletebook(self):
        self.ab.updatebook()
        dele= self.ab.validatedelete()
        self.ts.marktestfinal(dele, "DeleteBook", "test_deletebook")