# Stub for C++ with GoogleTest

## Prerequisite

You first need to retrieve the GoogleTest UnitTest framework sources. You can run the folowing:

```make get_gtest```

## Building

You can build the main decoder executable as well as the unit_tests executable with:

```make build```

## Running

You can run the decoder executable with:

```make run```

You can run the unit_tests executable with:

```make test```

## Makefile hack

The Makefile at the root of the project is intended to ease the boilerplate operations. CMake is used in the background to build all of these C++ mysteries. A few hacks allow to run ```make test``` and having Make to recompile only if one of the source files has changed. Cool. But if one change is detected in either the sources or the tests, everything is rebuilt. Uncool. If you trained so much that you need such a feature, you should probably use directly CMake behind the scene and not the friendly Makefile.
