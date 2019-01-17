from typing import List

from sigid.mock_asset_service import MockAssetService
from sigid.mock_signature_repository import MockSignatureRepository
from sigid.mock_signee_repository import MockSigneeRepository
from sigid.service import (
    AnyNewSignature,
    NewImageSignature,
    NewXYZSignature,
    SignatureApplicationService,
)

if __name__ == "__main__":
    # Data stores
    signee_repository = MockSigneeRepository()
    signature_repository = MockSignatureRepository()

    # Services
    asset_service = MockAssetService()
    application = SignatureApplicationService(
        signee_repository=signee_repository,
        signature_repository=signature_repository,
        asset_service=asset_service,
    )

    # Test data
    test_signatures: List[AnyNewSignature] = [
        NewImageSignature(local_uri="/tmp/does_not_actually_exist"),
        NewXYZSignature(x=1.0, y=2.0, z=3.0),
    ]

    # Use test data
    application.register_signatures(test_signatures)

    # Check if test data is stored in the mock data stores
    print("Signees:", signee_repository.signee_by_id)
    print("Signatures:", signature_repository.signatures_by_signee_id)
    print("Assets:", asset_service.asset_by_id)
