# Docker examples
### Dockerfile to deploy a python app using an alpine image with python3 builtin.

Docker container that runs a `print` in python3.

- Build image:
    ```
    docker build . -t alpine_python3:latest
    ```
- Run container :
    ```
    docker run --rm -it alpine_python3:latest
    ```

