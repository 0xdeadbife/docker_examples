FROM frolvlad/alpine-python3
WORKDIR /code
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers bash
RUN apk add --no-cache  --repository http://dl-cdn.alpinelinux.org/alpine/edge/main --repository  http://dl-cdn.alpinelinux.org/alpine/edge/community docker
CMD ["python3","app.py"]