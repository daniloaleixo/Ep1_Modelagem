import sys

#variaveis de tempo
t1 = 0
t2 = 0
t3 = 0

#variaveis globais 
aceleracao_media = 1.0
velocidade_media = 0
tempo_Total = 0
nSteps = 10
tipo = 0


# entra com os argumentos da funcao
if(len(sys.argv) < 4):
	print "modo de uso\n"
	print "ep1 <tempos de medicao>"
	print "Ex: $ ep1 tipo 4.5 5.6 7.8\n"
	print "Onde tipo e definido por:\n"
	print "  1 = Movimento Retilineo Uniforme\n"
	print "  2 = Movimento Uniormemente acelerado\n"
	exit(0)
else:
	tipo = sys.argv[1]
	t2 = float(sys.argv[2])
	t2 = float(sys.argv[3])
	t3 = float(sys.argv[4])


# calcula tempo total
tempo_Total = t1 + t2 + t3

#vamos calcular a aceleracao media
def calc_aceleracao():
	return 2 * 60.0/float((tempo_Total*tempo_Total))

# vamos calcular a velocidade media
def calc_velocidade():
	return 60.0 / tempo_Total


# calcula 	
aceleracao_media = calc_aceleracao()   
velocidade_media = calc_velocidade()

print aceleracao_media, velocidade_media, tempo_Total


# --------------------------------------------------------
#
#	Movimento Retilineo Uniforme
#
#

# Analitica
def posicaoMovimentoUniformeA(y0, v0, t):
	return y0 + v0*t

def velocidadeMovimentoUniformeA(v0, t):
	return v0

def movimentoUniformeAnalitico(y0, v0, tf, step):
	t = 0
	v = []
	y = []
	while (t<=tf):
		y.append(posicaoMovimentoUniformeA(y0,v0,t))
		v.append(velocidadeMovimentoUniformeA(v0,t))
		t += step
	return y,v

# Euler
def posicaoMovimentoUniformeE(y0, v0, dt):
	return y0 + v0*dt

def velocidadeMovimentoUniformeE(v0, dt):
	return v0

def movimentoUniformeEuler(y0, v0, tf, step):
	t = 0
	v = []
	y = []
	while (t<=tf):
		y.append(y0)
		v.append(v0)
		y0 = posicaoMovimentoUniformeE(y0, v0, step)
		v0 = velocidadeMovimentoUniformeE(v0, step) 
		t += step
	return y,v

# --------------------------------------------------------
#
#	Movimento Uniformemente Acelerado
#
#

# Analitica
def posicaoUnifAceleradoA(y0, v0, t):
	return y0 + v0*t + (aceleracao_media * t * t)/2.0

def velocidadeUnifAceleradoA(v0, t):
	return v0 + aceleracao_media * t 

def movimentoUnifAceleradoAnalitico(y0, v0, tf, step):
	t = 0
	v = []
	y = []
	while (t<=tf):
		y.append(posicaoUnifAceleradoA(y0,v0,t))
		v.append(velocidadeUnifAceleradoA(v0,t))
		t += step
	return y,v

# Euler
def posicaoUnifAceleradoE(y0, v0, dt):
	return y0 + v0*dt

def velocidadeUnifAceleradoE(v0, dt):
	return v0 + aceleracao_media * dt

def movimentoUnifAceleradoEuler(y0, v0, tf, step):
	t = 0
	v = []
	y = []
	while (t<=tf):
		y.append(y0)
		v.append(v0)
		y0 = posicaoUnifAceleradoE(y0, v0, step)
		v0 = velocidadeUnifAceleradoE(v0, step) 
		t += step
	return y,v


def printV(list1, list2,nome,step):
	print(nome)
	for i in range(0, len(list1)):
		print '%.3f' %list1[i], '%.3f' %list2[i]

# -----------------------------------------------------------
#
#
# 	MAIN
#
#
def main():

	step = tempo_Total / (nSteps - 1)

	nPrint = 10 # numero de amostras que serao impressas no output
	printStep = int(tempo_Total / (step * nPrint))

	if tipo == '1':
		y0 = 0
		v0 = velocidade_media
		tf = tempo_Total

		ya,va = movimentoUniformeAnalitico(y0, v0, tf, step)
		ye,ve = movimentoUniformeEuler(y0, v0, tf, step)

		printV(ya, ye,'ya | ye',printStep)
		printV(va , ve,'va | ve',printStep)
	elif tipo == '2':

		y0 = 0
		v0 = 0
		tf = tempo_Total	

		ya,va = movimentoUnifAceleradoAnalitico(y0, v0, tf, step)
		ye,ve = movimentoUnifAceleradoEuler(y0, v0, tf, step)

		printV(ya, ye,'ya | ye',printStep)
		printV(va , ve,'va | ve',printStep)


main()

