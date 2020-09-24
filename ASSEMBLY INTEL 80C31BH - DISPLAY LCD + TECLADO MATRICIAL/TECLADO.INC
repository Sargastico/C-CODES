COL_TECLADO		EQU     0FF50H
LIN_TECLADO		EQU     0FF60H 
LINHA0          EQU     007EH    ; = 0111 1110
LINHA1          EQU     007DH	 ; = 0111 1101
LINHA2          EQU     007BH	 ; = 0111 1011 
LINHA3          EQU     0077H	 ; = 0111 0111
LINHA4          EQU     006FH	 ; = 0110 1111
LINHA5          EQU     005FH	 ; = 0101 1111

;ROTINA DO TECLADO
;=====================================================================================================================================================
;=====================================================================================================================================================

;INCIALIZA LINHA POR LINHA E LE A COLUNA PARA IDENTIFICAR A TECLA . CAPTURA APENAS A PRIMEIRA
;=====================================================================================================================================================
LER_TECLADO:	
LIN0:    		MOV A,#LINHA0	    	;INICIALIZA A LINHA 0
				CALL LER_UMA_LINHA
				;ret
				JZ LIN1					;VERIFICA AS TECLAS DA LINHA 0, SEN?O VAI PARA LINHA 1
				RET
LIN1:
				MOV A,#LINHA1	    	;INICIALIZA A LINHA 1
				CALL LER_UMA_LINHA
				JZ LIN2			   		;VERIFICA AS TECLAS DA LINHA 1, SEN?O VAI PARA LINHA 2
				ADD A,#10;		   		;TEM UMA TECLA NA LINHA 1
				RET
			   
LIN2:       	MOV A,#LINHA2	    	;INICIALIZA A LINHA 2
				CALL LER_UMA_LINHA
			    JZ LIN3					;VERIFICA AS TECLAS DA LINHA 2, SEN?O VAI PARA LINHA 3
				ADD A,#20;		   		;TEM UMA TECLA NA LINHA 2
				RET

LIN3:		   	MOV A,#LINHA3	    	;INICIALIZA A LINHA 3
				CALL LER_UMA_LINHA
			    JZ LIN4					;VERIFICA AS TECLAS DA LINHA 3, SEN?O VAI PARA LINHA 4
				ADD A,#30;		   		;TEM UMA TECLA NA LINHA 3
				RET

LIN4:		   	MOV A,#LINHA4	    	;INICIALIZA A LINHA 4
				CALL LER_UMA_LINHA
			    JZ LIN5					;VERIFICA AS TECLAS DA LINHA 4, SEN?O VAI PARA LINHA 5
				ADD A,#40;		   		;TEM UMA TECLA NA LINHA 4
				RET

LIN5:			MOV A,#LINHA5	    	;INICIALIZA A LINHA 5
				CALL LER_UMA_LINHA
				JZ NENHUMA_TECLA		;VERIFICA AS TECLAS DA LINHA 5, SEN?O VAI PARA O LABEL NENHUMA_TECLA
				ADD A,#50;		   		;TEM UMA TECLA NA LINHA 5

;RETORNA PARA O LABEL LER_TECLADO
;=====================================================================================================================================================				
NENHUMA_TECLA: 	RET
;EFETUA O AJUSTE QUANTO A LINHA E COLUNA
;=====================================================================================================================================================
LER_UMA_LINHA:
				MOV DPTR,#LIN_TECLADO	;AJUSTA A LINHA	DO TECLADO
				MOVX @DPTR,A     
				
				MOV DPTR,#COL_TECLADO	;AJUSTA A COLUNA DO TECLADO
				MOVX A,@DPTR
				
				CALL AJUSTA_VALOR		;AJUSTA O VALOR DO TECLADO
			    JZ RETORNO_LER_LINHA
				
				CALL DELAYTC       		;ESTAS 3 LINHAS CAUSAM O DEBOUNCE
				MOVX A,@DPTR			;(ESPERA UM TEMPO E VERIFICA SE A
				CALL AJUSTA_VALOR		;TECLA AINDA ESTA APERTADA.SEN?O ? RUIDO)

RETORNO_LER_LINHA:
				RET              
                
AJUSTA_VALOR:	
				CPL A		 			;APENAS NO SIMULADOR - Operação lógica NOT
				ORL A,#0E0H				;Operação lógica OR 
				CPL A					;Operação lógica NOT
				RET
;=====================================================================================================================================================


;INICIO DA ROTINA DELAY				
;=====================================================================================================================================================
;=====================================================================================================================================================
DELAYTC:          MOV 03H,07FH			     
DELAYtc02:        MOV 02H,0FFH     
                                
DELAYtc01:        DJNZ R2,DELAYtc01			;CARREGA NOS REGISTRADORES R2 E R3 DO BANCO 0
                  DJNZ R3,DELAYtc02			;VALORES CONVENIENTES PARA GERAR ATRASO NECESSARIO

                RET
;=====================================================================================================================================================				
;FIM DA ROTINA DELAY