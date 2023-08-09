"""
----------Introduction to Prometheus and Grafana: ----------
Monitoring and analytics tools.

Showing CPU, memory disk, network utilization via a dashboard.
If you are hosting a lot of stuff at home or you have productions
    servers running somewhere and you whant to monitor them,
    normally it is a big challenge because every thing has its own
    web UI, switch to different OS etc.
Centralized monitoring system (everything accessible from one UI).
Track errors.
Notify when thresholds are reached.

Server monitoring is all about identifying bottlenecks in resources.

Two different monitoring techniques:
    LOGS = track events with specific details about the nature and type
            of it
        So if something happens it is a good idea to look in the logs
            file to see what happened in that particular point in time

    METRICS = counters, thresholds, numbers, statistics such as CPU and
        memory utilizations

You probably don't want to collect all of this data manually for every
    server or aplication. This is why having a centralized server to
    collect all this data is very useful.

PROMETHEUS------------------------------------------------------------
Monitoring system that stores all the metrics in a giant database
It is mainly to collect and store data not to visualize it.

Architecture and how it works:
    First you need to deploy the prometheus server which pulls metrics
        from different targets
    You configure all systems and services you want to collect metrics
        from inside prometheus configuration file
    Prometheus initiates the connection to all configure targets and
        scrapes the metrics ina specific interval. This targets are
        not necessarily physical or virtual servers. A target can
        represent a physical device, a virtual server (linux machine,
        docker daemons, kubernetes clusters, etc).
    Prometheus offers a simple interface to query and read this data,
        but it's mainly there for collecting and storing it, NOT TO
        VISUALIZE IT. This is why youi need another aplication: Grafana.

Has an alert system which can send you notifications in case of a specific
    event.

GRAFANA------------------------------------------------------------------
Visualize and monitor tool that displays information in a dashboard.

Architecture and how it works:
    Web UI that queries metrics from Prometheus using PromQL

DEPLOYMENT OF THESE TOOLS USING DOCKER AND PORTAINER---------------------
You can install them on a linux OS, but we are using Docker and Portainer.

1. Go to the Portainer web UI
    To deploy Prometheus, Grafana and other exporters that we will need to
        collect the metrics.
    Do the basics steps from other tutorials to get portainer up and running

2. Go to the prometheus-grafana folder in this tutorial and copy the
    compose.yaml file

3. In the portainer web UI, selct the portainer server, stacks, add new
stack.
    Call it monitoring and paste the compose.yaml file
    It probably won't work yet because we haben't created this configuration
        file for pometheus (if you go the the logs of promeheus container,
        you can see that it fails to open promehteus.yaml)

4. Create the configuration file that Promehteus can operate
        Go to the terminal of your home server
    sudo mkdir /etc/prometheus
        Create folder under etc folder
    sudo vim /etc/prometheus/prometheus.yaml
        Create config file inside the folder
        Paste content inside the prometheus-config folder and save (this
            file will listen to the data of prometheus itself)

5. Go to portainer and restart the prometheus container
    You can check inside the logs file to verify that everything is fine

6. Click on the prometheus Published Ports and click on the port 9090
to verify that we can oper the web UI
    In the Prometheus web UI you can click on Status -> TSDB Status
        To get infromation about the server health status
        And you can see that it is working because it is pulling some metrics
    Check targets and their states
        Status -> Targets

7. Query some metrics inside prometheus
    In the main page of prometheus you can also put in an expression using
        PromQL
    Go to home page (click on promeheus logo)
    If you click on the world icon next to Execute you can see a bunch of
        pre-made metrics. As you can see it can be a little bit overwhelming
        but that is because as we said prometheus is not made for
        visualization. We would be able to see all of this data in Grafana.

ADDING MORE METRICS (THIRD-PARTY EXPORTERS)----------------------------------
For a Linux server, a docker stack, etc.
Prometheus has a bunch of exporters and integratios that allows us to do that.
1. The 2 main exporters that will be covered here are:
    Node/system metrics exporter (although not recommended to deploy as a
        Docker container because it requires access to the host system)
        The problem with this exporters (that retrieve resourse data, such as
        cpu memory) always require privileges to access specific files. So
        mounting the root directory inside the docker container is necesary.
        This is why is not recommended, yet it is set to read only.
            1. Copy the docker-compose file under the node_exporter folder in
                this repo
            2. Edit the monitoring stack and add that code below grafana
                definition.

    cAdvisor to monitor docker containers. There are Docker exporters but this
        one is maintained by google
            1. Copy the docker-compose file under the cadvisor folder in
                this repo
            2. Edit the monitoring stack and add that code below node_exporter
                definition.

2. Update stack and redeploy

3. Get the metrics we just added inside prometheus
    Inside the terminal, go to sudo cd /etc/prometheus
    sudo vim prometheus.yml
        Uncomment example job for node_exporter. You can see that we are using
            the DNS name as well, which is only possible if you deploy all the
            containers in the same docker compose stack. This way they are
            located in the same isolated network of docker, allowing them to
            find each other by DNS name
        Uncomment example job for cadvisor.
    Save and restart Prometheus container

4. Do to prometheus web UI and verify that you are tracking those added metrics
    Status -> targets
        Everything hould be with an UP State

==========================VISUALIZE DATA IN GRAFANA============================
We already deployed Grafana in Portainer, so simply just go to localhost:3000
1. Go to home, click on Data Sources (add your first data source)

2. Select Prometheus
    Add HTTP URL: http://promehteus:9090 (http://localhost:9090)
    Click Save & Test

3. Go to home, click on Dashboards (Create your first dashboard)
    Add visulization
    Select promehteus

4. Go to metric and select metric
    Search and select container_memory_rss
    You don't have to build this yourself, you can use a dashboard template
        https://grafana.com/grafana/dashboards/
    Search for:
        node exporter full
        cadvisor exporter

5. Click on desired dashboard and copy dashboard id

6. Go to your grafana UI -> dashboards -> New (drop down menu) -> import
    Paste dashboard id and click on load
    Select Prometheus data source and click on import


"""
