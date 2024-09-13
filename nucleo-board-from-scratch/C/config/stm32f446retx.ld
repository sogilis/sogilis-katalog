ENTRY(Reset_Handler)

MEMORY
{
    RAM(xrw): ORIGIN = 0x20000000, LENGTH = 128K
    ROM(rw) : ORIGIN = 0x08000000, LENGTH = 512K
}

_estack = ORIGIN(RAM) + LENGTH(RAM);

HEAP_SIZE = 0x200;
STACK_SIZE = 0x400;

/* Section Definitions */
SECTIONS
{
     /* Startup code with vector table */
    .isr_vector :
    {
        . = ALIGN(4);
        KEEP(*(.isr_vector))
        . = ALIGN(4);
    } > ROM

    /* The program code and other data */
    .text :
    {
        . = ALIGN(4);
        *(.text*)
        . = ALIGN(4);
        _etext = .;
    } > ROM

    /* .rodata section to store constant data */
    .rodata :
    {
        . = ALIGN(4);
        *(.rodata*)
        . = ALIGN(4);
    } > ROM

    /* .bss section which is used for uninitialized data */
    .bss (NOLOAD) :
    {
        . = ALIGN(4);
        _sbss = .;
        *(.bss*)
        *(COMMON)
        . = ALIGN(4);
        _ebss = .;
    } > RAM

    _la_data = LOADADDR(.data);

    .data :
    {
        . = ALIGN(4);
        _sdata = .;
        *(.data*)
        . = ALIGN(4);
        _edata = .;
    } > RAM AT > ROM

    /* stack section */
    .stack (NOLOAD):
    {
        . = ALIGN(8);
        PROVIDE(end = .);
        PROVIDE(_end = .);
        . = . + STACK_SIZE;
        . = . + HEAP_SIZE;
        . = ALIGN(8);
    } > RAM
}
