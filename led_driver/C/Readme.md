# README

## Prerequisites
```bash
$ sudo apt install build-essential cmake gcc 
```

## Build and run test suite
```bash
$ cmake -B build
$ cmake --build build
$ ctest -V --test-dir build
```