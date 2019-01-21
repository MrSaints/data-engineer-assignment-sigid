import abc
from datetime import datetime
from typing import List, Mapping, Optional, Tuple, Union

import pydantic
import ulid
from typing_extensions import Protocol


class BaseSignature(pydantic.BaseModel, abc.ABC):
    signee_id: str


class ImageSignature(BaseSignature):
    asset_id: str

    metadata: Optional[Mapping[str, str]] = {}

    id: Optional[str]
    created: Optional[datetime]

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or ulid.new().str

    @pydantic.validator("created", pre=True, always=True)
    def default_created(cls, v):
        return v or datetime.utcnow()


class XYZPoint(pydantic.BaseModel):
    x: float
    y: float
    z: float


class XYZSignature(BaseSignature):
    points: List[XYZPoint]

    id: Optional[str]
    created: Optional[datetime]

    metadata: Optional[Mapping[str, str]] = {}

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or ulid.new().str

    @pydantic.validator("created", pre=True, always=True)
    def default_created(cls, v):
        return v or datetime.utcnow()


AnySignature = Union[ImageSignature, XYZSignature]


class Signee(pydantic.BaseModel):
    id: Optional[str]
    created: Optional[datetime]

    signatures: Optional[List[AnySignature]] = []

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or ulid.new().str

    @pydantic.validator("created", pre=True, always=True)
    def default_created(cls, v):
        return v or datetime.utcnow()

    def new_image_signature(self, asset_id: str) -> ImageSignature:
        return ImageSignature(signee_id=self.id, asset_id=asset_id)

    def new_xyz_signature(
        self, points=List[Tuple[float, float, float]]
    ) -> XYZSignature:
        transformed_points = [
            XYZPoint(x=point[0], y=point[1], z=point[2]) for point in points
        ]
        return XYZSignature(signee_id=self.id, points=transformed_points)
