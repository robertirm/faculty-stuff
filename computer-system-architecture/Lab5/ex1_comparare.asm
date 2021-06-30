bits 32
global start        

extern exit               
import exit msvcrt.dll    
                          
segment data use32 class=data
    s db 1,2,3,4
    len equ $-s
    d times len dw 0

; Se da un sir de octeti S de lungime l. Sa se construiasca sirul D de lungime l-1 astfel incat elementele din D sa reprezinte produsul dintre fiecare 2 elemente consecutive S(i) si S(i+1) din S.
; Exemplu:
; S: 1, 2, 3, 4
; D: 2, 6, 12

segment code use32 class=code
    start:
        mov eax,0
        mov ecx,len-1
        mov esi, 0
        mov edx, 0
        jecxz final
        repeta:
            mov al,[s+esi]
            inc esi
            mul byte [s+esi]
            mov [d+edx],ax
            inc edx
            inc edx
        loop repeta
    
    final:
        push    dword 0      
        call    [exit]       
