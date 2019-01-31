#include <iostream>

using namespace std;

class op_basica {
public:

	void soma(float a, float b) {
		float resultado = a + b;
		cout << ("Resultado: ") << resultado << endl;
	}

	void subtracao(float a, float b) {
		float resultado = a - b;
		cout << ("Resultado: ") << resultado << endl;
	}

	void multiplicacao(float a, float b) {
		float resultado = a * b;
		cout << ("Resultado: ") << resultado << endl;
	}

	void divisao(float a, float b) {
		float resultado = a / b;
		cout << ("Resultado: ") << resultado << endl;
	}
};

class op_trigonometrica {
public:

	float seno(float co, float hp) {
		float sen = co / hp;
		cout << ("Resultado seno: ") << sen << endl;
		return sen;
	}

	float coseno(float ca, float hp) {
		float cos = ca / hp;
		cout << ("Resultado cosseno: ") << cos << endl;
		return cos;
	}

	float tangente(float co, float ca) {
		float tang = co / ca;
		cout << ("Resultado tangente: ") << tang << endl;
		return tang;
	}
};

class op_complextrig : op_trigonometrica {
public:
	float cotangente(float co, float ca, float hp) {
		float cotg = seno(co, hp) / coseno(ca, hp);
		cout << ("Resultado cotangente: ") << cotg << endl;
		return cotg;
	}

	float secante(float ca, float hp) {
		float sec = 1 / coseno(ca, hp);
		cout << ("Resultado secante: ") << sec << endl;
		return sec;
	}

	float cossecante(float co, float hp) {
		float cossec = 1 / seno(co, hp);
		cout << ("Resultado cossecante: ") << cossec << endl;
		return cossec;
	}

};

int opcao,operacao, handshake = 0;
float a, b, c;

int main()
{
	cout << ("Calculadora basica e trigonometrica") << endl;
	while (handshake == 0) {
		cout << ("___________________________________________________________________________________________________________________") << endl;
		cout << ("Selecione o tipo de operacao desejada: ") << ("[1] Basica | [2] Trigonometrica | [3] Trigonometrica avancada") << endl;
		cout << ("Opcao: ");
		cin >> opcao;

		if (opcao == 1) {

			handshake = 1;
			op_basica basica;

			cout << ("Escolha a operacao: ") << ("[1] Soma | [2] Subtracao | [3] Multiplicao | [4] Divisao ") << endl;
			cout << ("Operacao: ");
			cin >> operacao;
			if (operacao != 1 && operacao != 2 && operacao != 3 && operacao != 4) {
				cout << ("Selecione uma operacao valida!") << endl;
			}
			else {
				cout << ("Informe o primeiro numero: ");
				cin >> a;
				cout << ("Informe o segundo numero: ");
				cin >> b;

				if (operacao == 1) {
					basica.soma(a, b);
				}
				else if (operacao == 2) {
					basica.subtracao(a, b);
				}
				else if (operacao == 3) {
					basica.multiplicacao(a, b);
				}
				else if (operacao == 4) {
					basica.divisao(a, b);
				}
				else {
					cout << ("Selecione uma operacao valida") << endl;
				}
			}
		handshake = 0;
		}

		else if (opcao == 2) {

			handshake = 1;
			op_trigonometrica trigo_b;

			cout << ("Escolha a operacao: ") << ("[1] Seno | [2] Cosseno | [3] Tangente") << endl;
			cout << ("Operacao: ");
			cin >> operacao;
			if (operacao != 1 && operacao != 2 && operacao != 3) {
				cout << ("Selecione uma operacao valida!") << endl;
			}
			else {
				cout << ("Informe o primeiro numero: ");
				cin >> a;
				cout << ("Informe o segundo numero: ");
				cin >> b;

				if (operacao == 1) {
					trigo_b.seno(a, b);
				}
				else if (operacao == 2) {
					trigo_b.coseno(a, b);
				}
				else if (operacao == 3) {
					trigo_b.tangente(a, b);
				}
				else {
					cout << ("Selecione uma operacao valida") << endl;
				}
			}
		handshake = 0;
		}

		else if (opcao == 3) {

			handshake = 1;
			op_complextrig trigo_c;

			cout << ("Escolha a operacao: ") << ("[1] Cotangente | [2] Secante | [3] Cossecante") << endl;
			cout << ("Operacao: ");
			cin >> operacao;
			if (operacao != 1 && operacao != 2 && operacao != 3) {
				cout << ("Selecione uma operacao valida!") << endl;
			}
			else {
				cout << ("Informe o primeiro numero: ");
				cin >> a;
				cout << ("Informe o segundo numero: ");
				cin >> b;

				if (operacao == 1) {
					cout << ("Informe a hipotenusa: ");
					cin >> c;
					trigo_c.cotangente(a, b, c);
				}
				else if (operacao == 2) {
					trigo_c.secante(a, b);
				}
				else if (operacao == 3) {
					trigo_c.cossecante(a, b);
				}
				else {
					cout << ("Selecione uma operacao valida! ") << endl;
				}
			}
		handshake = 0;
		}
		else {
			("Erro... Escolha uma opcao de 1 a 3!");
		}
	}
	return 0;
}

