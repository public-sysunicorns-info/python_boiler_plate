
#!/usr/bin/env bash

docker stop python_boilerplate
docker rm python_boilerplate

docker run \
    --name python_boilerplate \
    -p "8080:8080" \
    python_boilerplate:manual
