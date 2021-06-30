bits 32 ; assembling for the 32 bits architecture

global start        

extern exit,printf,scanf               
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
  mesaj db "Rezultatul este: %d", 0
  
segment code use32 class=code
    procedura:
       
      
    start:
        
        done:
       
    