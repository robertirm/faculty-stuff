bits 32

global start        

extern verif_prim
global e_prim
global aux

extern exit, printf, scanf               
import exit msvcrt.dll   
import printf msvcrt.dll
import scanf msvcrt.dll 

segment data use32 class=data
    sir_de_nr times 100 dd 0
    lun dd 0
    aux dd 0
    lun_prime dd 0
    format_msg1 db "Lungime sirului : ", 0 
    format_decimal db "%d",0
    spatiu db " ",0
    temp db 0
    e_prim db 0
    
; Se citeste de la tastatura un sir de numere in baza 10. Sa se afiseze numerele prime.
segment code use32 class=code
    start:
        push dword format_msg1
        call [printf]
        add esp, 4*1
        
        push dword lun
        push dword format_decimal
        call [scanf]
        add esp, 4*2 
       
        mov ecx, [lun]
        mov edi, sir_de_nr
        cld
        ;jecxz final
        loop_citire:
            ; citim un numar
            pusha
            push dword aux
            push dword format_decimal
            call [scanf]
            add esp,4*2
            
            call verif_prim
            
            ; daca e prim il stocam
            popa
            mov eax,[aux]
            mov bl,[e_prim]
            cmp bl,1
            jne negativ            
            stosd
            inc dword [lun_prime]
            negativ:
            mov [e_prim], byte 0
            
        loop loop_citire
        

        ; afisare numere prime
        mov ecx, [lun_prime]
        mov esi, sir_de_nr
        cld
        jecxz final
        loop_afisare:
            lodsd
            mov [temp],ecx
            mov [aux],eax
            push dword [aux]
            push dword format_decimal
            call [printf]
            add esp , 4*2
            
            push dword spatiu
            call [printf]
            add esp, 4
            
            mov ecx ,[temp]
        loop loop_afisare
        
    final:
        push    dword 0      
        call    [exit]       
