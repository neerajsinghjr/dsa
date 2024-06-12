```
-------------------------------------------------------------------------------------
- Topic	: Docker				
- Author : @neeraj-singh-jr	
- Status : Ongoing			
- Created : 29/09/2023		    
- Updated : 03/06/2024
-------------------------------------------------------------------------------------
- Q*** : Dockerfile stages wise optimization;;
- Q*** : Difference in CMD vs ENTRYPOINT Command;;
- Q*** : Docker Utility Based ENV Containers;;
- Q*** : Define Customer Container Name in Docker Compose;;
- Q*** : Docker-Compose Helpful Commands;;	
- Q*** : Docker-Compose File Commands;;
- Q*** : Different docker compose extensions (yml vs yaml);;
- Q*** : Docker Compose Core Concept;;
- Q*** : Integrate Multiple Docker Container Network;;
- Q*** : Docket Network Commands;;
- Q*** : Connect Docker Container to Local Host Services;;
- Q*** : Docker Container Networking;;
- Q021 : Docker ARG and ENV Variable Concept;;
- Q020 : Docker Ignore (.dockerignore) File Concept;;
- Q019 : Docker Volume Commands;;
- Q018 : Difference - Anonymous Vs Named Vs Mount Bind Volume;;
- Q017 : Docker Mount Bind Volumne Concept;;
- Q016 : Docker Named Volume Concept;;
- Q015 : Docker Anonymous Volume Concept;;
- Q014 : Docker Volume Concepts in Container;;
- Q013: Setup an interactive docker container;;
- Q012 : Docker interactive vs tty flag;;
- Q011 : Connect to container Interactively;;
- Q010 : Attach to running docker container;;
- Q009 : Different Start Vs Run Command in Docker;;
- Q008 : Dockerfile Commands Go through;;
- Q007 : Dockerfile Getting Started;;
- Q006 : Docker Favourite Commands;;
- Q005 : Docker Vs Hypervisor in Real life;;
- Q004 : Docker Architecture for Developement;;
- Q003 : Docker Setup in Cross Platform;;		
- Q002 : Docker Vs Virtual Machines;;			
- Q001 : What is Docker and Why Containers;;
```
-------------------------------------------------------------------------------------

### DOCKER NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q*** : Dockerfile stages wise optimization;;

-------------------------------------------------------------------------------------
### Q*** : Difference in CMD vs ENTRYPOINT Command;;

-------------------------------------------------------------------------------------
### Q*** : Docker Utility Based ENV Containers;;

-------------------------------------------------------------------------------------
### Q*** : Define Customer Container Name in Docker Compose;;

-------------------------------------------------------------------------------------
### Q*** : Docker-Compose Helpful Commands;;	

-------------------------------------------------------------------------------------
### Q*** : Docker-Compose File Commands;;

-------------------------------------------------------------------------------------
### Q*** : Different docker compose extensions (yml vs yaml);;

-------------------------------------------------------------------------------------
### Q*** : Docker Compose Core Concept;;

-------------------------------------------------------------------------------------
### Q*** : Integrate Multiple Docker Container Network;;

-------------------------------------------------------------------------------------
### Q*** : Docket Network Commands;;

-------------------------------------------------------------------------------------
### Q*** : Connect Docker Container to Local Host Services;;

-------------------------------------------------------------------------------------
### Q022 : Docker Container Networking;;

-------------------------------------------------------------------------------------
### Q021 : Docker ARG and ENV Variable Concept;;

-  Docker mechanisms for passing configuration values into a container
	1) ARG (build-time variables)
	2) ENV (environment variables)

#### ARG : Argument Variable on Image Build-Time

- ARG allows you to define variables which can be used in the process of
  building the image.

- These variables are typically used to provide flexibility during the
  image building process, allowing you to customize the image based on
  build-time parameters.

- ARG variables are specified in a Dockerfile using the ARG instruction.

- You can set the values of ARG variables at build time using the `--build-arg` 
  flag when executing the docker build command.

- Common use cases include specifying the version of a software package,
  setting default values for environment variables, or allowing users to
  customize the image behavior during the build process.

- for eg,
````
# Dockerfile structure;;
FROM ubuntu:20.04

ARG my_port=80
ENV PORT=$my_port

# Image Build-up from terminal;;
$ docker build -t arg_test_app:0.1 --build-arg my_port=9090 .
````
  
#### ENV : Environment Variables On Run-Time

- ENV allows you to set environment variables within a Docker image that
  are available to processes running inside containers.

- These variables are typically used for configuring software running
  within the container and for providing runtime parameters.

- ENV variables are specified in a Dockerfile using the ENV instruction.

- You can set the values of ENV variables during the image build process,
  and they are accessible within the running container.

- Common use cases include specifying configuration settings for applications 
  within the container, such as database connection strings or API keys.

- for eg,
    ````
    # Dockerfile structure;;
    FROM Ubuntu:20.04
  
    ENV LOGS_URL='https://api.example.com/logs/monitoring'
    ENV DEBIAN_FRONTEND noninteractive
    CMD echo $LOGS_MONITORING $DEBIAN_FRONTEND

    # Image Build-up from terminal;;
    $ docker build -t env_test_app:0.1 .

    # Set ENV Run-Time Variable;;
    $ docker run -d --env LOGS_URL='https://api.example.com/new/endpoint' <image_id>

    # Short Form of ENV flag;;
    $ docker run -d -e LOGS_URL='https://api.example.com/new/endpoint' <image_id>

    or, alternatively you can put all ENV in one file;;
    $ docker run -d --env-file 'path/to/env/file' <image_id>
    ````


-------------------------------------------------------------------------------------
### Q020 : Docker Ignore (.dockerignore) File Concept;;

-  The `.dockerignore file` is used to specify which files and directories
   should be excluded when building docker image.

-  The `.dockerignore file` should be placed in the same directory as your
   Dockerfile.

for eg,
````
# .dockerignore file
node_modules
*.log
/temp 
````


-------------------------------------------------------------------------------------
### Q019 : Docker Volume Commands;;

Docker provides several commands to manage volumes, allowing you to create,
inspect, list, and remove volumes. 

Here are the key volume-related commands in Docker:

- Create a Volume: `$ docker volume create my_volume`

- List Volumes: `$ docker volume ls`

- Inspect a Volume: `$ docker inspect volume <volume_name>`

- Remove Volume: `$ docker volume rm <volume_name>`

- Prune Un-Used Volume: `$ docker volume prune`

- Mount Volume in Container: 

  `$ docker run -d -v my_volume::/path/to/container <image_id>`


-------------------------------------------------------------------------------------
### Q018 : Difference - Anonymous Vs Named Vs Mount Bind Volume;;

Docker offers two primary types of volumes for managing data persistence 
within containers: 
	
1) Anonymous volumes
2) Named volumes
3) Bind Volumes

#### Anonymous Volumes:

- Automatically Created: Created automatically using -v or --volume flag at runtime.

- Unique Identifiers: Unique UUID is always assigned to anonymous volume.

- Ephemeral Data: They are usually considered as temporary data.

- Docker-Managed: Create or delete automatically by Docker in its lifecycle.

- No Direct Access: Volume access by docker and user have no direct access.

- Short-Lived Data: Suited for storing short-lived data, such as cache
files, log files, or other temporary container-specific data.

#### Named Volumes:

- User-Defined Names: These are explicitly created by user given names.

- Persistent Data: Volume that needs to be stored even after container not
  running.

- Access from Host and Containers: Named volumes can be mounted in multiple
  containers and easy to share among different container. 

- Ease of Access: Named volumes are also accessible from the host system,
  allowing you to manage and back up the data directly from the host.

- Explicit Management: Named volume are automatically removed, manual
  interaction needed.

- Sharing Data: Named volumes are  used for sharing data between containers
  or host system, allowing for consistent data access and management
  across containers.

#### Bind Volumes:

- Creation: Created manually by a host system path and container path, -v
  or --volume flag.

- Naming: Bind volumes are defined by their host system paths, so they are
  not named in the same way as named volumes.

- Purpose: Used for sharing data between the host system and containers.
  Data is stored on the host machine and is accessible from both the host
  and containers.

- Lifecycle: Bind volumes are managed as regular files and directories on
  the host system. They persist beyond container removal.

- Access: Data is directly accessible from the host system, making it easy
  to manage, edit, and back up.

- Use Cases: Suitable for scenarios where data needs to be accessed and
  shared between the host and containers, making it ideal for development,
  configuration files, and shared data.

#### Anonymous and Named Volumes:

- Anonymous volumes are suitable when you need to store temporary,
  container-specific data that doesn't require external management. Docker
  handles their creation and deletion.

- Named volumes are preferred for handling persistent data that needs to be
  shared between containers, accessed from the host, and managed
  externally. They provide more control and flexibility for data
  management.

- Bind volumes are used to share data between the host system and
  containers, making them ideal for development or scenarios where data
  needs to be accessible and editable on the host.

- In practice, a combination of both anonymous, named, bind volumes is
  often used to address different requirements within a containerized
  environment


-------------------------------------------------------------------------------------
### Q017 : Docker Mount Bind Volume Concept;;

-  `Docker bind volumes`, also known as host volumes, are a type of volume used
   to manage data persistence within containers. 

-  They allow you to explicitly specify a path on the host system that should
   be mounted into the container. 

-  This provides a way to share and manage data between the host system and
   containers. 

Here are some key concepts and characteristics of Docker bind volumes:

`1) Path on Host and Container`:

Bind volumes allow you to specify a path on the host system and a path
within the container.

The data in the host directory is mounted into the container, making it
accessible from both the host and the container.

`2) Persistence`:

Data in bind volumes is persistent and survives the removal of containers.
This makes bind volumes suitable for managing persistent data that needs
to be accessed and shared between containers or the host system.

`3) User-Defined Paths`:

You explicitly define the source path on the host system and the
destination path within the container when using the -v or --volume flag.

`4) Direct Host Access`:

Bind volumes are easily accessible from the host system, allowing you to
manage and back up data directly from the host.

`5) Data Sharing`:

Bind volumes are often used to share data between the host and containers
or among multiple containers. For example, you can use a bind volume to
store configuration files that need to be edited on the host system and
accessed by the container.

`6) File Permissions`:

File permissions on the mounted volume are the same as those on the host
system. This means that changes made to the files within the container
can affect the file permissions on the host.

Here's how to create and use a bind volume when running a Docker container:

`$ docker run -d -v /host/path:/container/path my_image`

Here, `/host/path` is the path on the host system and `/container/path` 
is the path within the container where the data is mounted. 

The container can access and modify the data in the `/container/path`
directory, and changes are reflected on the host system in the 
`/host/path directory`.

`7) Mount Volume Key Uses`:

Bind volumes are commonly used for scenarios where data needs to be
accessed and shared between containers and the host system, 

or, when it's necessary to manage persistent data that can be directly
edited and controlled from the host.


-------------------------------------------------------------------------------------
### Q016 : Docker Named Volume Concept;;

- Docker named volumes are a type of volume used to manage data persistence
  within containers. 

- They are explicitly named and provide a convenient and flexible way to data
  that needs to survive the removal of containers. 

- These can be shared among multiple containers, or be easily accessible from
  both the host system and containers. 

Here are some key concepts and characteristics of named volumes in Docker:

`1) User-Defined Names`: 

Named volumes are explicitly created and given user-defined names. You can
create them using the docker volume create command or by specifying a
name with the -v or --volume flag.

`2) Persistent Data`: 

Named volumes are designed for storing persistent data. This data is meant
to survive the removal of containers, container restarts, or even the
removal of the volume's associated containers.

`3) User-Defined Names`: 

Named volumes are given user-defined names, making them easily identifiable
and more human-readable than anonymous volumes.

`4) Access from Host and Containers`: 

Named volumes can be mounted in multiple containers, which makes it easier
to share data between containers. Named volumes are also accessible from
the host system, allowing you to manage and back up the data directly
from the host.

`5) Explicit Management`: 

Named volumes are not automatically deleted when containers using them are
removed. This means that you have to explicitly remove the volume when
it is no longer needed, using the docker volume rm command.

`6) Sharing Data`: 

Named volumes are often used for sharing data between containers. For
example, you can create a named volume to store a database's data and
then use that volume in multiple containers to ensure consistent data
access across containers.

Here's how to create a named volume using the docker volume create command:

`$ docker volume create my_named_volume`

or, alternatively, you can also create volume when running a container using
the flag -v or --volume,

`$ docker run -d -v my_named_volume:/container_path my_image`

In this example, `my_named_volume` is the name of the `named volume`.

`7) Named Volume Key Uses`:

`Named volumes` are a powerful and flexible way to handle persistent data in
Docker. They are commonly used for databases, configuration files,
application code, and any data that needs to survive container restarts
and be shared between containers.


-------------------------------------------------------------------------------------
### Q015 : Docker Anonymous Volume Concept;;

-  Docker anonymous volumes are a type of volume used to manage data persistence 
   within containers.

-  They are created and managed by Docker itself, and unlike named volumes,
   they are not explicitly named. Instead, they are assigned unique
   identifiers (UUIDs) and are typically used for temporary or ephemeral data
   specific to a container. 

Here are some key concepts and characteristics of anonymous volumes in Docker:

`1) Automatically Created`: 

Anonymous volumes are automatically created by Docker when you specify
the `-v` or `--volume` flag without explicitly specifying a source location.
	
For eg,
> $ docker run -v /project/temp <image_id>

An anonymous volume is created at the path `/project/temp` inside the container.

`2) Unique Identifiers`:

Each anonymous volume is assigned a unique identifier, such as a UUID, and
does not have a user-defined name. This identifier is not easily
human-readable.

`3) Ephemeral Data`:
Anonymous volumes are typically used for managing data that is temporary
and specific to a container's runtime. This data is expected to be
short-lived and may not need to be accessed or managed externally.

`4) Docker-Managed:` 

Docker is responsible for managing the lifecycle of anonymous volumes. This
includes their creation and deletion. When you remove a container that
uses anonymous volumes, Docker will also remove those associated volumes.

`5) No Direct Access`: 

Anonymous volumes are not meant to be directly accessible from the host
system. They are managed by Docker and may be challenging to access or
manage externally.

`6) Temporary Data Preferences`: 

Use anonymous volumes when you need to store temporary data, such as cached
files or runtime-specific data, within a container. Since Docker
automatically handles their creation and removal, you don't need to
worry about managing them.

`7) Not Easily Shared`: 

Anonymous volumes are typically associated with a single container and are
not designed for sharing data across multiple containers or with the
host system.


-------------------------------------------------------------------------------------
### Q014 : Docker Volume Concepts in Container;;

-  Volumes are folder on your host machine or hard drive which are mounted
("made available or mapped") into the containers.

-  Shared directory of docker-container volume mounted to the local-machine.

- For eg,

`/home/local-machine/shared  <- /home/docker-container/shared`

-  Volumes persist if a container shuts down. If a container (re-)starts and
mounts a volume, any data inside of that volume is available in the container.

-  A container can read or write data into a volume and similary it is
available for the local machine as well for read/write operation.

-  Volume Types are of two types :
	- Anonymous or Names Volume (Managed By Docker)
	- Bind Volume (Managed By Engineer)


-------------------------------------------------------------------------------------
### Q013: Setup an interactive docker container;;

-  Suppose we've a dummy project called python-docker-app. 

````
python-docker-app/
	- apps.py
	- Dockerfile

-  app.py 
````

````
# inside app.py...

# Internal Content of app.py
def main():
	print("Hello, I'm docker-first-app")
	name = input("Your Name...")
	print(f"Hi {name}")
	print("Shutting down...")

if __name__ == "__main__":
	main()

# /app.py
````

````
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
````

````
#  Building Image
$ docker build -t first_app:0.1 .

# Verify image build ...
$ docker images

# Docker container up 
$ docker run -it <image_id>

# verify the result...
$ Hello, I'm docker-first-app
$ Your Name...Neeraj 
$ Hi Neeraj
$ Shutting down...
````


-------------------------------------------------------------------------------------
### Q012: Docker interactive vs tty flag;;

-  `Interactive (-i or --interactive)`: The -i or --interactive option in Docker
   allows you to keep STDIN open, even if not attached to a TTY.
   
   or, In other words, it enables you to interact with the container's shell
   or application. When you run a container with this option, you can send
   input to and receive output from the container, making it suitable for
   running interactive commands, scripts, or applications that require user
   interaction.

-  `Allocating a TTY (teletypewriter)` in a Docker container can be useful when
   you want to interact with the container's shell or, run an interactive
   application that expects a terminal. 
	
   You can allocate a TTY when running a Docker container using the -t
   or --tty option, and you can also use the -i or --interactive option for
   interactive sessions. Here's how you can allocate a TTY in Docker:

    `$ docker exec -it <container_id> /bin/bash`

-------------------------------------------------------------------------------------
### Q011: Connect to container Interactively;;

Sometimes you have the requirement to connect a container interactively,
then you can use the command by like this

`$ docker exec -it <container_id> /bin/bash`

This command is composed of two flags

a) `-i` stands for interactive session.

b) `-t` stands for tele-type writer handle interaction with terminal


-------------------------------------------------------------------------------------
### Q010: Attach to running docker container;;

Suppose you have a state where you want to attach the already running docker
container for real time logs monitoring and actions,

then you can do so by using this command 

`$ docker attach <container_id>`

or, you can also use logs with follow flag,

`$ docker logs -f <container_id>`


-------------------------------------------------------------------------------------
### Q009: Difference Start Vs Run Command in Docker;;

- First Difference is that, 

	- Run command used image id to spin off a container.

		`$ docker run -p 8000:8000 <image_id>`

	- Start command used container_id to re-run already existing container,
	
		`$ docker start -p 8000:8000 <container_id>`

- Second difference is that, 
	
	- `RUN` command can spin off any container with some extra flags, 
		like `port (-p)`, `interactive mode -(it)`

		`$ docker run -p 8000:8000 -it <image_id>`

	- `START` command responsiblity will do the task of running the already
	  stopped or any pre-existing container. 

  		`$ docker start <container_id>`

- Third difference is that, 

    - `RUN` command run the container in the foreground mode 

        `$ docker run <image_id>`

        or, run the container in background mode.

        `$ docker run -d <image_id>`

    - `START` command run the container in the background mode by default. 

        `$ docker start <container_id>`

        or, run the container in foreground mode,
   
        `$ docker start -a <container_id>`

NOTE: Run mode is not fixed can be changed as per the requirements as well. 
It can be used interchangely using the flag `-d` for detached or background 
and `-a` for attached or foreground mode.

NOTE: To run a container in interactive mode then use the `-it` flag.

`$ docker exec -it <container_id> /bin/bash`


-------------------------------------------------------------------------------------
### Q008 : Dockerfile Commands Go through;;

Dockerfile use case commands,
	
- `FROM`: Specifies the base image to use for building your image.

	`$ from ubuntu:20` 

	- arg1: base image name
	- arg2: base image tag name

- `RUN`: Executes a command inside the image during the build process. 
It's often used to install packages or run setup scripts.

	`$ RUN apt-get install && apt-get install -y wkhtmltopdf`

- `COPY or ADD` : Copies files or directories from your local machine into
the image.

	`$ COPY ./app /app`

  or, 
	`# ADD ./app /app`

- `WORKDIR` : Sets the working directory for subsequent commands.

	`$ WORKDIR /app`

- `EXPOSE` : Informs Docker that the container will listen on a specified
port at runtime.

 	`$ EXPOSE 5000`

- `CMD or ENTRYPOINT` : Specifies the command to run when the container
 starts. CMD is often used for providing default commands, while
 ENTRYPOINT is used to define a container's main executable.

	`$ CMD ["python", "app.py"]`

	or, alternatively
	`$ ENTRYPOINT ["python", "app.py"]`

- `ENV` : Sets environment variables inside the container.

    `$ ENV DEBIAN_FRONTEND noninteractive`

   here to set any library package installation non-interactive.

- `ARG` : Defines build-time variables that can be passed to the Dockerfile
with the `--build-arg flag`

	`$ ARG MY_ARG=default_value`

- `LABEL` : Adds metadata to the image in key-value pairs

	`$ LABEL maintainer="yourname@example.com"`

- `USER` : Specifies the user that the subsequent instructions will run as.

	`$ USER appuser` 

- `VOLUME` : Creates a mount point for external volumes

	`$ VOLUME /data`


-------------------------------------------------------------------------------------
### Q007: Dockerfile Getting Started;;

-  Suppose the project directory is like this ...

````
# project-directory;;
root/
    - apps/
        - core_apps 
        - migrations
        - settings
    - requirements.txt
    - Dockerfile
````

-  Basic Dockerfile looks something like this ...

````
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
````


-------------------------------------------------------------------------------------
### Q006 : Docker Favourite Commands;;

#### Run a docker container on a specific port;;
> $ docker run -p 8000:8000 <container_id>

or, on a port with the image name
> $ docker run -d -p 8080:8000 --name my-web-app nginx

here 8000:8000 means first port listening outside container and second port
listening inside the docker.

#### To Run a container in detached mode or background mode;;
> $ docker run -d <image_name>

or, 
> $ docker run -d <container_id>

#### View container logs;;
> $ docker logs <container_id> 

or, to see continuous logs tail
> $ docker logs -f <container_id>

#### Execute a command inside the container;;
> $ docker exec -it <container_id> sh 

or, alternatively 
> $ docker exec -it <container_id> /bin/bash

#### Stop the container;;
> $ docker stop <container_id>

#### To check all docker process;;
> $ docker ps -a

#### Docker Up;;
> $ docker-compose up 

or, in background
> $ docker-compose up &
 
#### Docker remove un-used container or images;;
> $ docker prune

or, for container only
> $ docker containers prune

or, for images only
> $ docker images prune

#### Docker command to first build then up the container;;
> $ docker-compose up --build 

#### Build docker image with tag
> $ docker build -t hello-world-app /path/to/dockerfile 

#### Check any docker command usage;;
> $ docker images --help

or, general help
> $ docker --help

#### Run the docker container from existing build image;;
> $ docker start <container_id>

#### Remove pre-build images on the system;;
> $ docker rmi <image_id>

or, forcefully use -f 
> $ docker rmi -f <image_id> 

or, remove every image in one go 
> $ docker rmi -f $(docker images -aq)

#### Remove container;;
> $ docker rm <container_id>

#### Automatically remove container when it stops after run;;
> $ docker run --rm <image_id>

here, it will remove the container as soon as it exited.

#### Inspect an docker image;;
> $ docker image inspect <image_id>


-------------------------------------------------------------------------------------
### Q005: Docker Vs Hypervisor in Real life;;

`Docker` and `hypervisors` are both technologies used for virtualization and 
isolation, but they serve different purposes and have distinct use cases in real-life 
scenarios. 

Here's a comparison of Docker and hypervisors in practical terms:

1. Resource Efficiency:

- `Docker`: Docker containers are lightweight and share the host OS kernel, which 
   makes them more resource-efficient compared to traditional virtualization. 
   Containers can be started and stopped quickly, consuming fewer system resources.

- `Hypervisor`: Hypervisors, such as VMware or VirtualBox, create full virtual 
   machines (VMs) that emulate an entire operating system. VMs are bulkier and 
   demand more system resources because they run a separate OS kernel for each VM.

- `Real-life scenario`: In a cloud environment where you want to maximize resource 
   utilization, Docker containers are preferred for running microservices, as they 
   allow you to pack more workloads onto a single host.

2. Isolation:

- `Docker`: Containers share the host OS kernel but have isolated filesystems and 
   processes. While this provides a good level of isolation for most applications, 
   it may not be suitable for highly sensitive workloads.

- `Hypervisor`: Hypervisors offer stronger isolation because each VM runs its own 
   OS kernel. This makes VMs more secure but less efficient in terms of resource usage.

- `Real-life scenario`: In situations where security and isolation are paramount, such 
   as hosting multiple customer environments on a single physical server, hypervisors 
   are often preferred.

3. Portability:

- `Docker`: Docker containers are highly portable. You can build a container image on 
   your development machine and run it on different environments without worrying about 
   compatibility issues. This makes Docker an excellent choice for continuous integration 
   and continuous deployment (CI/CD) pipelines.

- `Hypervisor`: VMs are less portable because they encapsulate an entire OS, which can 
   make moving VMs between different hypervisor platforms more challenging.

- `Real-life scenario`: Docker is commonly used in DevOps workflows, enabling developers 
   to build and test applications in consistent environments and deploy them seamlessly 
   across various stages of the development pipeline.

4. Performance:

- `Docker`: Docker containers have minimal overhead due to their lightweight nature. 
   They generally offer better performance than VMs for applications that don't require 
   strict isolation.

- `Hypervisor`: VMs have additional overhead because they run a complete OS. While this 
   overhead is acceptable for some use cases, it can impact performance-sensitive 
   applications.

- `Real-life scenario`: In scenarios where performance is critical, such as running 
   high-throughput databases or real-time applications, Docker containers are often 
   preferred.

5. Management and Orchestration:

- `Docker`: Docker provides tools like Docker Compose and Kubernetes for container 
   orchestration and management. These tools simplify the deployment, scaling, and 
   management of containerized applications.

- `Hypervisor`: Hypervisors typically rely on external tools for management and 
   orchestration. They are not as tightly integrated with orchestration frameworks as 
   Docker containers.

- `Real-life scenario`: For large-scale, distributed applications, Docker's built-in 
   orchestration tools or platforms like Kubernetes provide comprehensive solutions for 
   managing containerized workloads.

   In real-life scenarios, the choice between Docker and hypervisors depends on your 
   specific requirements, resource constraints, and the nature of your applications. 
   
   Docker containers excel in modern microservices architectures, while hypervisors
   are more suitable for traditional virtualization scenarios where strong isolation 
   and compatibility with legacy systems are essential. 
   
   Often, organizations use a combination of both technologies to meet various use 
   cases within their IT infrastructure.


-------------------------------------------------------------------------------------
### Q004: Docker Architecture for Developement;;

-  Docker's architecture is designed to provide a consistent and efficient
   environment for developing, testing, and deploying applications.

-  Here's an overview of Docker's architecture:
	
#### DOCKER ENGINE:

At the core of Docker is the Docker Engine. It's responsible for container
management, including creating, running, and managing containers. 

The Docker Engine consists of `three` key components:

- `Docker Daemon`: This is a background service that manages Docker
  containers. It listens for Docker API requests and performs
  container-related tasks.

- `Docker CLI (Command-Line Interface)`: Developers interact with the Docker
  Engine using the Docker CLI. They issue commands to create, manage, and
  control containers.

- `REST API`: The Docker Engine exposes a REST API that allows programs and
  tools to communicate with it programmatically. Developers can use this
  API to automate Docker-related tasks.

#### DOCKER IMAGE:

Docker containers are created from images. 

An image is a lightweight, standalone, executable package that contains
everything needed to run a piece of software, including the code, runtime,
libraries, and system tools. 

Images are typically built from a set of instructions defined in a
Dockerfile.

#### DOCKER-FILE:

A `Dockerfile is a text file` that contains instructions for building a `Docker
image`. 

It specifies a base image, copies files into the image, sets environment
variables, and defines the commands to run when a container is started. 

Dockerfiles are the blueprints for creating Docker images and are essential
for reproducible and version-controlled container builds.

#### DOCKER CONTAINER:

A container is an instance of an image that runs as an isolated process on the
host system. 

Containers share the host's OS kernel but have their own isolated file system
and runtime environment. 

Containers are portable and can be run consistently across different
environments, making them ideal for development and testing.

#### DOCKER REGISTRY:

A Docker registry is a repository for Docker images. The Docker Hub is a
popular public registry where you can find a wide range of pre-built
images. 

Organizations often use private registries to store and distribute their
custom images securely. Docker images can be pulled from and pushed to
registries.

#### DOCKER COMPOSE:

Docker Compose is a tool for defining and running multi-container
applications. 

It allows developers to define a multi-container setup in a docker-compose.yml
file, specifying the services, their configuration, and dependencies. 

Compose simplifies the process of managing complex applications with multiple
containers.

#### SWARM AND KUBERNETES:

Docker Swarm and Kubernetes are container orchestration platforms that help
manage and scale containers in production environments. 

They provide features like load balancing, high availability, service
discovery, and automated scaling. While primarily used in production,
understanding these orchestration tools can be valuable for development teams
working on containerized applications.


-------------------------------------------------------------------------------------
### Q003 : Docker Setup in Cross Platform;; 

-  for MacOs and Windows if the docker requirements are not installed successively 
   then you should install docker toolbox then you've to install docker desktop.

-  for Linux, Docker Engine are supported Natively that means we don't need any
   docker related toolbox. we can setup docker directly.

-  Refer Ubuntu Installation :

	step 1: you can install the docker package using the snap package library,
 	
 		$ snap install docker 

 	step 2: Till now docker has been installed, now the docker io needs to installed
 	to run the docker daemon in the linux terminal.

 		$ sudo apt-get install docker.io

 	step 3: verify everything using their version, like 

 		# Verify docker and docker engine version ...
 		$ docker --version

 		# verify docker daemon ...
 		$ sudo systemctl status docker 	

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
### Q002 : Docker Vs Virtual Machines;;

#### VIRTUAL MACHINE

-  Virtual Machine are setup on the top of the host machine. Any number of VM
   can be setup but require the hardware as well.

-  Every VM require dedicated amount of hardware resource including RAM, CPU,
   HDD to perform the task or bootup the system well.

-  Every VM bloated on the top Host machine is bloated the actual host
   configuration. Every time when spinning off the new VM we have to do the
   same step again and again. 

-  Virtual Machine Block Diagram

````
---------------------------------------------------------------
|       App A1     |         App B1    |      App C1           |
|------------------|-------------------|-----------------------|
| Library, Tools   | Libraries, Tools, | Own Libraries, Tools, |
|  Dependency      | Dependencies      | Dependencies          |
|------------------|-------------------|-----------------------|
| Virtual OS       | Virutal OS        |      Virutal OS       |
|  (Linux)         | (Windows 7)       |    (Centos)           |
|--------------------------------------------------------------|
|                     Host Operating System                    |
---------------------------------------------------------------
````

**(NOTE: Creating a own replicas of virtual os takes a lot of space on your 
hard drive and tends to slow.)**


#### Virtual Machine : Pros

	- It also allows separated environments.
	- Environment specific configuration are possible as well.
	- Environment configuration can be shared and reproduced reliably.

#### Virtual Machine : Cons 
	
	- Lots of Redundant duplication, wastage of resource - RAM, HDD, CPU etc.
	- Performance can be slow, boot time can be long 
	- Reproducing on another computer/Server is possible but may still be tricky.


### DOCKER BLOCK DIAGRAM

````
-------------------------------
|    Containers A, B, C        |
|  (A,B,C are independent      |
|  container with their own    |
|  os image, tools, libraries  |
|  and other dependencies)     |
|------------------------------|
|      Docker Engine           |
| (Setup by Docker itself)     |
|------------------------------|
|   OS Build-in/Emulated       |
|   Containers Support         |
|------------------------------|
|    your operating system     |
-------------------------------
````

#### DOCKER VS VIRTUAL MACHINE

- Docker Containers:
	- Low impact on OS, Very fast, minimal disk space usages.
	- Sharing, re-building and distribution of image is easy.
	- Encapsulation apps/environments instead of whole machines.

- Virtual Machines:
	- Bigger impact on OS, slower higher disk space usage.
	- Sharing, re-building and distribution can be challenge.
	- Encapsulate whole machine instead of just apps/environment.


-------------------------------------------------------------------------------------
### Q001 : What is Docker and Why Containers;;

#### What is Docker:

-  `Docker` is a container technology or a tool for creating and managing containers.

#### Containers Basic:

- A Standardized unit for software. In a real world, it can be a package
  or a bundled of code and its related dependencies to run that code. 

- The same container always yields the exact same application and
  execution behaviour. No matter where or by whom it might be executed.

- Support for containers is built into modern operating system.

- Docker simplifies the creation and management of such containers.

- for eg, Python Django Project with Particular Python runtime Version.

#### Why Containers:

-  Because we want independent, standardised - application packages.

-  Different Developement & Production Environments : We want to build and
   test in exactly the same code and environment on development and
   production. So that we can make sure that everything works as expected.

-  Different Development Environments With Team/Company : Every team
   member should have exactly the same environment when working on the
   same project

-  Clashing Tools/Versions Between Different Projects : When switching
   between Projects or tools used in project A should not clash with
   Project B.


-------------------------------------------------------------------------------------