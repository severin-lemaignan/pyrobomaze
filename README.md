A* implementation for the robomaze game
=======================================

Prerequisites
-------------

You need to install `cpprest` to easily perform REST request from C++.

On Ubuntu/Debian:

```
sudo apt install libcpprest-dev
```

Installation
------------

```
mkdir build
cd build

# due to an issue with libcpprest packaging, we need to help CMake a little
# see https://github.com/Microsoft/cpprestsdk/issues/686#issuecomment-440622042
cmake . -DCMAKE_PREFIX_PATH=/usr/lib/x86_64-linux-gnu/cmake
make install
```

Usage
-----

```
./astar <name of your robot>
```

