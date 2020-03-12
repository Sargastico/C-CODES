library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

ENTITY N_HOME IS
	PORT (endereco : IN UNSIGNED(3 downto 0);
	ce : IN std_logic;
	saida : OUT UNSIGNED(7 downto 0));
END N_HOME;

ARCHITECTURE test OF N_HOME IS
	TYPE arranjo_memoria IS ARRAY(NATURAL RANGE <>) OF UNSIGNED (7 downto 0);
	CONSTANT dados : arranjo_memoria(0 to 15) := 
	("00000001","00100011","00110100","11000101","00010011",
	"01000011","00101001","00111001","11111111","01101101",
	"01011101","01110001","01100101","01010011","10101010",
	"10111101");
	
BEGIN
	saida <= dados(to_integer(endereco)) WHEN ce='0' ELSE (OTHERS => 'Z');
END test;
