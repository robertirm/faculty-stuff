bits 32 

global start        

extern exit               
import exit msvcrt.dll    

; Interpretare cu semn
; a,b-byte; c-word; e-doubleword; x-qword
segment data use32 class=data
    a db 100
    b db -20
    c dw 2
    e dd -10
    x dq 6

;(a-b+c*128)/(a+b)+e-x
segment code use32 class=code
    start:
        mov ax,128
        imul word [c]         ; DX:AX = c*128
        
        push dx
        push ax
        pop ebx         ; EBX = c*128
        
        mov al,[a]
        sub al,[b]
        cbw
        cwde            ; EAX = a-b

        add eax,ebx     ; EAX = a-b+c*128
        
        push eax        ;retinem EAX = a-b+c*128 pe stiva
     
        mov al,[a]
        add al,[b]      ; Al = a+b
        cbw             ; AX = a+b
        
        mov bx,ax       ; BX = a+b
        idiv bx         
        
        pop ax
        pop dx          ; DX:AX = a-b+c*128
        
        idiv bx         ; AX = (DX:AX)/BX = (a-b+c*128)/(a+b)   , DX = restul
        
        cwd             ; EAX = (a-b+c*128)/(a+b)
        add eax,[e]     ; EAX = (a-b+c*128)/(a+b)+e
        cdq             ; EDX:EAX = (a-b+c*128)/(a+b)+e
        
        sub eax,[x]
        sbb edx,[x+4]    ; EDX:EAX = (a-b+c*128)/(a+b)+e-x
        
        push    dword 0      
        call    [exit]       
