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


#ifndef TCA1_H_INCLUDED
#define TCA1_H_INCLUDED

#include <stdint.h>
#include <stdbool.h>
#include "../system/system.h"
#include "timer_interface.h"
#include "../system/utils/compiler.h"

#ifdef __cplusplus
extern "C" {
#endif

/**
 * \brief Initialize tca interface
 *
 * \return Initialization status.
 */
    
typedef void (*TCA1_cb_t)(void);    

extern const struct TMR_INTERFACE TCA1_Interface;

void TCA1_Initialize(void);
void TCA1_Start(void);
void TCA1_Stop(void);
void TCA1_OverflowCallbackRegister(TCA1_cb_t cb);
void TCA1_Compare0CallbackRegister(TCA1_cb_t cb);
void TCA1_Compare1CallbackRegister(TCA1_cb_t cb);
void TCA1_Compare2CallbackRegister(TCA1_cb_t cb);
void TCA1_EnableInterrupt(void);
void TCA1_DisableInterrupt(void);
uint16_t TCA1_Read(void);
void TCA1_Write(uint16_t timerVal);
void TCA1_ClearOverflowInterruptFlag(void);
bool TCA1_IsOverflowInterruptEnabled(void);
void TCA1_ClearCMP0InterruptFlag(void);
bool TCA1_IsCMP0InterruptEnabled(void);
void TCA1_ClearCMP1InterruptFlag(void);
bool TCA1_IsCMP1InterruptEnabled(void);
void TCA1_ClearCMP2InterruptFlag(void);
bool TCA1_IsCMP2InterruptEnabled(void);

#ifdef __cplusplus
}
#endif

#endif /* TCA1_H_INCLUDED */