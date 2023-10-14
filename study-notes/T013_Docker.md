
# DOCKER NOTES : BEGINNING 

-------------------------------------------------------------------------------------

- Topic	 Docker				
- Author   @neeraj-singh-jr	
- Status   Ongoing			
- Created 29/09/2023		    
- Updated  12/10/2023		
-------------------------------------------------------------------------------------

| Docker Topic                          |     Go      |
| ------------------------------------- |:-----------:|
| Setup an interactive docker container | [Go](#q015) |
| Docker interactive vs tty flag  		| [Go](#q14)  |
| Connect to container Interactively	| [Go](#q13)  |
| Attach to running docker container	| [Go](#q12)  |
| Different Start Vs Run Command in Docker|[Go](#q11) |
| Dockerfile stages optimization		| [Go](#q10)  |
| Dockerfile Commands Go through		| [Go](#q09)  |
| Dockerfile Getting Started			| [Go](#q08)  |
| Docker Commands All Time Favourite	| [Go](#q07)  |
| Docker Getting Started Commands		| [Go](#q06)  |
| Docker Vs Hypervisor in Real life		| [Go](#q05)  |
| Docker Architecture for Developement	| [Go](#q04)  |
| Docker Setup in Cross Platfor			| [Go](#q03)  |
| Docker Vs Virtual Machines;			| [Go](#q02)  |
| What is Docker and Why Containers		| [Go](#q01)  |




-------------------------------------------------------------------------------------
-> Q015: Setup an interactive docker container;;

-> Suppose we've a dummy project called python-docker-app. 

python-docker-app/
	- apps.py
	- Dockerfile

-> app.py 

# app.py...

# Internal Content of app.py
def main():
	print("Hello, I'm docker-first-app")
	name = input("Your Name...")
	print(f"Hi {name}")
	print("Shutting down...")

if __name__ == "__main__":
	main()

# /app.py

-> Dockerfile

# Dockerfile ...

# stage 1: declaring base image;;
FROM python:3.9

# stage 2: pre-project requirements or dependencies setup;;

# stage 3: setup project;;
RUN mkdir -p /home/devil/first-app
WORKDIR /home/devil/first-app
COPY . ./

# stage 4: post-project requirements or dependencies setup;;

# stage 5: Expose it to parent host;;
EXPOSE 8000

# stage 6: setup entrypoint to that child container;;
ENTRYPOINT ["python3", "app.py"]

# /Dockerfile

-> Building Image

	$ docker build -t first_app:0.1 .

	verify image build ...
	$ docker images

-> Docker container up 
	
	# docker run -it <image_id>

	verify the result...

	$ Hello, I'm docker-first-app
	$ Your Name...Neeraj 
	$ Hi Neeraj
	$ Shutting down...


-------------------------------------------------------------------------------------
-> Q014: Docker interactive vs tty flag;;

-> Interactive (-i or --interactive): The -i or --interactive option in Docker
   allows you to keep STDIN open, even if not attached to a TTY.
   
   or, In other words, it enables you to interact with the container's shell
   or application. When you run a container with this option, you can send
   input to and receive output from the container, making it suitable for
   running interactive commands, scripts, or applications that require user
   interaction.

-> Allocating a TTY (teletypewriter) in a Docker container can be useful when
   you want to interact with the container's shell or, run an interactive
   application that expects a terminal. 
	
	or, You can allocate a TTY when running a Docker container using the -t
   or --tty option, and you can also use the -i or --interactive option for
   interactive sessions. Here's how you can allocate a TTY in Docker:


-------------------------------------------------------------------------------------
-> Q013: Connect to container Interactively;;

-> Sometimes you have the requirement to connect a container interactively,
   then you can use the command by like this

	$ docker exec -it <container_id> /bin/bash

	This command is composed of two flags 
		
		a) '-i' stands for interactive session.

		b) -t stands for tele type writer handle interaction with terminal


-------------------------------------------------------------------------------------
-> Q012: Attach to running docker container;;

Suppose you have a state where you want to attach the already running docker
container for real time logs monitoring and actions,

then you can do so by using this command 

$ docker attach <container_id>

or, you can also use logs with follow flag,
$ docker logs -f <container_id>


-------------------------------------------------------------------------------------
-> Q011: Different Start Vs Run Command in Docker;;

-> First Difference is that, 

	- Run command used image id to spin-off a container.

		$ docker run -p 8000:8000 <image_id>

	- Start command used container_id to re-run already existing container,
	
		$ docker start -p 8000:8000 <container_id>

-> Second difference is that, 
	
	- RUN command can spin-off any container with some extra flags, 
		like port (-p), interactive mode -(it)

		$ docker run -p 8000:8000 -it <image_id>

	- START command responsiblity will do the task of running the already
	  stopped or any pre-existing container. 

  		$ docker start <container_id>

-> Third different is that, 

	- RUN command run the container in the foreground mode 

		$ docker run <image_id>

		or, run the container in background mode.
		$ docker run -d <image_id>

	- START command run the container in the background mode by default. 

		$ docker start <container_id>

		or, run the container in foreground mode,
		$ docker start -a <container_id>

	Note: Run mode is not fixed can be changed as per the requirements as well. 
	It can be used interchangely using the flag `-d` for detached or background 
	and `-a` for attached or foreground mode.


NOTE: To run a container in interactive mode then use the `-it` flag.
$ docker exec -it <container_id> /bin/bash


-------------------------------------------------------------------------------------
-> Q010 : Dockerfile Commands Go through;;

-> Some Everytime Dockerfile use case commands ,
	
	-	FROM: Specifies the base image to use for building your image.

		$ FROM ubuntu:20 

		arg1 : base image name 
		arg2: base image tag name

	- RUN: Executes a command inside the image during the build process. It's
	  often used to install packages or run setup scripts.

	  	$ RUN apt-get install && apt-get install -y wkhtmltopdf

 	- COPY or ADD : Copies files or directories from your local machine into
	   the image.

	   $ COPY ./app /app

	   or, 
	   # ADD ./app /app

	- WORKDIR : Sets the working directory for subsequent commands.

		$ WORKDIR /app

	- EXPOSE : Informs Docker that the container will listen on a specified
	  port at runtime.

	  	$ EXPOSE 5000

	- CMD or ENTRYPOINT : Specifies the command to run when the container
	  starts. CMD is often used for providing default commands, while
	  ENTRYPOINT is used to define a container's main executable.

		$ CMD ["python", "app.py"]

		or, alternatively

		$ ENTRYPOINT ["python", "app.py"]

	- ENV : Sets environment variables inside the container.

		$ ENV DEBIAN_FRONTEND noninteractive

		here to set any library package installation non-interactive.

	- ARG : Defines build-time variables that can be passed to the Dockerfile
	  with the --build-arg flag

	  $ ARG MY_ARG=default_value

	- LABEL : Adds metadata to the image in key-value pairs

		$ LABEL maintainer="yourname@example.com"

	- USER : Specifies the user that the subsequent instructions will run as.

		$ USER appuser 

	- VOLUME : Creates a mount point for external volumes

		$ VOLUME /data


-------------------------------------------------------------------------------------
-> Q009: Dockerfile stages wise optimization;;



-------------------------------------------------------------------------------------
-> Q008: Dockerfile Getting Started;;

-> Suppose the project directory is like this ...

root/
	- apps 
		- core_apps 
		- migrations
		- settings
	- requirements.txt
	- Dockerfile

-> Basic Dockerfile looks something like this ...

# stage 1: declaring base image;;
FROM ubuntu:20.04

# stage 2: pre-project requirements or dependencies setup;;
# Requirement needs on the container image level,;;

# stage 3: project setup;;
RUN mkdir -p /home/devil/django-app

WORKDIR /home/devil/django-app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

# stage 4: post-project requirements or dependencies setup;;
# post project requirements, if any;;


# stage 5: Expose it to parent host;;
EXPOSE 8000

# stage 6: setup entrypoint to that child container;;
Entrypoint ["python3", "manage.py", "runserver"]

or, in windows use CMD
CMD ["python3", "manage.py", "runserver"]


-------------------------------------------------------------------------------------
-> Q007: Docker Commands All Time Favourite;;

#--- Run a docker container on a specific port;;
$ docker run -p 8000:8000 <container_id>

or, on a port with the image name
$ docker run -d -p 8080:8000 --name my-web-app nginx

here 8000:8000 means first port listening outside container and second port
listening inside the docker.

#--- To Run a container in detached mode or background mode;;
$ docker run -d <image_name>

or, 
$ docker run -d <container_id>

#--- View container logs;;
$ docker logs <container_id> 

or, to see continuous logs
$ docker logs -f <container_id>

#--- Execute a command inside the container;;
$ docker exec -it <container_id> sh 

or, alternatively 
$ docker exec -it <container_id> /bin/bash

#--- Stop the container;;
$ docker stop <container_id>

#--- To check all docker process;;
docker ps -a

#--- Docker Up;;
$docker-compose up 

or, in background
$ docker-compose up &
 
#--- docker remove un-used container or images;;
$ docker prune

or, for container only
$ docker containers prune

or, for images only
$ docker images prune

#--- docker command to first build then up the container;;
$ docker-compose up --build 

#--- build docker image with tag
$ docker build -t hello-world-app /path/to/dockerfile 

#--- check any docker command usage;;
$ docker images --help

or, general help
$ docker --help

#--- run the docker container from existing build image;;
$ docker start <container_id>

#--- remove pre-build images on the system;;
$ docker rmi <image_id>

or, forcefully use -f 
$ docker rmi -f <image_id> 

or, remove every image in one go 
$ docker rmi -f $(docker images -aq)

#--- remove container;;
$ docker rm <container_id>

#---- automatically remove container when it stops after run;;
$ docker run --rm <image_id>

here, it will remove the container as soon as it exited.

#--- inspect an docker image;;
$ docker image inspect <image_id>


-------------------------------------------------------------------------------------
-> Q006: Docker Getting Started Commands;;

-> 


-------------------------------------------------------------------------------------
-> Q005: Docker Vs Hypervisor in Real life;;

-> Docker and hypervisors are both technologies used for virtualization and isolation, but they serve different purposes and have distinct use cases in real-life scenarios. Here's a comparison of Docker and hypervisors in practical terms:

Resource Efficiency:

Docker: Docker containers are lightweight and share the host OS kernel, which makes them more resource-efficient compared to traditional virtualization. Containers can be started and stopped quickly, consuming fewer system resources.

Hypervisor: Hypervisors, such as VMware or VirtualBox, create full virtual machines (VMs) that emulate an entire operating system. VMs are bulkier and demand more system resources because they run a separate OS kernel for each VM.

Real-life scenario: In a cloud environment where you want to maximize resource utilization, Docker containers are preferred for running microservices, as they allow you to pack more workloads onto a single host.

Isolation:

Docker: Containers share the host OS kernel but have isolated filesystems and processes. While this provides a good level of isolation for most applications, it may not be suitable for highly sensitive workloads.

Hypervisor: Hypervisors offer stronger isolation because each VM runs its own OS kernel. This makes VMs more secure but less efficient in terms of resource usage.

Real-life scenario: In situations where security and isolation are paramount, such as hosting multiple customer environments on a single physical server, hypervisors are often preferred.

Portability:

Docker: Docker containers are highly portable. You can build a container image on your development machine and run it on different environments without worrying about compatibility issues. This makes Docker an excellent choice for continuous integration/continuous deployment (CI/CD) pipelines.

Hypervisor: VMs are less portable because they encapsulate an entire OS, which can make moving VMs between different hypervisor platforms more challenging.

Real-life scenario: Docker is commonly used in DevOps workflows, enabling developers to build and test applications in consistent environments and deploy them seamlessly across various stages of the development pipeline.

Performance:

Docker: Docker containers have minimal overhead due to their lightweight nature. They generally offer better performance than VMs for applications that don't require strict isolation.

Hypervisor: VMs have additional overhead because they run a complete OS. While this overhead is acceptable for some use cases, it can impact performance-sensitive applications.

Real-life scenario: In scenarios where performance is critical, such as running high-throughput databases or real-time applications, Docker containers are often preferred.

Management and Orchestration:

Docker: Docker provides tools like Docker Compose and Kubernetes for container orchestration and management. These tools simplify the deployment, scaling, and management of containerized applications.

Hypervisor: Hypervisors typically rely on external tools for management and orchestration. They are not as tightly integrated with orchestration frameworks as Docker containers.

Real-life scenario: For large-scale, distributed applications, Docker's built-in orchestration tools or platforms like Kubernetes provide comprehensive solutions for managing containerized workloads.

In real-life scenarios, the choice between Docker and hypervisors depends on your specific requirements, resource constraints, and the nature of your applications. Docker containers excel in modern microservices architectures, while hypervisors are more suitable for traditional virtualization scenarios where strong isolation and compatibility with legacy systems are essential. Often, organizations use a combination of both technologies to meet various use cases within their IT infrastructure.


-------------------------------------------------------------------------------------
-> Q004: Docker Architecture for Developement;;

-> Docker's architecture is designed to provide a consistent and efficient
   environment for developing, testing, and deploying applications.

-> Here's an overview of Docker's architecture:
	
#--- DOCKER ENGINE:

At the core of Docker is the Docker Engine. It's responsible for container
management, including creating, running, and managing containers. 

The Docker Engine consists of three key components:

	- Docker Daemon: This is a background service that manages Docker
	  containers. It listens for Docker API requests and performs
	  container-related tasks.

	- Docker CLI (Command-Line Interface): Developers interact with the Docker
	  Engine using the Docker CLI. They issue commands to create, manage, and
	  control containers.

	- REST API: The Docker Engine exposes a REST API that allows programs and
	  tools to communicate with it programmatically. Developers can use this
	  API to automate Docker-related tasks.

#--- DOCKER IMAGE:

Docker containers are created from images. 

An image is a lightweight, standalone, executable package that contains
everything needed to run a piece of software, including the code, runtime,
libraries, and system tools. 

Images are typically built from a set of instructions defined in a
Dockerfile.

#--- DOCKER-FILE:

A Dockerfile is a text file that contains instructions for building a Docker
image. 

It specifies a base image, copies files into the image, sets environment
variables, and defines the commands to run when a container is started. 

Dockerfiles are the blueprints for creating Docker images and are essential
for reproducible and version-controlled container builds.

#--- DOCKER CONTAINER:

A container is an instance of an image that runs as an isolated process on the
host system. 

Containers share the host's OS kernel but have their own isolated file system
and runtime environment. 

Containers are portable and can be run consistently across different
environments, making them ideal for development and testing.

#--- DOCKER REGISTRY:

A Docker registry is a repository for Docker images. The Docker Hub is a
popular public registry where you can find a wide range of pre-built
images. 

Organizations often use private registries to store and distribute their
custom images securely. Docker images can be pulled from and pushed to
registries.

#--- DOCKER COMPOSE:

Docker Compose is a tool for defining and running multi-container
applications. 

It allows developers to define a multi-container setup in a docker-compose.yml
file, specifying the services, their configuration, and dependencies. 

Compose simplifies the process of managing complex applications with multiple
containers.


#--- SWARM AND KUBERNETES:

Docker Swarm and Kubernetes are container orchestration platforms that help
manage and scale containers in production environments. 

They provide features like load balancing, high availability, service
discovery, and automated scaling. While primarily used in production,
understanding these orchestration tools can be valuable for development teams
working on containerized applications.


-------------------------------------------------------------------------------------
-> Q003 : Docker Setup in Cross Platform 

-> for Mac Os and Windows if the docker requirements are not installed
   successively then you should install docker toolbox then you've to install
   docker desktop.

-> for Linux, Docker Engine are supported Natively that means we dont need any
   docker related toolbox. we can setup docker directly.

-> Refer Ubuntu Installation :

	step 1: you can install the docker package using the snap package library,
 	
 		$ snap install docker 

 	step 2: Till now docker has been installed, now the docker io needs to installed
 	to run the docker daemon in the linux terminal.

 		$ sudo apt-get install docker.io

 	step 3: verify everything using their version, like 

 		# Verify docker and docker engine version ...
 		$ docker --version

 		# verify docker daemon ...
 		$ sudo sytemctl status docker 	

 		# Verify the docker compose version 
 		$ docker-compose --version

 		Till now if everything works fine then try to build test image,

 		$ docker run hello-world

 		This will pull the image from the docker hub and show you the
 		acknowledgement for the docker setup completion.

 		$ docker run -it ubuntu /bin/bash

 		To kill the docker contanier fetch the container id using `docker ps`
 		the kil using `docker kill <container_id>`

 	step 4: Add the docker in sudo group to run all the command without sudo
 	privileges
 		
 		- If you want to avoid typing sudo whenever you run the docker command,
 		  add your username to the docker group

			$ sudo usermod -aG docker ${USER}

		- To apply the new group membership, log out of the server and back in,
		  or type the following

			$ su - ${USER}

		- Confirm the group changes by using the below command

			$ groups

		- If you need to add a user to the docker group that you’re not logged
		  in as, declare that username explicitly using

			$ sudo usermod -aG docker username


-------------------------------------------------------------------------------------
-> Q002	: Docker Vs Virtual Machines;;

###-------- VIRTUAL MACHINE

-> Virtual Machine are setup on the top of the host machine. Any number of VM
   can be setup but require the hardware as well.

-> Every VM require dedicated amount of hardware resource including RAM, CPU,
   HDD to perform the task or bootup the system well.

-> Every VM bloated on the top Host machine is bloated the actual host
   configuration. Every time when spinning off the new VM we have to do the
   same step again and again. 

-> Virtual Machine Block Diagram
	
-------------------------------------------------------------------------
|     App A1		| 		 App B1			 |		App C1				|
|-------------------|------------------------|--------------------------|
| Library, Tools	| Libraries, Tools, 	 | Own Libraries, Tools, 	|
|  Dependency 		|  Dependencies 		 | Dependencies				|
|-------------------|------------------------|--------------------------|
| Virtual OS (Linux)| Virutal OS (Windows 7) | Virutal OS (Centos)		|
|					|						 | 							|
|-----------------------------------------------------------------------|
| 							Host Operating System						|
-------------------------------------------------------------------------

NOTE: 

Creating a own replicas of virtual os takes a lot of space on your hard
drive and tends to slow.


###--- Virtual Machine : Pros

	- It also allows separated environments.
	- Environment specific configuration are possible as well.
	- Environment configuration can be shared and reproduced reliably.

###--- Virtual Machine : Cons 
	
	- Lots of Redundant duplication, wastage of resource - RAM, HDD, CPU etc.
	- Performance can be slow, boot time can be long 
	- Reproducing on another computer/Server is possible but may still be tricky.


###----------- DOCKER

-> Docker Block Diagram

-------------------------------
|    Containers A, B, C 	   |
|  (A,B,C are independent 	   |
|  container with their own    |
|  os image, tools, libraries  |
|  and other dependencies)	   |
|------------------------------|
|      Docker Engine           |
| (Setup by Docker itself)	   |
|------------------------------|
| 	OS Build-in/Emulated       |
|   Containers Support         |
|------------------------------|
| your operating system        |
-------------------------------


###------------ DOCKER VS VIRTUAL MACHINE

-> Docker Containers:
	- Low imapact on OS, Very fast, minimal disk space usages
	- Sharing, re-building and distribution of image is easy.
	- Encapsulation apps/environments instead of whole machines.

-> Virtual Machines:
	- Bigger impact on OS, slower higher disk space usage
	- Sharing, re-building and distribution can be challenge.
	- Encapsulate whole machine instead of just apps/environment.


-------------------------------------------------------------------------------------
######q01 

### What is Docker and Why Containers;;

-> Docker is a container technology or a tool for creating and managing containers.

-> Containers Basic

	- A Standardized unit for software. In a real world, it can be a package
	  or a bundled of code and its related dependencies to run that code. 

	- The same container always yields the exact same application and
	  execution behaviour. No matter where or by whom it might be executed.

	- Support for containers is built into modern operating system.

	- Docker simplifies the creation and management of such containers.

	- for eg, Python Django Project with Particular Python runtime Version.

-> Why Containers: 

	-> Because we want independent, standardised - application packages.
	
	-> Different Developement & Production Environments : We want to build and
	   test in exactly the same code and environment on development and
	   production. So that we can make sure that everything works as expected.

	-> Different Development Environments With Team/Company : Every team
	   member should have exactly the same environemtn when working on the
	   same project

	-> Clashing Tools/Versions Between Different Projects : When switching
	   between Projects or tools used in project A should not clash with
	   Project B.


-------------------------------------------------------------------------------------