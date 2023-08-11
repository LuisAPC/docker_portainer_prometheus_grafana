"""
--------------------------Docker----------------------------
One of the most important trends in the IT world.
It has changed the way we develop and deploy applications.

How traditionally we developed or deployed applications:
    1. You would need to install your development application first.
        Set up a Linux server
        Install web server like Apache or nginx
        Database like MySQL
        Deploy libraries and frameworks needed to run your
            application on a server
    2. Run, test and deploy your application

The problem when you develop an application is that you probably want
to deploy it somewhere else or share it with someone who wants to
deploy it in its own environment. Not every environment will look the
same (different versions, different databases, different config files,
different Linux distros). There are many edge cases you want to
consider.

Docker introduces containers: an isolated environment to run your
application. It is like a virtual machine, but different because vms
come with a full OS, which is very heavyweight. A container only has
the necessary libraries and things you need to run your application.
It is lightweight, boots and runs in seconds, and is very scalable.

2 key features that make containers so powerful:
    Deployment: To create a containerized application and deploy it
        you just need a collection of necessary frameworks,
        libraries and dependencies needed in an OS to run your
        application.
        From here you would create an image which is a template
        for your container. It creates an illusion for the
        container to run an application.

    Scalability: Easy scalable and fast boot up. This is key when
        working with cloud.

If you want to run Linux docker containers on windows, you need to
install docker and a vm to run it.
    Running your first docker container:
            Docker container always runs from an image which are
            distributed via docker hub.
        docker run hello-world
            To run a docker container.
        docker ps -a
            Show all your docker containers and not just the ones
            running.
        docker run hello-world
            It would create another container, not just use the
            one you already have.
        docker run --name webserver -p 80:80 -d nginx
            If you want to run the same container instead of
            creating a new one, use docker start. Here we deployed
            a web server with an image based on the web server
            nginx.

To access the container:
    1. Open a Web browser and type localhost:80

Containers don't have any persistent storage by default. That
means that if we stop or close the container, and run it again, all
of the changes made to the directory or files inside the container
will be gone.

Obviously, you need storage. In docker this is done via volumes,
which are persistent storages that you can attach to a specific
location inside a container.
    docker stop webserver
    docker rm webserver
    docker images
        To see my downloaded images
    mkdir websites
    docker run --name webserver -p 80:80 -d -v
         ~/websites:/usr/share/nginx/html nginx

To view that web page by granting permissions:
    chmod 777 websites
    cd websites
    ls
    vim index.html
        <body>
            <h1>Docker is awesome!</h1>
        </body>
        :wq
    refresh page

Now, if we stopped the container, and run it again, we would have
everything saved.

You can go to hub.docker.com to view all of the available images

To stop all running containers:
    docker stop $(docker ps -a -q)

to run all containers:
    docker start $(docker ps -a -q)

"""
