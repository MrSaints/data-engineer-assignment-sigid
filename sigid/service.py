from typing import Dict, List, Optional, Union

import pydantic
import ulid
from typing_extensions import Protocol

from sigid.entity import AnySignature, Signee


class BaseNewSignature(pydantic.BaseModel):
    metadata: Optional[Dict[str, str]] = {}


class NewImageSignature(BaseNewSignature):
    local_uri: str


class NewXYZSignature(BaseNewSignature):
    x: float
    y: float
    z: float


AnyNewSignature = Union[NewImageSignature, NewXYZSignature]

# Protocols are essentially interfaces.
# See: https://mypy.readthedocs.io/en/latest/protocols.html#simple-user-defined-protocols


class SigneeRepository(Protocol):
    def store(self, signee: Signee) -> None:
        ...


class SignatureRepository(Protocol):
    def store(self, signatures: List[AnySignature]) -> None:
        ...


class AssetService(Protocol):
    def register_asset(
        self, local_uri: str, metadata: Optional[Dict[str, str]] = {}
    ) -> str:
        ...


class SignatureApplicationService:
    def __init__(
        self,
        signee_repository: SigneeRepository,
        signature_repository: SignatureRepository,
        asset_service: AssetService,
    ):
        self.signee_repository = signee_repository
        self.signature_repository = signature_repository
        self.asset_service = asset_service

    def register_signatures(
        self, new_signatures: List[AnyNewSignature], idempotence_key: str = ""
    ):
        new_signee = Signee()
        self.signee_repository.store(new_signee)

        signatures: List[AnySignature] = []

        for new_signature in new_signatures:

            if isinstance(new_signature, NewImageSignature):
                asset_id = self.asset_service.register_asset(
                    local_uri=new_signature.local_uri, metadata=new_signature.metadata
                )
                signatures.append(new_signee.new_image_signature(asset_id=asset_id))
            else:
                signatures.append(
                    new_signee.new_xyz_signature(
                        x=new_signature.x, y=new_signature.y, z=new_signature.z
                    )
                )

        self.signature_repository.store(signatures)
