bits 32 
global start        

extern exit, printf, scanf               
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
    mesaj1 db "octet = ", 0
    mesaj2 db "cuvant = ", 0
    format1 db "%d", 0
    format2 db "%d", 0
    rez1 db "DA", 0
    rez2 db "NU", 0
    oct db 0
    cuv dw 0
    
; 19 . Sa se citeasca de la tastatura un octet si un cuvant. 
; Sa se afiseze pe ecran daca bitii octetului citit se regasesc consecutiv printre bitii cuvantului. Exemplu:
; a = 10 = 0000 1010b
; b = 256 = 0000 0001 0000 0000b
; Pe ecran se va afisa NU.
; a = 0Ah = 0000 1010b
; b = 6151h = 0110 0001 0101 0001b
; Pe ecran se va afisa DA (bitii se regasesc pe pozitiile 5-12)
    
segment code use32 class=code
    start:
        ;citire octet
        push dword mesaj1
        call [printf]
        add esp, 4*1    
        push dword oct
        push dword format1
        call [scanf]
        add esp, 4*2
        
        ;citire cuvant
        push dword mesaj2
        call [printf]
        add esp, 4*1
        push dword cuv
        push dword format2
        call [scanf]
        add esp, 4*2
        
        ;verificare cerinta
        mov ecx,9 
        mov eax,[cuv]
        repeta:
            cmp al,[oct]
            jz afirmativ
            shr eax,1
        loop repeta
        
        ;caz negativ
        push dword rez2
        call [printf]
        add esp,4*1
        jmp final
        
        ;caz afirmativ
        afirmativ:
            push dword rez1
            call [printf]
            add esp,4*1
            jmp final
            
         
    final:    
        push    dword 0      
        call    [exit]       
