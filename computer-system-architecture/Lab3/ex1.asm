bits 32 

global start        

extern exit               
import exit msvcrt.dll    

;Interpretare fara semn
;a - byte, b - word, c - double word, d - qword  
segment data use32 class=data
    a db 2
    b dw 1234h
    c dd 100012h
    d dq 1200054005h

;(d+d-b)+(c-a)+d    
segment code use32 class=code
    start:
        mov ebx, [d]
        mov ecx, [d+4]    ; ECX:EBX = d
        
        add ebx, [d]
        adc ecx, [d+4]    ; ECX:EBX = d+d
        
        ; b(word) -> b(dword) -> b(qword)
        mov ax,[b]        ; AX = b(word)
        mov dx,0          ; DX:AX = b(dword)
        push dx
        push ax
        pop eax           ; EAX = b
        mov edx,0         ; EDX:EAX = b(qword)
        
        sub ebx,eax
        sbb ecx,edx       ; ECX:EBX = d+d-b
        
        ;c(dword) ->c(qword)
        mov eax,[c]
        mov edx, 0        ; EDX:EAX = c
        
        push ebx
        push ecx          ;salvam rezultatul d+d-b pe stiva
        
        ;a(byte) -> a(word) -> a(dword) -> a(dword)
        mov bl,[a]
        mov bh,0          ;BX=a
        mov cx,0          ;CX:BX = a
        push cx
        push bx
        pop ebx           ;EBX = a
        mov ecx,0         ;ECX:EBX = adc
        
        sub eax,ebx
        sbb edx,ecx       ;EDX:EAX = c-a
        
        pop ecx
        pop ebx           ;ECX:EBX = d+d-b
        
        add ebx,eax
        adc ecx,edx       ;ECX:EBX = (d+d-b) + (c-a)
        
        add ebx, [d]
        adc ecx, [d+4]    ;ECX:EBX = (d+d-b) + (c-a) + d
        
        
        
        
       
        ; exit(0)
        push    dword 0      
        call    [exit]       
