bits 32 

global start        

extern exit               
import exit msvcrt.dll    


; a - byte , b- word
segment data use32 class=data
    a db 10
    b dw 40
    c resb 4     ; rezerva o locatie de memorie de 4 octeti pentru c
    
; (b/a *2 + 10 )* b - b * 15
segment code use32 class=code
    start:
        
        
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
