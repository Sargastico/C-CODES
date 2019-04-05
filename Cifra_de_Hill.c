//Cifra de Hill

#include <stdio.h>
#include <stdlib.h>

char *mensagem,*mensagem_c;

int i,i2,j,t_matriz1,t_matriz2,num,op,Aux,p;

int identidade,size;

int m_chave;

int m_cifrada;

/* TABELA DE SUBSTITUIÇÃO DE CARACTERES

A=01	J=10	S=19
B=02	K=11	T=20
C=03	L=12	U=21
D=04	M=13	V=22
E=05	N=14	W=23
F=06	O=15	X=24
G=07	P=16	Y=25
H=08	Q=17	Z=26
I=09	R=18

*/

int matriz_ponteiro(int linhas, int colunas, int matriz[linhas][colunas]) {
    int lin, col;
    for (lin = 0; lin < linhas; lin++) {
        for (col = 0; col < colunas; col++) {
            printf("\t%d", matriz[lin][col]);
        }
        return matriz[lin][col];
    }
}


int main (){

	printf("Voce deseja: criptografar [1] ou descriptografar [2]");
	scanf("%d",op);
    printf("Insira a quantidade des caracteres da msg:");
    scanf("%d",p);
    mensagem = (int *)malloc(p * sizeof(int));
	printf("Insira a mensagem cifrada: \n");
	scanf("%c",mensagem);

	printf("Insira o tamanho da matriz chave: \n");
	printf("num1: \n");
	scanf("%d",t_matriz1);
	printf("num2: \n");
	scanf("%d",t_matriz2);
	printf("Insira os valores a matriz chave. \n");

	size = sizeof(mensagem);
//Substituição das letras da mensagem por números
	for (i=0,i<=size,i++){

		if (mensagem[i] = 'A'){mensagem_c = 1;}else if (mensagem[i] = 'B'){mensagem_c = 2;}else if (mensagem[i] = 'C'){mensagem_c = 3;}else if (mensagem[i] = 'D'){mensagem_c = 4;}else if (mensagem[i] = 'E'){
			mensagem_c = 5;
		}
		else if (mensagem[i] = 'F'){mensagem_c = 6;}else if (mensagem[i] = 'G'){mensagem_c = 7;}else if (mensagem[i] = 'H'){mensagem_c = 8;}else if (mensagem[i] = 'I'){mensagem_c = 9;}else if (mensagem[i] = 'J'){
			mensagem_c = 10;
		}
		else if (mensagem[i] = 'K'){mensagem_c = 11;}else if (mensagem[i] = 'L'){mensagem_c = 12;}else if (mensagem[i] = 'M'){mensagem_c = 13;}else if (mensagem[i] = 'N'){mensagem_c = 14;}else if (mensagem[i] = 'O'){
			mensagem_c = 15;
		}
		else if (mensagem[i] = 'P'){mensagem_c = 16;}else if (mensagem[i] = 'Q'){mensagem_c = 17;}else if (mensagem[i] = 'R'){mensagem_c = 18;}else if (mensagem[i] = 'S'){mensagem_c = 19;}else if (mensagem[i] = 'T'){
			mensagem_c = 20;
		}
		else if (mensagem[i] = 'U'){mensagem_c = 21;}else if (mensagem[i] = 'V'){mensagem_c = 22;}else if (mensagem[i] = 'W'){mensagem_c = 23;}else if (mensagem[i] = 'X'){mensagem_c = 24;}else if (mensagem[i] = 'Y'){
			mensagem_c = 25;
		}
		else{
			mensagem_c = 26;
		}
	}

	switch(op){

		//Criptografia
		case '1':

			//Obter matriz chave
			for(i=0,i<=t_matriz1,i++){
				for(i2=t_matriz2,i2!=0,i2--){
					printf("[%d]x[%d] = ",i,i2);
					scanf("%d",m_chave[i][i2]);
				}
			}

			//m_cifrada = (mensagem_c)*(m_chave);
			for(i=0; i<lA; i++){
        		for(j=0; j<cB; j++){
                 matrizC[i][j]=0;
                 	for(X=0; X<lB; X++){
                 		Aux += matriz[i] * m_chave[X][j];
                    }
                 	m_Cifrada[i][j]=Aux;
                 	Aux=0;
                }
            }
            
			printf("%c",m_cifrada);
		break;

		//Descriptografia
		case '2':

			//Obtem matriz chave
			for(i=0,i<=t_matriz1,i++){
				for(i2=t_matriz2,i2!=0,i2--){
					printf("[%d]x[%d] = ",i,i2);
					scanf("%d",m_chave[i][i2]);
				}
			}

			//Gerador da matriz identidade
			for(i=0,i<t_matriz1,i++){
				for(i2=0;j<t_matriz2.j++){
					if(i==j){
						identidade[i][k] = 1;
					}else{
						identidade[i][j] = 0;
					}
				}
			}

			//m_clara = (mensagem)*(identidade); //CORRIGIR
			for(i=0; i<lA; i++){
        		for(j=0; j<cB; j++){
                 matrizC[i][j]=0;
                 	for(X=0; X<lB; X++){
                 		Aux += matriz[i][X] * m_chave[X][j];
                    }
                 	m_Cifrada[i][j]=Aux;
                 	Aux=0;
                }
            }


			print(m_clara);


	}
}
