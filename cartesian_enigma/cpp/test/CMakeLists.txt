file(GLOB SRCS *.cpp)

ADD_EXECUTABLE(test_cartesian_enigma ${SRCS})

TARGET_LINK_LIBRARIES(test_cartesian_enigma
    libcartesian_enigma
    gtest
)

add_test(NAME test_cartesian_enigma
         COMMAND test_cartesian_enigma)
