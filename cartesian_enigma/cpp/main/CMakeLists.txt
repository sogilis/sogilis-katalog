set(Main_SRCS
    main.cpp
)

add_executable(myApp
    ${Main_SRCS}
)

# Specify here the libraries this program depends on
target_link_libraries(myApp
    libcartesian_enigma
)
