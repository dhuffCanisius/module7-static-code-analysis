#!/bin/bash
pylint cyb600_module7/ --output-format=parseable > .pylint-report.txt
docker run \
    --rm \
    --net host \
    -e SONAR_TOKEN="squ_15ca729ac650abe954ddcfe7c7c129c1a8b6c124" \
    -e SONAR_HOST_URL="http://localhost:9000" \
    -v "${PWD}:/usr/src" \
    sonarsource/sonar-scanner-cli