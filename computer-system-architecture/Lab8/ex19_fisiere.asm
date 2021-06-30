bits 32 
global start       
 
extern exit, fopen, fclose, fprintf              
import exit msvcrt.dll    
import fopen msvcrt.dll  
import fclose msvcrt.dll
import fprintf msvcrt.dll
                        
segment data use32 class=data
    fisier db "suma.txt",0
    descriptor dd -1
    mod_acces db "w",0
    format db "Suma cifrelor din text este %d",0
    sir db "2 + 2 e egal cu 4 , scadem 3 , mai ramane 1 , foarte simplu",0   ; suma = 12
    len equ $-sir
    suma db 0
    
; 19. Se dau in segmentul de date un nume de fisier si un text (poate contine orice tip de caracter). 
;   Sa se calculeze suma cifrelor din text. 
;   Sa se creeze un fisier cu numele dat si sa se scrie suma obtinuta in fisier.

segment code use32 class=code
    start:
        ; deschidem fisierul
        push dword mod_acces
        push dword fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor], eax
        
        ; verificam daca fisierul a fost creat
        cmp eax,0
        je final
        
        ; parcurgem textul caracter cu caracter
        mov ecx, len
        mov esi, sir
        jecxz final
        parcurgere:
            lodsb
            ; verificam daca caracterul curent este cifra
            cmp al, '0'
            jb nu_e_cifra
            cmp al, '9'
            ja nu_e_cifra
            
            ; in caz afirmativ il adunam in suma totala a cifrelor
            sub al, '0'      ; convertim in nr natural
            add [suma], al
            
            nu_e_cifra:  
        loop parcurgere
        
        ; scriem suma in fisier
        push dword [suma]
        push dword format
        push dword [descriptor]
        call [fprintf]
        add esp, 4*3
        
        ; inchidem fisierul
        push dword [descriptor]
        call [fclose]
    final:
        push    dword 0      
        call    [exit]       
