# xld-simple-itest

This project shows how to use Integration Server Gradle Plugin to run Deploy for testing purposes.
The configuration is the easiest to get the grasp what is the minimum configuration required to make this setup.

The configuration how to run Gradle task, can be found in `.github/workflows/build.yaml`.

If you are going to configure it on a bare VM, you have to be sure you have the next things installed:

* Java 11
* Docker
* Docker Compose 

The main piece of integration server configuration is specified in this block in `build.gradle` file. 
For more information you read this blog: 
[https://xebialabs.github.io/integration-server-gradle-plugin/blog/2021/09/01/run-integration-test](https://xebialabs.github.io/integration-server-gradle-plugin/blog/2021/09/01/run-integration-test)  
