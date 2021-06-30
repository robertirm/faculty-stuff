bits 32 
global start        

extern exit, printf               
import exit msvcrt.dll    
import printf msvcrt.dll

segment data use32 class=data
    a dw 61
    b dw 7
    cat dd 0
    rst dd 0
    format db "Cat = %i, rest = %i", 0
    
; 5. Se dau doua numere naturale a si b (a, b: word, definite in segmentul de date). 
; Sa se calculeze a/b si sa se afiseze catul si restul impartirii in urmatorul format: "Cat = <cat>, rest = <rest>"
; Exemplu: pentru a=23 si b=10 se va afisa: "Cat = 2, rest = 3"
; Valorile vor fi afisate in format decimal (baza 10) cu semn.

segment code use32 class=code
    start:
        
        ;realizam impartirea a/b 
        mov ax, [a]         
        cwd
        idiv word [b]       ; AX = catul  , DX = restul
        
        ;stocam catul si restul in memorie
        mov [cat],ax
        mov [rst],dx
        
        ;afisam in formatul cerut
        push dword [rst]
        push dword [cat]
        push dword format
        call [printf]
        add esp, 4*3
        
        push    dword 0      
        call    [exit]       
