from sys import stdin
#ejercico, hacer esto pero con los mecanismo que me permtite el obbjeto de stdin
# en stdin podemos usar la funcion read, pero ahora usaremos el buffer que utiliza
# la libreria por defecto

# Buffer: funcion que realiza la lectura de bytes hasta el límite que se le ponga,
# si no se le agrega, leera todo el archivo ingresado

#lee todos el archivo
INPUT, I = stdin.buffer.read(),0	
SPACE, CR, LPAR, RPAR, ZERO, NINE = ord(' '), ord('\n'), ord('('), ord(')'), ord('0'), ord('9')
#print(INPUT)
#for b in INPUT: print(b,end = ' ')

def has_next(): return I<len(INPUT)

def is_digit(): return ZERO <= INPUT[I] <= NINE
# 0 <= INPUT[I] - ord('0') <= 9

def read_blanks():
	global INPUT, I
	while has_next() and (INPUT[I] == CR or INPUT[I] == SPACE): I+=1

def read_par():
	global INPUT, I
	ans, I = chr(INPUT[I]), I+1
	return ans

"""
para leer 123 se lee de la siguiente manera:
1. 1
punto (1)*10 + 2
2. 12
punto (1)*100 + 3 o punto (2)*10 + 3
3. 123
"""

def read_num():
	global INPUT, I
	ans = 0
	while has_next() and is_digit():
		ans, I = int(chr(INPUT[I])) + ans*10, I+1
		#ans, I = (INPUT[I]-ord('0'))+ ans*10, I+1
	return ans
	
# si retorna None significa que ya agotó la entrada
def next_token():
	global INPUT, I
	ans = None
	read_blanks()
	if I!=len(INPUT):
		if is_digit(): ans = read_num()
		else: ans = read_par() 
	return ans

tkn = next_token()
while tkn!=None:
	print(tkn)
	tkn = next_token()