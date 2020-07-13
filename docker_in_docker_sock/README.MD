# Docker examples
### Dockerfile to deploy a python app using an alpine image with python3 builtin.

In this case, mounting the docker sock to execute docker commands on the host from a python app.
The python app returns a "docker images" output. 

- Build image:
    ```
    docker build . -t alpine_sock101
    ```
- Run container :
    ```
    docker run -v "/var/run/docker.sock:/var/run/docker.sock" -it alpine_sock101
    ```

