import os

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", 'kXpBmV^_|BFq#c.-""B:cd#k6-/EuVp]')
USER_SERVICE_HOSTS = os.environ.get("USER_SERVICE_HOSTS", None)

if JWT_SECRET_KEY == '' or JWT_SECRET_KEY is None:
    raise ValueError("JWT_SECRET_KEY must be specified")

if USER_SERVICE_HOSTS is None:
    raise ValueError("USER_SERVICE_HOSTS must be specified")
