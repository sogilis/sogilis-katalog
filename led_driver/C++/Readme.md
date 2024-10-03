# README

## Prerequisites
```bash
$ sudo apt install cmake g++ ninja-build
```

## Build and run test suite
```bash
$ cmake -B build
$ cmake --build build
$ ctest -V --test-dir build
```