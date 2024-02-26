#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#

#SQLALCHEMY_DATABASE_URI = 'crate://crate@cratedb:4200'
#SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pguser:pgpwd@some.host/superset"
#SQLALCHEMY_ECHO = True

# https://www.restack.io/docs/superset-knowledge-superset-redis-caching
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400, # 24 hours in seconds
    'CACHE_KEY_PREFIX': 'superset_filter_cache',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_explore_cache',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}

FEATURE_FLAGS = {
    "THUMBNAILS": True,
    "THUMBNAILS_SQLA_LISTENERS": True,
}

# https://www.restack.io/docs/superset-knowledge-apache-superset-config-guide
PREFERRED_DATABASES = ['CrateDB', 'PostgreSQL', 'MySQL']

SECRET_KEY='J0L4j7tRN3DpewJkowyZZgYx1qZb3iE0'
MAPBOX_API_KEY='pk.eyJ1IjoibmV0bGl0ZSIsImEiOiJjbHN4ZWxmcTEwMjB3Mm5saXB0Y2hkbnNxIn0.gtzgRk8ollA-d914dbiuTw'