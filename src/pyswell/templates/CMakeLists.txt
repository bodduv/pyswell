cmake_minimum_required(VERSION ${cmake_minimum_required})

project(${project_name}
  VERSION ${version}
  CXX
)

add_executable(${target_name}
  source/main.cc
)

add_library(${target_name}
)

target_compile_features(${target_name} INTERFACE cxx_std_17)

#[[

# TODO Advanced Options
include(cmake/standard_project_settings.cmake)
include(cmake/compiler_warnings.cmake)
include(cmake/doxygen.cmake)
include(cmake/sanitizers.cmake)
include(cmake/static_analyzers.cmake)
include(cmake/conan.cmake)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

enable_sanitizers()
enable_doxygen()
enable_conan()

]]
