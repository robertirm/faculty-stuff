bits 32

global _convertire

segment data public data use32

segment code public code use32

_convertire:
    push ebp
    mov ebp,esp
    
    mov ecx, [ebp+8]
    jecxz final
    mov esi, [ebp+12]
    mov ebx, 1
    mov edx, 0
    cld
    
    repeta:
        lodsb
        cmp al,31h
        jne pas
        
        add edx,ebx
        pas:
        add ebx,ebx
    loop repeta
    mov eax,edx
    final:
    mov esp,ebp
    pop ebp
    
    ret