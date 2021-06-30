bits 32

global start

extern exit
import exit msvcrt.dll
 
;a,b,c,d - word
segment data use32 class=data
    a dw 10
    b dw 25
    c dw 20
    d dw 30


;(b-a)-(c+c+d)
segment code use32 class=code
    start:
        mov eax, 0
        mov ebx, 0
        
        mov ax , [b]    ; AX = b
        sub ax , [a]    ; AX = AX - a = b - a
        
        mov bx , [c]    ; BX = c
        add bx , [c]    ; BX = BX + c = c + c
        add bx , [d]    ; BX = BX + d = c + c + d
    
        sub ax, bx      ; AX = AX - BX = ( b - a ) - ( c + c + d )

        push dword 0      
        call [exit]       