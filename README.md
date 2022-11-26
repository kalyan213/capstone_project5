[![CircleCI](https://dl.circleci.com/status-badge/img/gh/kalyan213/capstone_project5/tree/main.svg?style=svg&circle-token=37287e8153b2e37d549cae3b3547cdaccc7fc90a)](https://dl.circleci.com/status-badge/redirect/gh/kalyan213/capstone_project5/tree/main)

# Cloud DevOps Engineer Capstone Project

This project represents the successful completion of the last final Capstone project and the Cloud DevOps Engineer Nanodegree at Udacity.

This deploys a static page .

## Technologies used:

*	Docker
*	Kubectl
*	Eksctl
*	CircleCI
*	GitHub
*	Python
*	

Steps:
******

1) Docker file is tested using a hadolint

2) Build a Docker image for the python flask app

3) Upload the Docker image into Docker Hub

4) Create Kubernetes cluster in AWS (EKS) 

5) Create Service as loadbalancer and web hosts for  high availability

6) Deploy a docker container from a docker HUB

7) An application is deployed and running on EKS cluster

8) Now, there is an update to the webpage and it has to be re-deployed. The challenge is what type of deployment strategy needed to use
   so that the clients faces the minimal downtime. 
   
   Here we have used the rolling update strategy
   ---------------------------------------------
   It is a gradual process that allows you to update your Kubernetes system with only a minor effect on performance and no downtime. 
   In this strategy, the Deployment selects a Pod with the old programming, deactivates it, and creates an updated Pod to replace it.

9) Firstly, as a best practice ensure to take a backup of old application either using version control etc
   Here I have used to tagging approach to TAG the docker image as V1,V2,V3 etc
   So in case of roll back can change the build order version and re-apply the settings
   
10) V1 tag is old-application, V2 tag us updated version 

11) Once the V2 is ready, push it to docker hub with V2 tag. Modify the Kubernetes configuration to pull
    updated version, then add the rolling strategy configuration so whenvever a changes in application it uses
    rolling update strategy to redeploy a update code

12) The entire process to deploy the latest version is via a CIRCLECI code pulled from gitrepo

13) Please refer to URL file to get the LB details

