configure_file("${CMAKE_CURRENT_SOURCE_DIR}/gitsha1.cpp.in" "${CMAKE_CURRENT_BINARY_DIR}/gitsha1.cpp" @ONLY)


add_library(
	integrands
	STATIC
    dipole_amplitudes.cpp
	integrands_T.cpp
	integrands_L.cpp
    b_integral.cpp
    evaluate_integral_T.cpp
    evaluate_integral_L.cpp
    constants.cpp
)


add_executable(
	NLO_amplitude
    ${CMAKE_CURRENT_BINARY_DIR}/gitsha1.cpp
	main.cpp
)


include_directories(.)

target_link_libraries(
	NLO_amplitude
	PRIVATE
	integrands
	amplitude
	GSL::gsl
	GSL::gslcblas
    pthread
)







# Add compatibility with Boost

# set(Boost_USE_STATIC_LIBS ON)
# set(Boost_USE_MULTITHREADED ON)
# set(Boost_USE_STATIC_RUNTIME OFF)
# find_package(Boost 1.55 REQUIRED COMPONENTS unit_test_framework)


# add_executable(tests tests.cpp)
# target_include_directories(tests PRIVATE ${Boost_INCLUDE_DIRS})


# target_link_libraries(
# 	tests
# 	PRIVATE
# 	integrands
# 	amplitude
# 	${Boost_LIBRARIES}
# 	GSL::gsl
# 	GSL::gslcblas
# )

# add_custom_command(TARGET tests POST_BUILD COMMAND tests)