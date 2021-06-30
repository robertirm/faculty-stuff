bits 32 

global start        

extern exit               
import exit msvcrt.dll    
                    
segment data use32 class=data
    s dd 12345678h, 1A2B3C4Dh, 0FE98DC76h
    len equ ($-s)/4
    zece db 10 
    d times len db 0
   
; 26 . Se da un sir de dublucuvinte. Sa se obtina sirul format din octetii superiori 
; ai cuvintelor inferioare din elementele sirului de dublucuvinte, care sunt multiplii de 10.
    
segment code use32 class=code
    start:
        mov ecx,len     
        jecxz final
        mov esi, s      ;sirul sursa
        mov edi, d      ;sirul destinatie
        cld             ;parcurgem de la stanga la dreapta
        
        repeta:
            lodsd       ; in EAX avem cuvantul inferior
            shr ax,8    ; mutam bitii cu 8 pozitii spre dreapta
            
            mov bl,al   ; memoram octetul de care avem nevoie
            div byte[zece]  
            cmp ah, 0       ; verificam daca e multiplu de 10
            jnz nu_e_multiplu
            
            mov al,bl       ;in caz afirmativ in adaugam in sirul destinatie
            stosb
           
            nu_e_multiplu:
        loop repeta
    
    final:
        push    dword 0      
        call    [exit]       
