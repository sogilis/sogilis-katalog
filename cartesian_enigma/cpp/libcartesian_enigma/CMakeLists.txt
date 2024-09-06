set(libcartesian_enigma_decoder_SRCS
    decoder.h
    decoder.cpp
)

# Declare the library
add_library(libcartesian_enigma STATIC
    ${libcartesian_enigma_decoder_SRCS}
)

# Specify here the include directories exported
# by this library
target_include_directories(libcartesian_enigma PUBLIC
	${CMAKE_CURRENT_SOURCE_DIR}
)
