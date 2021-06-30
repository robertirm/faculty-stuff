bits 32 

global start        

extern exit               
import exit msvcrt.dll    


;a,b,c - byte
segment data use32 class=data
   a db 10
   b db 8
   c db 5
      
;(a+(b-c))*3
segment code use32 class=code
    start:
        mov eax,0
        mov ebx,0
        
        mov bl,[b]          ; BL = b
        sub bl,[c]          ; BL = b-c
        
        mov al,[a]          ; AL = a
        add al,bl           ; AL = AL + BL = a+(b-c)
        
        mov ah,3            ; AH = 3 
        mul ah              ; AX = AL * 3 = (a+(b-c))*3
        
        push    dword 0      
        call    [exit]       
