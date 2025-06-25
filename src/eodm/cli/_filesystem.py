from typing import Optional

import botocore.session
import fsspec


def _get_fsspec_fs(protocol: str, profile: Optional[str]) -> fsspec.AbstractFileSystem:
    """Get fsspec filesystem with proper credential handling."""
    if protocol == "s3":
        session = (
            botocore.session.Session(profile=profile)
            if profile
            else botocore.session.Session()
        )
        creds = session.get_credentials()
        config: dict = session.get_scoped_config()

        region = config.get("region")
        endpoint_url = config.get("endpoint_url")

        return fsspec.filesystem(
            "s3",
            key=creds.access_key if creds else None,
            secret=creds.secret_key if creds else None,
            token=creds.token if creds else None,
            client_kwargs={
                "region_name": region,
                "endpoint_url": endpoint_url,
            },
        )
    return fsspec.filesystem(protocol)
