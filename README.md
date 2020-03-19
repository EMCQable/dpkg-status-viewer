# dpkg-status-viewer


in dpkgStatusviewer/settings.py, insert settings:

```python
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_STORAGE_BUCKET_NAME =
AWS_S3_REGION_NAME =
AWS_S3_ENDPOINT_URL =
AWS_S3_HOST =

S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': 'uploads/',
        'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],
    },
}
```