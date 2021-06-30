bits 32
global start        

extern exit               
import exit msvcrt.dll    
                          
segment data use32 class=data
    s1 db '+', '2', '2', 'b', '8', '6', 'X', '8'
    len1 equ $-s1
    s2 db 'a', '4', '5'
    len2 equ $-s2
    d times len1+len2 db 0

; 10 . Se dau doua siruri de caractere S1 si S2. Sa se construiasca sirul D prin concatenarea elementelor sirului S2 in ordine inversa cu elementele de pe pozitiile pare din sirul S1.
; Exemplu:
; S1: '+', '2', '2', 'b', '8', '6', 'X', '8'
; S2: 'a', '4', '5'
; D: '5', '4', 'a', '2','b', '6', '8'

segment code use32 class=code
    start:
        ;punem in D elementele din S2 in ordine inversa
        mov ecx,len2
        mov esi,0       ;index pentru D
        jecxz final
        repeta:
            mov al,[s2+ecx-1]
            mov [d+esi], al
            inc esi
        loop repeta
        
        ;punem in D elementele de pe pozitiile pare din S1
        ;din exemplu am inteles ca sirul incepe de la pozitia 1
        mov ecx,len1
        
        mov al,len1     ;testam daca lungimea sirului este impara 
        test al, 1b     ;deoarece decrementarea din 2 in 2 poate duce la o bucla infinita(ecx !=0)
        je lun_para
        dec ecx
        
    lun_para:    
        mov ebx,1       ;index pentru s1
        jecxz final
        repeta2:
            mov al,[s1+ebx]
            mov [d+esi],al
            inc esi
            inc ebx
            inc ebx
            dec ecx
        loop repeta2
    
    final:
        push    dword 0      
        call    [exit]       
