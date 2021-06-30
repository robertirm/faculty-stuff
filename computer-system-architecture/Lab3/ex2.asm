bits 32 

global start        

extern exit               
import exit msvcrt.dll    

;Interpretare cu semn
;a - byte, b - word, c - double word, d - qword
segment data use32 class=data
    a db -2
    b dw 5
    c dd -6
    d dq 7

;a-d+b+b+c
segment code use32 class=code
    start:
        
        mov al,[a]  ;Al = a
        cbw         ;AX = a
        cwde        ;EAX = a
        cdq         ;EDX:EAX = a
        
        mov ecx,edx
        mov ebx,eax     ; ECX:EBX = a
        
        sub ebx,[d]
        sbb ecx,[d+4]   ; ECX:EBX = a-d
        
        mov ax,[b]
        cwde
        cdq             ; EDX:EAX = b
        
        add ebx,eax
        adc ecx,edx     ; ECX:EBX = a-d+b
        
        add ebx,eax
        adc ecx,edx     ; ECX:EBX = a-d+b+b
        
        mov eax,[c]
        cdq             ; EDX:EAX = c
        
        add ebx,eax
        adc ecx,edx     ; ECX:EBX = a-d+b+b+c
       
        ; exit(0)
        push    dword 0      
        call    [exit]       
