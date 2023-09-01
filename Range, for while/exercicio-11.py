numero = int( input('Você deseja a tabuada de qual número? '))
for c in range (1, 11):
    print ('{}x {:2}={}'.format(numero, c, numero*c))
