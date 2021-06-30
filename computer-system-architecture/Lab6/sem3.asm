bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 11223344h, 55667788h

; our code starts here
segment code use32 class=code
    start:
        mov esi,a 	; a - sirul sursa este a 
        mov edi,a+5 	; a+5 - sirul destinatie
        lodsb		; AL = 44h
        mov ah,al 	; AX = 4444h
        lodsb		; AL = 33h
        lodsb		; AL = 22h  (AX=4422h)
        stosw		; se stocheaza AX pe [a+5] si [a+6] 
    
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
