cmake_minimum_required(VERSION 3.5)
project(mnist)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED 17)
set(CMAKE_OSX_ARCHITECTURES arm64)
set(CMAKE_CXX_COMPILER "/usr/bin/clang++")
set(CMAKE_PREFIX_PATH "/Users/lindong/Applications/libtorch")
set(CMAKE_VERBOSE_MAKEFILE "ON")

find_package(Torch REQUIRED)

add_executable(mnist mnist.cpp)
target_compile_features(mnist PUBLIC cxx_range_for)
target_link_libraries(mnist ${TORCH_LIBRARIES})

