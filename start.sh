#!/bin/bash

work_dir=`pwd`

docker rm http_svr
docker run -it -p 8008:80 -v "$work_dir:/code" --name http_svr http_svr:release
