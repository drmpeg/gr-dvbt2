# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
list(APPEND dvbt2_sources
    bbheader_bb_impl.cc
    bbscrambler_bb_impl.cc
    bch_bb_impl.cc
    ldpc_bb_impl.cc
    interleaver_bb_impl.cc
    modulator_bc_impl.cc
    cellinterleaver_cc_impl.cc
    framemapper_cc_impl.cc
    freqinterleaver_cc_impl.cc )

set(dvbt2_sources "${dvbt2_sources}" PARENT_SCOPE)
if(NOT dvbt2_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT dvbt2_sources)

add_library(gnuradio-dvbt2 SHARED ${dvbt2_sources})
target_link_libraries(gnuradio-dvbt2 ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-dvbt2 PROPERTIES DEFINE_SYMBOL "gnuradio_dvbt2_EXPORTS")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

if(APPLE)
    set_target_properties(gnuradio-dvbt2 PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-dvbt2
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})
list(APPEND test_dvbt2_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_dvbt2.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_dvbt2.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/)

add_executable(test-dvbt2 ${test_dvbt2_sources})

target_link_libraries(
  test-dvbt2
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-dvbt2
)

GR_ADD_TEST(test_dvbt2 test-dvbt2)
