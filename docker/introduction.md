### Development 

Instead of installing Postgres, MongoDB, dependencies, configs, scripts, and dealing with "works on my machine" issues, you can just do `"docker compose up"`
This starts the app and its needed services from a config file. 

### Deployment 

Instead of manually preparing a server, installing dependencies, copying files, and configuring everything, you package the app into a <b>container image</b>. Then deployment becomes more like `"Run this container image with these options"`. 

Big idea: <b>Containers package the applications + dependencies + runtime environment</b>, so the app runs more consistently across different machines. 
<hr>

### What is a Container Image? 

A docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application.

For example, if writing a python program, it would have the python runtime (software stack responsible for installing your application and dependencies) and the python version (specific release of the language). It may have Python libraries used such as SQLAlchemy to talk to a database or FastAPI to build out an API. Also, it will have the application code and all of these components get bundled into a container image. 

### What is a Container? 

A docker container is the actual running app created from the image. Note, One image can create many containers. For example, I send a container image to my friend. When my friend runs it `docker run your-image`, Docker creates a <b>Container</b> from that image. 
<hr>

### Open Container Initiative (OCI)

There were many companies building out containers, and many realized that it would make much more sense to create one standard that can be used across different implementations. All the companies came together and created the OCI which specifies industry standards around container formats and runtimes. There are three primary specifications of the OCI: 


- <b>Image Specification</b>: Specifies what should be included in the image in terms of metadata and the format it should contain so a serializable file system. 
- <b>Runtime Specification</b>: Defines how you would take an image that adheres to the image specification and run it in a container. 
- <b>Distribution Specification</b>: Talks about how images should be distributed so it is about registries, pushing and pulling images.  
<hr>


