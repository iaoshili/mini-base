# mini-base
**Reference: https://testdriven.io/courses/auth-flask-react/react-and-docker/**

Basic code for starting a new project

Go to http://localhost:3007/ for the react app (Comment out the client section in docker-compose for faster build in case you are not using react)

For REST, go to:
http://localhost:5001/ping

For Flask admin, go to:
http://localhost:5001/admin/user/


# Workflow using VSCode (Highly recommend)
(install remote container extension)
- remote-containers: reopen in container
(That's it, you get auto complete, per function run test, everything)

# Workflow if you are not using VSCode
- Build and run: make run
- Create db and dummy data: make builddb
- Run test: make test

# To copy these to your folder
- clone this repo
- `rsync -av --progress mini-base/ <your awesome directory> --exclude .git`

# Features
- Global cache with Redis
- A message queue worker
- Added a sample Mongodb model in models.py
