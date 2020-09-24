; biblioteca das fun??es do LCD
LCDCMDO         EQU     0FF40H          ;ENDERECO DE COMANDO DO LCD
LCDDADO         EQU     0FF41H          ;ENDERECO DE DADO DO LCD
	
;INICIO DA ROTINA DE INICIALIZACAO DO LCD

INITLCD:        MOV A,#39H              ;DEFINE INTERFACE LCD DE 8 BITS/2 LINHAS/MATRIX 7x5
                CALL CMDOLCD            ;CHAMA ROTINA ENVIA COMANDO AO LCD
                MOV A,#06H              ;DESLOCA CURSOR A DIREITA
                CALL CMDOLCD            ;CHAMA ROTINA ENVIA COMANDO AO LCD
                MOV A,#0CH              ;MENSAGEM APARENTE E CURSOR DESLIGADO
                CALL CMDOLCD            ;CHAMA ROTINA ENVIA COMANDO AO LCD
                CALL CLEARLCD           ;CHAMA ROTINA LIMPA LCD
                RET                     ;FIM DA ROTINA DE INICIALIZACAO DO LCD

;INICIO DA ROTINA ENVIA DADO AO LCD

DADOLCD:        PUSH DPH                ;carrego na pilha
                PUSH DPL                ;carrego na pilha, para o DPTR funcionar
                MOV DPTR,#LCDDADO		;DPTR são o DPH e DPL
                MOVX @DPTR,A            ;ENVIA DADO AO LCD
                MOV R4,#20H             ;
DELAYDADOLCD:   DJNZ R4,DELAYDADOLCD    ;DELAY DE DADO DO LCD
                POP DPL                 ;RESTAURA O CONTEUDO DO REGISTRADOR DPTR
                POP DPH                 ;RESTAURA O CONTEUDO DO REGISTRADOR DPTR
                RET                     ;FIM DA ROTINA ENVIA DADO AO LCD, reseta

;INICIO DA ROTINA ENVIA COMANDO AO LCD

CMDOLCD:        PUSH DPH
                PUSH DPL
                MOV DPTR,#LCDCMDO		;comando
                MOVX @DPTR,A            ;ENVIA COMANDO AO LCD
                MOV R4,#20H             ;
DELAYCMDOLCD:   DJNZ R4,DELAYCMDOLCD    ;DELAY DE COMANDO DO LCD
                POP DPL					;RESTAURA O CONTEUDO DO REGISTRADOR DPTR
                POP DPH					;RESTAURA O CONTEUDO DO REGISTRADOR DPTR
                RET                     ;FIM DA ROTINA ENVIA COMANDO AO LCD

;INICIO DA ROTINA LIMPA LCD

CLEARLCD:       PUSH DPH                ;SALVA O CONTEUDO DO REGISTRADOR DPTR
                PUSH DPL                ;SALVA O CONTEUDO DO REGISTRADOR DPTR
                MOV A,#01H              ;LIMPA LCD E RETORNA CURSOR A POSICAO 80H
                MOV DPTR,#LCDCMDO
                MOVX @DPTR,A            ;ENVIA COMANDO AO LCD
                MOV R5,#06H             ;tempo para limpar o LCD 5 no caso
DELAYCLRLCD5:   MOV R4,#0FFH            ;tempo para limpar o LCD 4
DELAYCLRLCD4:   DJNZ R4,DELAYCLRLCD4    ;DElay de comando clear do LCD
                DJNZ R5,DELAYCLRLCD5    ;DELAY DE COMANDO CLEAR DO LCD
                POP DPL                 ;RESTAURA O CONTEUDO DO REGISTRADOR DPTR
                POP DPH                 ;RESTAURA O CONTEUDO DO REGISTRADOR DPTR
                RET                     ;FIM DA ROTINA LIMPA LCD

;INICIO DA ROTINA ESCREVE MENSAGEM NO LCD
                                        
MENSAGE:        MOV A,#00H              ;Move o valor o em A
                MOVC A,@A+DPTR          ;BUSCA MENSAGEM LETRA A LETRA
                CJNE A,#00H,MOSTRA      ;VERIFICA FIM DE MENSAGEM,SE NAO,DESVIA
                                        ;PARA O ROTULO "MOSTRA"
                JMP ENDMENS             ;DESVIA PARA O ROTULO "ENDMENS"
MOSTRA:         CALL DADOLCD            ;CHAMA A ROTINA ENVIA DADO AO LCD
                INC DPTR
                JMP MENSAGE             ;DESVIA PARA O ROTULO "MENSAGE"
ENDMENS:        RET                     ;FIM DA ROTINA ESCREVE MENSAGEM NO LCD