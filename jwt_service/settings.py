import os


JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", 'kXpBmV^_|BFq#c.-""B:cd#k6-/EuVp]')

if JWT_SECRET_KEY == '' or JWT_SECRET_KEY is None:
    raise ValueError("JWT_SECRET_KEY must be specified")
