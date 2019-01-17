from typing import Dict

from sigid.service import Signee


class MockSigneeRepository:
    def __init__(self):
        self.signee_by_id: Dict[str, Signee] = {}

    def store(self, signee: Signee) -> None:
        print("[MockSigneeRepository] storing signee:", signee)
        if not signee.id:
            raise Exception("missing signee id")
        self.signee_by_id[signee.id] = signee
