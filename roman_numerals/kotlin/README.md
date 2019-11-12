
# How to start with Docker?

1- Start a docker image with `JDK8`:

```bash
docker run -it -v $(pwd)/..:/home openjdk:8-jdk
```

2- Install prerequisites:

```bash
apt update && apt install make
```

3- Run tests with `make`

```bash
cd /home/kotlin
make
```

4- Hack `App.kt` in `src/main/kotlin`

# How to start with Java Development Kit >= 8 (see [AdoptOpenJDK](https://adoptopenjdk.net) for example)

1- Run tests with `make`

2- Hack `App.kt` in `src/main/kotlin`
