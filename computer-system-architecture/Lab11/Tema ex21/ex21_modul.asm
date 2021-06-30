bits 32
global verif_prim
extern e_prim, aux

segment code use32 class=code
    verif_prim:
        mov eax,[aux]

        cmp eax,0
        je nu_e_prim
            
        cmp eax,1
        je nu_e_prim
            
        cdq   ; EDX:EAX = nr
            
        ; i = 2...(n-1)
        mov ecx,2           
        mov ebx,[aux]        
        dec ebx
        
        ; for
        loop_divizibil:
            ; if(n%i==0)
            div dword ecx   
            cmp edx,0        
            je nu_e_prim
             
            ;refacem numarul
            mov eax,[aux]
            cdq
               
            ;pasul urmator
            inc ecx         
            cmp ecx,ebx     
        jl loop_divizibil
                
        ;este_prim
        mov [e_prim],byte 1
        jmp pas
        nu_e_prim:
            mov [e_prim], byte 0
        pas:
        
        ret