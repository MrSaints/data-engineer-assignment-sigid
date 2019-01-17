from typing import Dict, Optional

import ulid


class MockAssetService:
    def __init__(self):
        self.asset_by_id: Dict[str, str] = {}
        self.metadata_by_asset_id: Dict[str, Dict[str, str]] = {}

    def register_asset(
        self, local_uri: str, metadata: Optional[Dict[str, str]] = {}
    ) -> str:
        print("[MockAssetService] registering asset:", local_uri, metadata)

        asset_id = ulid.new().str
        self.asset_by_id[asset_id] = local_uri
        if metadata:
            self.metadata_by_asset_id[asset_id] = metadata
        return asset_id
