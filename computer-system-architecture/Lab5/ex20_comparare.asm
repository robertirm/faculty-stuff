bits 32 

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    a db 2, 1, 3, 3, 4, 2, 6
    len_a equ $-a
    b db 4, 5, 7, 6, 2, 1
    len_b equ $-b
    r times len_a+len_b db 0
    
; Se dau 2 siruri de octeti A si B. Sa se construiasca sirul R care sa contina elementele lui B in ordine inversa urmate de elementele pare ale lui A.
; Exemplu:
; A: 2, 1, 3, 3, 4, 2, 6
; B: 4, 5, 7, 6, 2, 1
; R: 1, 2, 6, 7, 5, 4, 2, 4, 2, 6

segment code use32 class=code
    start:
        mov ecx , len_b
        mov esi,0
        jecxz final
        repeta:
            mov al,[b+ecx-1]
            mov [r+esi],al
            inc esi
        loop repeta
        
        mov ecx, len_a
        mov edi, 0
        repeta2:
            mov al,[a+edi]
            test al,1
            jg este_impar
            mov [r+esi],al
            inc esi
            este_impar:
                inc edi
        loop repeta2
            
        
        
    final:    
        push    dword 0      
        call    [exit]       
