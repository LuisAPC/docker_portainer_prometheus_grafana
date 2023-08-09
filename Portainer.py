"""
--------------------------Portainer----------------------------
Free and open-source tool to manage containers from docker.

Use portainer to manage all our docker resources on the local server.
Also, you can expose this service public on the internet with trusted
    ssl certificates by using a reverse proxy.

USE PORTAINER WITH DOCKER---------------------------------------
1. To install a volume where portainer is going to store its data
    docker volume create portainer_data.

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
    ip a
        type this in terminal to check ip address.
        copy the one from eth0 and paste it with the specified port.
            e.g., 127.0.0.1:9000
    http://localhost:9000
        or just type localhost.

DEPLOY A STACK OF A REVERSE PROXY TO MAKE OUR DATA PUBLIC-----------
1. Go to portainer -> stacks -> add stack
    name the stack as> nginxproxymanager

2. Go to nginxproxymanager folder in this directory and copy the
    docker compose file (for updates on code, check the following link:
    https://nginxproxymanager.com/setup/#using-mysql-mariadb-database)

3. paste it under the web editor section in portainer

4. Click on: deploy the stack

* Up to this point we will create and deploy the two containers from our
    copied file and set up everything as described there.

Note: You could also deploy docker compose files in a yaml file via cli
    of docker compose, BUT then portainer will not have full control over
    the stack because it wasn't deployed via portainer.

5. Click on the stack we just created
    If you scroll down, you can see the two containers we just deployed.
    One is the db and the other the app.
    The app has some published ports: the 81:81 is the web UI of the
        nginxproxymanager

6. Under settings, click on:
    environments -> local -> under public ip enter an ip address
        on terminal, run:
            ip a
                select the inet ip from eth0 and paste it on portainer.

7. Click on update environment

8. Go to stacks -> click on stack we just created -> under the app
    container, click on published ports 81

* Note that this web UI of nginx is an unsecured connection. You could
    also create a proxy host for this UI as well

9. Login in the nginx web UI:
    email: admin@example.com
    password: changeme
        If you sign in for the first time you will need to change the
        administrator email address and password
            the password I used was temporalpassword

10. Get a domain that will point to you public ip address
    Go to https://www.duckdns.org/, log in, and create a sub domain.
    Update the ip of your sub domain to your public ip address.
        You can check your public ip address by typing on the terminal:
            ip a
                Under eth0, copy the inet ip address.

11. Go to the nginx site and add an SSL certificate
    Under the burger menu, click on SSL certificates.
    Click on Add SSL Certificate -> Let's Encrypt
    Enter the domain name created on Duck DNS: something.duckdns.org
        (Without the http://)
    Select: Use a DNS Challenge
    Select DNS Provider = DuckDNS and change the value "your-duckdns-token"
        for the token generated in the DuckDNS website
    Agree on terms.
    Save

12. Click on burger menu -> Hosts -> Proxy Hosts -> Add Proxy Hosts

13. Fill out the required information
    Under Details:
        Domain Names: enter the address you want.
        Forward Hostname / IP: portainer
        Forward Port: 9000
        Enable Block Common Exploits
    Under SSL:
        SSL Certificate: Select the SSL certificate we just created.
        Enable Force SSL
        Enable HTTP/2 Support
        Enable HSTS Enabled
        Agree to terms.
    Click on Save

* If you click on the link, it won't work right away:
    This is because we deployed the nginxproxymanager in a docker
    compose stack. This automatically creates a new network and attach
    the nginxproxymanager to an isolated docker network. The portainer
    container is also running on a separate docker network.
    So, we need to make sure that every docker container you want to
    expose via reverse proxy are running on the same docker network.
    The networks are isolated from each other.
    To interconnect them:

12. Redeploy the portainer container
    docker stop portainer
    docker rm portainer
    - Check which networks are currently running:
        docker network ls
            copy the nginxproxymanager_default network.
    - Close the port 9000 (so no one can access it via that way) and
    add the proxy network.
        docker container run -d -p 8000:8000 --network
             nginxproxymanager_default \
            --name=portainer --restart=always \
            -v /var/run/docker.sock:/var/run/docker.sock \
            -v portainer_data:/data portainer/portainer-ce

13. Go to the proxy browser and click the web link
    It should work!

"""
