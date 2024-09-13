set(BUILD_TARGET firmware)

add_executable(${BUILD_TARGET})

target_sources(${BUILD_TARGET} PRIVATE
    main.c
)

target_compile_options(${BUILD_TARGET} PRIVATE
    -Wall
    -Wextra
    -Werror
)

target_link_options(${BUILD_TARGET} PRIVATE
    -T${LINKER_FILE}
    --specs=nosys.specs
    --specs=nano.specs
    -Wl,-Map=output.map,--cref
    -Wl,--print-memory-usage
)
