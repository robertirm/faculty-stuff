bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

;Interpretare fara semn
; a,b-byte; c-word; e-doubleword; x-qword                          
segment data use32 class=data
    a db 100
    b db 50
    c dw 2
    e dd 10
    x dq 5

;(a-b+c*128)/(a+b)+e-x
segment code use32 class=code
    start:
        mov ax,128
        mul word [c]     ; DX:AX = c*128
        
        push dx
        push ax
        pop ebx          ; EBX = c*128
        
        mov al,[a]
        sub al,[b]       ; AL= a-b
        mov ah,0         ; AX= a-b
        mov dx,0         ; DX:AX = a-b
        push dx
        push ax
        pop eax          ; EAX = a-b
        
        add eax,ebx      ; EAX = a-b+c*128
        
        push eax
        pop ax
        pop dx           ; DX:AX = EAX = a-b+c*128       
               
        mov bl,[a]
        add bl,[b]       ; BL = a+b
        mov bh, 0        ; BX = a+b
        
        div bx           ; AX = (DX:AX)/ BX = (a-b+c*128)/(a+b) ,  DX = restul
        
        mov dx,0         ; DX:AX = (a-b+c*128)/(a+b)
        push dx
        push ax
        pop eax          ; EAX = (a-b+c*128)/(a+b)
        
        add eax,[e]      ; EAX = (a-b+c*128)/(a+b)+e
        mov edx,0        ; EDX:EAX = (a-b+c*128)/(a+b)+e      
        
        sub eax,[x]
        sbb edx,[x+4]    ; EDX:EAX = (a-b+c*128)/(a+b)+e-x
        
        push    dword 0      
        call    [exit]       
