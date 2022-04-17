# JWT service

JWT service for generating and refreshing tokens.

### Technologies

<ul>
    <li>Python = 3.8.10</li>
    <li>FastAPI = 0.75.1</li>
</ul>


### Install and run 

1. Clone repo: `git clone git@github.com:TeamSchedule/jwt.git`
2. Run service standalone with:
    1. Dockerfile:<br/>
   `docker build --tag jwt:latest -f Dev.dockerfile .`<br/>
   `docker run --rm -it -p 8080:8080 jwt:latest`<br/>

    2. Python:<br/>
    `pip install --user poetry`<br/>
    `poetry install`<br/>
    `uvicorn jwt_service.main:app --host 0.0.0.0 --port 8080 --reload`<br/>
