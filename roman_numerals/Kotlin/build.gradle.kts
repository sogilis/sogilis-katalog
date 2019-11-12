plugins {
    kotlin("jvm") version "1.3.50"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib-jdk8"))
    testImplementation(kotlin("test"))
    testImplementation(kotlin("test-junit"))
}

application {
    mainClassName = "com.sogilis.katalog.romanNumerals.AppKt"
}
