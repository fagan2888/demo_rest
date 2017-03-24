#!/usr/bin/env bash
docker-compose build pyrest
docker-compose run -p "6218:8000" pyrest