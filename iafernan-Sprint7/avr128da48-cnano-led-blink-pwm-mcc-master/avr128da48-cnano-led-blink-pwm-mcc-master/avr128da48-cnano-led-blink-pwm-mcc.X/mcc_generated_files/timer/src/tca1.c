/**
  @Company
    Microchip Technology Inc.

  @Description
    This Source file provides APIs.
    Generation Information :
    Driver Version    :   2.0.0
*/
/*
Copyright (c) [2012-2020] Microchip Technology Inc.  

    All rights reserved.

    You are permitted to use the accompanying software and its derivatives 
    with Microchip products. See the Microchip license agreement accompanying 
    this software, if any, for additional info regarding your rights and 
    obligations.
    
    MICROCHIP SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT 
    WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT 
    LIMITATION, ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT 
    AND FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT WILL MICROCHIP OR ITS
    LICENSORS BE LIABLE OR OBLIGATED UNDER CONTRACT, NEGLIGENCE, STRICT 
    LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR OTHER LEGAL EQUITABLE 
    THEORY FOR ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES INCLUDING BUT NOT 
    LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES, 
    OR OTHER SIMILAR COSTS. 
    
    To the fullest extend allowed by law, Microchip and its licensors 
    liability will not exceed the amount of fees, if any, that you paid 
    directly to Microchip to use this software. 
    
    THIRD PARTY SOFTWARE:  Notwithstanding anything to the contrary, any 
    third party software accompanying this software is subject to the terms 
    and conditions of the third party's license agreement.  To the extent 
    required by third party licenses covering such third party software, 
    the terms of such license will apply in lieu of the terms provided in 
    this notice or applicable license.  To the extent the terms of such 
    third party licenses prohibit any of the restrictions described here, 
    such restrictions will not apply to such third party software.
*/


#include "../tca1.h"

const struct TMR_INTERFACE TCA1_Interface = {
    .Initialize = TCA1_Initialize,
    .Start = NULL,
    .Stop = NULL,
    .PeriodCountSet = TCA1_Write,
    .TimeoutCallbackRegister = TCA1_OverflowCallbackRegister,
    .Tasks = NULL
};

void TCA1_DefaultCompare0CallbackRegister(void);
void (*TCA1_CMP0_isr_cb)(void) = &TCA1_DefaultCompare0CallbackRegister;
void TCA1_DefaultCompare1CallbackRegister(void);
void (*TCA1_CMP1_isr_cb)(void) = &TCA1_DefaultCompare1CallbackRegister;
void TCA1_DefaultCompare2CallbackRegister(void);
void (*TCA1_CMP2_isr_cb)(void) = &TCA1_DefaultCompare2CallbackRegister;
void TCA1_DefaultOverflowCallbackRegister(void);
void (*TCA1_OVF_isr_cb)(void) = &TCA1_DefaultOverflowCallbackRegister;

void TCA1_DefaultCompare0CallbackRegister(void)
{
    //Add your ISR code here
}

void TCA1_DefaultCompare1CallbackRegister(void)
{
    //Add your ISR code here
}

void TCA1_DefaultCompare2CallbackRegister(void)
{
    //Add your ISR code here
}

void TCA1_DefaultOverflowCallbackRegister(void)
{
    //Add your ISR code here
}

void TCA1_OverflowCallbackRegister(TCA1_cb_t cb)
{
    TCA1_OVF_isr_cb = cb;
}

void TCA1_Compare0CallbackRegister(TCA1_cb_t cb)
{
    TCA1_CMP0_isr_cb = cb;
}

void TCA1_Compare1CallbackRegister(TCA1_cb_t cb)
{
    TCA1_CMP1_isr_cb = cb;
}

void TCA1_Compare2CallbackRegister(TCA1_cb_t cb)
{
    TCA1_CMP2_isr_cb = cb;
}

ISR(TCA1_CMP0_vect)
{
    if (TCA1_CMP0_isr_cb != NULL)
        (*TCA1_CMP0_isr_cb)();
    
    TCA1.SINGLE.INTFLAGS = TCA_SINGLE_CMP0_bm;
}

ISR(TCA1_CMP1_vect)
{
    if (TCA1_CMP1_isr_cb != NULL)
        (*TCA1_CMP1_isr_cb)();
    
    TCA1.SINGLE.INTFLAGS = TCA_SINGLE_CMP1_bm;
}

ISR(TCA1_CMP2_vect)
{
    if (TCA1_CMP2_isr_cb != NULL)
        (*TCA1_CMP2_isr_cb)();
    
    TCA1.SINGLE.INTFLAGS = TCA_SINGLE_CMP2_bm;
}

ISR(TCA1_OVF_vect)
{
    if (TCA1_OVF_isr_cb != NULL)
        (*TCA1_OVF_isr_cb)();
    
    TCA1.SINGLE.INTFLAGS = TCA_SINGLE_OVF_bm;
}


/**
 * \brief Initialize TCA interface
 */
void TCA1_Initialize(void) {
    // Compare 0
    TCA1.SINGLE.CMP0 = 0xFFDB;
        
    // Compare 1
    TCA1.SINGLE.CMP1 = 0xFFDB;
    
    // Compare 2
    TCA1.SINGLE.CMP2 = 0x7FED;
        
    // Count
    TCA1.SINGLE.CNT = 0x0;
    
    // ALUPD disabled; CMP0EN disabled; CMP1EN disabled; CMP2EN enabled; WGMODE SINGLESLOPE; 
    TCA1.SINGLE.CTRLB = 0x43;
    
    // CMP0OV disabled; CMP1OV disabled; CMP2OV disabled; 
    TCA1.SINGLE.CTRLC = 0x0;
    
    // SPLITM disabled; 
    TCA1.SINGLE.CTRLD = 0x0;
    
    // CMD NONE; DIR disabled; LUPD disabled; 
    TCA1.SINGLE.CTRLECLR = 0x0;
    
    // CMD NONE; DIR UP; LUPD disabled; 
    TCA1.SINGLE.CTRLESET = 0x0;
    
    // CMP0BV disabled; CMP1BV disabled; CMP2BV disabled; PERBV disabled; 
    TCA1.SINGLE.CTRLFCLR = 0x0;
    
    // CMP0BV disabled; CMP1BV disabled; CMP2BV disabled; PERBV disabled; 
    TCA1.SINGLE.CTRLFSET = 0x0;
    
    // DBGRUN disabled; 
    TCA1.SINGLE.DBGCTRL = 0x0;
    
    // CNTAEI disabled; CNTBEI disabled; EVACTA CNT_POSEDGE; EVACTB NONE; 
    TCA1.SINGLE.EVCTRL = 0x0;
    
    // CMP0 disabled; CMP1 disabled; CMP2 disabled; OVF disabled; 
    TCA1.SINGLE.INTCTRL = 0x0;
    
    // CMP0 disabled; CMP1 disabled; CMP2 disabled; OVF disabled; 
    TCA1.SINGLE.INTFLAGS = 0x0;
    
    // Period
    TCA1.SINGLE.PER = 0xFFDB;
    
    // Temporary data for 16-bit Access
    TCA1.SINGLE.TEMP = 0x0;
    
    // CLKSEL DIV1; ENABLE enabled; RUNSTDBY disabled; 
    TCA1.SINGLE.CTRLA = 0x1;
    
}

void TCA1_Start(void)
{
    TCA1.SINGLE.CTRLA|= TCA_SINGLE_ENABLE_bm;
}

void TCA1_Stop(void)
{
    TCA1.SINGLE.CTRLA&= ~TCA_SINGLE_ENABLE_bm;
}

void TCA1_Write(uint16_t timerVal)
{
    TCA1.SINGLE.CNT=timerVal;
}

uint16_t TCA1_Read(void)
{
    uint16_t readVal;

    readVal = TCA1.SINGLE.CNT;

    return readVal;
}

void TCA1_EnableInterrupt(void)
{
        TCA1.SINGLE.INTCTRL = 1 << TCA_SINGLE_CMP0_bp /* Compare 0 Interrupt: enabled */
	 				| 1 << TCA_SINGLE_CMP1_bp /* Compare 1 Interrupt: enabled */
	 				| 1 << TCA_SINGLE_CMP2_bp /* Compare 2 Interrupt: enabled */
	 				| 1 << TCA_SINGLE_OVF_bp; /* Overflow Interrupt: enabled */
}
void TCA1_DisableInterrupt(void)
{
    TCA1.SINGLE.INTCTRL = 0 << TCA_SINGLE_CMP0_bp /* Compare 0 Interrupt: disabled */
	 				| 0 << TCA_SINGLE_CMP1_bp /* Compare 1 Interrupt: disabled */
	 				| 0 << TCA_SINGLE_CMP2_bp /* Compare 2 Interrupt: disabled */
	 				| 0 << TCA_SINGLE_OVF_bp; /* Overflow Interrupt: disabled */
}
void TCA1_ClearOverflowInterruptFlag(void)
{
    TCA1.SINGLE.INTFLAGS &= ~TCA_SINGLE_OVF_bm; /* Overflow Interrupt: disabled */
}
bool TCA1_IsOverflowInterruptEnabled(void)
{
    return ((TCA1.SINGLE.INTFLAGS & TCA_SINGLE_OVF_bm) > 0);
}

void TCA1_ClearCMP0InterruptFlag(void)
{
    TCA1.SINGLE.INTFLAGS &= ~TCA_SINGLE_CMP0_bm; /* Compare Channel-0 Interrupt: disabled */
}

bool TCA1_IsCMP0InterruptEnabled(void)
{
    return ((TCA1.SINGLE.INTFLAGS & TCA_SINGLE_CMP0_bm) > 0);
}

void TCA1_ClearCMP1InterruptFlag(void)
{
    TCA1.SINGLE.INTFLAGS &= ~TCA_SINGLE_CMP1_bm; /* Compare Channel-1 Interrupt: disabled */
}

bool TCA1_IsCMP1InterruptEnabled(void)
{
    return ((TCA1.SINGLE.INTFLAGS & TCA_SINGLE_CMP1_bm) > 0);
}

void TCA1_ClearCMP2InterruptFlag(void)
{
    TCA1.SINGLE.INTFLAGS &= ~TCA_SINGLE_CMP2_bm; /* Compare Channel-2 Interrupt: disabled */
}

bool TCA1_IsCMP2InterruptEnabled(void)
{
    return ((TCA1.SINGLE.INTFLAGS & TCA_SINGLE_CMP2_bm) > 0);
}