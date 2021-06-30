bits 32 
global start        

extern exit               
import exit msvcrt.dll    

;ex 19                          
;Se da un cuvant A. Sa se obtina dublucuvantul B astfel:
;bitii 28-31 ai lui B sunt 1
;bitii 24- 25 si 26-27 ai lui B sunt bitii 8-9 ai lui A
;bitii 20-23 ai lui B sunt bitii 0-3 inversati ca valoare ai lui A ;
;bitii 16-19 ai lui B sunt biti de 0
;bitii 0-15 ai lui B sunt identici cu bitii 16-31 ai lui B.

segment data use32 class=data
    a dw 0111010101010111b                  
    b dd 0   ; 1111 0101 1000 0000 1111 0101 1000 0000 / F580F580


segment code use32 class=code
    start:
        mov ebx,0    ; stocam rezultatul in BX
        
        ; bitii 28-31 ai lui B sunt 1
        or ebx, 11110000000000000000000000000000b   
        
        
        ;bitii 24- 25 si 26-27 ai lui B sunt bitii 8-9 ai lui A
        mov eax,0
        mov ax,[a]          
        and ax,0000001100000000b   ; izolam 8-9 bitii lui a
        mov cl,16
        rol eax,cl     ; rotim 16 pozitii spre stanga
        or ebx,eax     
        mov cl,2
        rol eax,cl      ; rotim 2 pozitii spre stanga
        or ebx,eax
        
        
        ;bitii 20-23 ai lui B sunt bitii 0-3 inversati ca valoare ai lui A ;
        mov eax,0
        mov ax,[a]
        not ax                          ;inversam bitii
        and ax,0000000000001111b        ; izolam bitii 0-3
        mov cl,20
        rol eax,cl
        or ebx,eax
        
        
        ;bitii 16-19 ai lui B sunt biti de 0
        and ebx,11111111111100001111111111111111b
        
        
        ;bitii 0-15 ai lui B sunt identici cu bitii 16-31 ai lui B.
        mov eax,ebx
        and eax,11111111111111110000000000000000b    ; izolam bitii 16-31
        mov cl,16
        ror eax,cl          ;rotim 16 pozitii la dreapta
        or ebx,eax
        
        mov [b] , ebx   
        
        push    dword 0      
        call    [exit]       
