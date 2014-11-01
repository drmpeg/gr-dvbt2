INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DVBT2 dvbt2)

FIND_PATH(
    DVBT2_INCLUDE_DIRS
    NAMES dvbt2/api.h
    HINTS $ENV{DVBT2_DIR}/include
        ${PC_DVBT2_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DVBT2_LIBRARIES
    NAMES gnuradio-dvbt2
    HINTS $ENV{DVBT2_DIR}/lib
        ${PC_DVBT2_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DVBT2 DEFAULT_MSG DVBT2_LIBRARIES DVBT2_INCLUDE_DIRS)
MARK_AS_ADVANCED(DVBT2_LIBRARIES DVBT2_INCLUDE_DIRS)

