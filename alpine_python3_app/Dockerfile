FROM frolvlad/alpine-python3
WORKDIR /code
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers bash
CMD ["python3","app.py"]
