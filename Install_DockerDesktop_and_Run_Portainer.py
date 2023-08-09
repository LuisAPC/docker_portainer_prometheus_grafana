"""
----------Install Docker Desktop and Run Portainer:----------
DOCKER=
1. have wsl (Windows Subsystem for Linux) installed

2. Download Ubuntu (in my case I will use Ubuntu-22.04)

3. In terminal run:
    wsl -l -v
        Verify is wsl version 2 or follow to change it:
            https://learn.microsoft.com/en-us/windows/wsl/install

4. Install Docker desktop
    Once inside go to settings -> Resources -> WSL Integration
        Enable and apply & Restart

5. Go to WSL terminal (Ubuntu) and run a couple commands to verify
    that everything is correct
        cd: Go to home dicercoty via
        docker -v: version
        docker run hello-world: run a container
        docker-compose -v

PORTAINER & DOCKER=
https://adamtheautomator.com/docker-portainer/

1. To install a volume where portainer is going to store its data
    docker volume create portainer_data

2. Create a Portainer container
    docker container run -d -p 8000:8000 -p 9000:9000 --name=portainer \
        --restart=always \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v portainer_data:/data portainer/portainer-ce
            -d: run in detached mode (in the background to keep using terminal)
            -p 8000: portainer agent, to connect remote servers
            -p 9000: for the web interface, the one we want to expose
            -v: append volume to manage local docker resources (if you want to
                only manage remote servers, you can skip this)
            -v: use community edition of portainer


3. Check if container is running
    docker ps

4. Access portainer in localhost
    http://localhost:8080

5. Create user

6. Connect to local docker environment

7. Click on your local environment

8. Click on container
    You can see the 2 containers we created, which are:
        portainer and hello-world

=====To Remove portainer======
docker stop portainer
docker remove portainer
docker ps
docker pull portainer/portainer-ce:latest
docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v
 /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/
portainer-ce

=====Reset Paswword=====
docker stop "id-portainer-container"
docker pull portainer/helper-reset-password
docker run --rm -v portainer_data:/data portainer/helper-reset-password
docker start "id-portainer-container"
password given = gPf3+0ULBcy1p79mbY>?62_D{X@t8`,N

* Extra: Get a bunch of templates for free!
1. Go to:
    https://github.com/SelfhostedPro/selfhosted_templates
        and copy the url for the templates:
            https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json

2. Go to portainer
    Settings -> add template URL

"""
