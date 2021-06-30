bits 32 

global start        

extern exit               
import exit msvcrt.dll 
   
;a,b,c - byte, d - word
segment data use32 class=data
    a db 10
    b db 5
    c db 7
    d dw 200
    
;[(10+d)-(a*a-2*b)]/c
segment code use32 class=code
    start:
        mov eax,0
        mov ebx,0
        mov edx,0
        
        mov dx , [d]        ; d = d + 10 
        add dx, word 10
        
        mov al,[b]           ; AL = b
        mov ah,2             ; AH = 2
        mul ah               ; AX = AH * AL = 2*b
        
        push ax              
        pop bx               ; BX = AX = 2*b
        
        mov al,[a]           ; AL = a
        mul al               ; AX = AL * AL = a*a
        
        sub ax,bx            ; AX = AX - BX = a*a - 2*b
        
        mov dx,[d]           ; DX = d + 10
        sub dx, ax           ; DX = DX - AX = (10+d)-(a*a-2*b)
        
        mov ax,dx            ; AX = DX = (10+d)-(a*a-2*b)
        div byte [c]         ; AL = AX/c = [(10+d)-(a*a-2*b)]/c  si AH = AX%c = [(10+d)-(a*a-2*b)]%c
        
        
        push    dword 0      
        call    [exit]       
