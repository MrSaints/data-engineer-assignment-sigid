from typing import Dict, List

from sigid.service import AnySignature


class MockSignatureRepository:
    def __init__(self):
        self.signatures_by_signee_id: Dict[str, List[AnySignature]] = {}

    def store(self, signatures: List[AnySignature]) -> None:
        for signature in signatures:
            print("[MockSignatureRepository] storing signature:", signature)

            existing_signatures = self.signatures_by_signee_id.get(
                signature.signee_id, []
            )
            signatures_to_store = [*existing_signatures, signature]
            self.signatures_by_signee_id[signature.signee_id] = signatures_to_store
