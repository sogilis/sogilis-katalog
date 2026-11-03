plugins {
    kotlin("jvm") version "2.4.20"
    application
}

group = "kata"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
    testImplementation(platform("org.junit:junit-bom:5.10.1"))
    testImplementation("org.junit.jupiter:junit-jupiter-params")
}

kotlin {
    jvmToolchain(25)
}

application {
    mainClass = "MainKt"
}

tasks.test {
    useJUnitPlatform()
    testLogging {
        events("passed", "failed", "skipped")
    }
}
