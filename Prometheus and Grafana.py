"""
----------Introduction to Prometheus and Grafana: ----------
Monitoring and analytics tools

Showing CPU memory disk, network utilization via a dashboard
Centralized monitoring system (everything accessible from one UI)
Track errors
Notify when thresholds are reached.

Two different monitoring techniques:
LOGS = track events with specific details about the nature and type of it
METRICS = counts, threshold numbers, statistics such as CPU and memory
    utilizations

PROMETHEUS-----------------------------------------------------
Monitoring system that stores all the metrics in a giant database
It is mainly to collect and store data not to visualize it.

GRAFANA--------------------------------------------------------
Web UI that queries metrics from Prometheus using PromQL
Used to visualize information in a friendly dashboard.

USING/INSTALLING THEM WITH DOCKER------------------------------
https://www.youtube.com/watch?v=9TJx7QTrTyo&ab_channel=ChristianLempa

"""
