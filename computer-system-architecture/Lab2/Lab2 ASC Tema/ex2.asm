bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                          
; a,b,c,d - byte
segment data use32 class=data
    a db 5
    b db 1
    c db 6
    d db 6


;(a+b+b)-(c+d)
segment code use32 class=code
    start:
        mov eax , 0
        mov ebx , 0
    
        mov al , [a]    ; AL = a
        add al , [b]    ; AL = AL + b = a + b
        add al , [b]    ; AL = AL + b = a + b + b
        
        mov bl, [c]     ; BL = c
        add bl, [d]     ; BL = BL + d = c + d
        
        sub al,bl       ; AL = AL - BL = (a+b+b)-(c+d)
        
        push    dword 0      
