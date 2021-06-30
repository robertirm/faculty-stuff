bits 32 

global start        

extern exit, printf, scanf               
import exit msvcrt.dll
import printf msvcrt.dll 
import scanf msvcrt.dll   
                          
segment data use32 class=data
    a dd 0
    b dd 0
    sum dd 0
    msg_a db 'a = ', 0
    msg_b db 'b = ', 0
    format_r db "%d", 0
    format_p db "Suma = %d", 0
    
    
; vom calcula suma a doua nr , a+b , citite de la tastatura
segment code use32 class=code

    suma_1:
        add eax, edx
        ret 
        
    start:
        push dword msg_a
        call [printf]
        add esp, 4*1
        
        push dword a
        push dword format_r
        call [scanf]
        add esp, 4*2
        
        push dword msg_b
        call [printf]
        add esp, 4*1
        
        push dword b
        push dword format_r
        call [scanf]
        add esp, 4*2
        
        mov eax, [a]
        mov edx, [b]
        call suma_1
        mov [sum], eax 

        push dword [sum]
        push dword format_p
        call [printf]
        add esp, 4*2
        
        push    dword 0      
        call    [exit]       
