bits 32 
global start        

extern exit, printf, scanf               
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
   a dd 0
   b dd 0
   msg1 db "a = ",0
   msg2 db "b = ",0
   format db "%x",0
   suma dd 0
   dif dd 0
   msg3 db "suma = %x  ",0
   msg4 db "diferenta = %x",0
    

; Sa se citeasca de la tastatura  doua numere a si b de tip word. 
; Sa se afiseze in baza 16 numarul c de tip dword pentru care partea low este suma celor doua numere,
; iar partea high este diferenta celor doua numere. Exemplu:
; a = 574, b = 136
; c = 01B602C6h

segment code use32 class=code
    start:
        
        ;citire a
        push dword msg1
        call [printf]
        add esp , 4*1
        push dword a
        push dword format
        call [scanf]
        add esp, 4*2
        
        ;citire b
        push dword msg2
        call [printf]
        add esp , 4*1        
        push dword b
        push dword format
        call [scanf]
        add esp, 4*2
        
        ;curatam eax si ebx
        mov eax, 0
        mov ebx,0
        
        mov eax, [a]
        mov ebx, [b]
        
        ;aflam suma partilor low
        add [suma],ax
        add [suma],bx
        
        ;aflam diferenta partilor high
        rol eax,16
        rol ebx,16 
        mov [dif], ax
        sub [dif], bx
        
        ;afisam suma
        push dword [suma]
        push dword msg3
        call [printf]
        add esp,4*2
        
        ;afisam diferenta
        push dword [dif]
        push dword msg4
        call [printf]
        add esp,4*2
        
        
        
        push    dword 0      
        call    [exit]       
