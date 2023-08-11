'''
-------Develop Python applications inside a Docker container with VSC--------

Develop you python apps in your linux subsystem------------------------------
1. Get WSL

2 Download Ubuntu from Microsoft store

3. We need two extensions in VSC:
    Docker
    Remote WSL

4. Click on bottom left corner and connect to the remote window
    You may need to restart VSC

Now you can run python using VSC in your linux subsystem!

Develop you python apps in a Docker container--------------------------------
1. Click on F1
    Select Add Docker Files to Workspace or Docker Compose
    Select Aplication Platform (in this case Python General)
    Select entry point or main file
    Select if you want to include a docker compose file

2. Build image
    docker build . (build image of current directory) or
    left click on the dockerfile file and click on build image

    docker image ls (to verify that the image was created)

3. Execute container
    docker run name_of_image

'''
