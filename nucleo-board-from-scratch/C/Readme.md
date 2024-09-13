# README
## Prerequisites
Docker should be installed on the computer.
All the tools need for the project are included on the docker image.
To build the docker image, following the line :
```bash
$ docker build -t nucleo-board-from-scratch .
```
After building the image, launch a container :
```bash
$ docker run -it --rm -v $(pwd):/home/user/workspace nucleo-board-from-scratch
```
## Build the firmware
All the following commands are to enter on the container :
1. Create a specific workspace with wanted build type (debug or release mode) :
```bash
$ cmake -B build/<debug or release> -DCMAKE_BUILD_TYPE=<debug or release>
```
2. Build the firmware on the wanted workspace :
```bash
$ cmake --build build/<debug or release>
```
If you want to clean the workspace :
```bash
$ rm -rf build/<debug or release>
```
## Run the firmware
After building the firmware, you can flash it on the target connected by ST-Link:
```bash
$ openocd -f config/stm32f446retx.cfg -c "setup" -c "program_release <firmware file>"
```
Or if you don't have a board, you can run it on a emulator:
```bash
$ renode config/nucleo-f446re.resc
```
Note: Firmware path and name is on the config file *config/nucleo-f446re.resc*.
## Build and run test suite
1. Create workspace with build type as test :
```bash
$ cmake -B build/test -DCMAKE_BUILD_TYPE=test
```
2. Build all test binaries :
```bash
$ cmake --build build/test
```
3. Run a test suite :
```bash
$ build/test/bin/<test_suite_name>
```