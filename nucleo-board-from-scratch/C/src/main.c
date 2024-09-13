#include <stdint.h>

#define RAM_START 0x20000000u
#define RAM_SIZE (128u * 1024u) // 128K
#define RAM_END (RAM_START + RAM_SIZE)
#define STACK_START RAM_END

extern uint32_t _estack;
extern uint32_t _etext;
extern uint32_t _sdata;
extern uint32_t _edata;
extern uint32_t _la_data;
extern uint32_t _sbss;
extern uint32_t _ebss;

uint32_t volatile systick_counter = 0;

int main(void);
void Reset_Handler(void);
void NMI_Handler(void);
void HardFault_Handler(void);
void MemManage_Handler(void);
void BusFault_Handler(void);
void UsageFault_Handler(void);
void SVC_Handler(void);
void DebugMon_Handler(void);
void PendSV_Handler(void);
void SysTick_Handler(void);

uint32_t vectors[] __attribute__((section(".isr_vector"))) = {
    (uint32_t)STACK_START,
    (uint32_t) &Reset_Handler,
    (uint32_t) &NMI_Handler,
    (uint32_t) &HardFault_Handler,
    (uint32_t) &MemManage_Handler,
    (uint32_t) &BusFault_Handler,
    (uint32_t) &UsageFault_Handler,
    (uint32_t) 0, // reserved
	(uint32_t) 0, // reserved
	(uint32_t) 0, // reserved
	(uint32_t) 0, // reserved
	(uint32_t) &SVC_Handler,
	(uint32_t) &DebugMon_Handler,
	(uint32_t) 0, // reserved
	(uint32_t) &PendSV_Handler,
	(uint32_t) &SysTick_Handler,
};

void Reset_Handler(void) {
	// Copy .data section to RAM
	uint8_t *ramData = (uint8_t *)&_sdata;
	uint8_t *romData = (uint8_t *)&_la_data;
	uint32_t dataSize = (uint32_t)&_edata - (uint32_t)&_sdata;
	for (uint32_t index = 0; index < dataSize; index++) {
		*ramData++ = *romData++;
	}

	// Init the .bss section to 0
	uint32_t bssSize = (uint32_t)&_ebss - (uint32_t)&_sbss;
	uint8_t *bssData = (uint8_t *)&_sbss;
	for (uint32_t index = 0; index < bssSize; index++) {
		*bssData++ = 0;
	}

	// Now invoke main
	(void)main();
}

int main(void) {
	/* After reset, the CPU clock frequency is 16MHz */

	while(1) {
		// empty
	}

	return 0;
}

void NMI_Handler(void) {
	while(1);
}

void HardFault_Handler(void) {
	while(1);
}

void MemManage_Handler(void) {
	while(1);
}

void BusFault_Handler(void) {
	while(1);
}

void UsageFault_Handler(void) {
	while(1);
}

void SVC_Handler(void) {
	while(1);
}

void DebugMon_Handler(void) {
	while(1);
}

void PendSV_Handler(void) {
	while(1);
}

void SysTick_Handler(void) {
	systick_counter++;
}
