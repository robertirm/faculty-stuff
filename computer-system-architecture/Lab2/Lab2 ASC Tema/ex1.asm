bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          

segment data use32 class=data

;  16/4 
segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0      ; curatam eax si ebx
        
        
        mov ax, 16    ; AX = 16    
        mov bl, 4     ; BL = 4
        div bl        ; AL = 16/4 = 4  
    
        push    dword 0      
