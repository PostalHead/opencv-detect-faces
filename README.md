# opencv-detect-faces
## Building
```bash
docker build --build-arg USER_ID=$(id -u) -t postalhead/opencv-detect-faces .
```
## Running
```bash
docker run --rm -v "/path/to/images/:/app/img" postalhead/opencv-detect-faces
```
or
```bash
docker run --rm -v "/path/to/images/:/app/img" postalhead/opencv-detect-faces --image "/app/img/image"
```
