
# How to start with Docker?

1- Start a docker image with `JDK8`:

```bash
docker run -it -v $(pwd)/..:/home openjdk:8-jdk
```

2- Run tests

```bash
cd /home/java
./gradlew test
```

3- Hack `App.java` in `src/main/java`

# How to start with Java Development Kit >= 8 (see [AdoptOpenJDK](https://adoptopenjdk.net) for example)

1- Run tests with `./gradlew test`

2- Hack `App.java` in `src/main/java`

# How to generate Eclipse configuration files?

```bash
./gradlew eclipse
```

# Known bug

On `Windows` OS, `SystemExtension.getOutput()` does not return trailing carriage return.
