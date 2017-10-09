import json
from  resources import All#import the class All
from resources import ErrorManagement#importa la clase ErrorManagement del archivo resources
from resources import TableSimbol
from resources import Automata

res = All()#other is an instance of All
error = ErrorManagement()#manejador de errores
automata = Automata()
simbol = TableSimbol()#tabla de simbolos del usuario, aqui estaran los nuevos simbolos que el usuario ingrese
_file = open("files/file", "r")#abre el archivo
result = [] #resultado del automata
convert = "" #line convertida
token = []
spaceCount = 0#numero de esapcios
lineCount = 0
lexema = ""
for line in _file:#itera el archivo
    print line#imprime la linea que esta leyendo
    for i in line:#itera la linea
        if not i in " " and not i in "\n":
            lexema = lexema + i#toma el lexema
            spaceCount = 0
        else:
            token = automata.automata(lexema,token)
            if token[1] and not lexema in " ":
                if spaceCount < 1:#si la cantidad de espacios es menor que 1, agrega un |
                    print "lexema is: "+lexema+" token is: "+token[0]
                    convert += (str(token[0])+"|")
                spaceCount += 1#cuenta la cantidad de espacios para que no hayan | de mas
                simbol.tableSimbols[token[0]+str(lineCount)] = lexema #instalacion en la tabla de simbolos
            token = []
            #print lexema
            lexema = ""
    else:
        if not convert in " ":
            result.append(convert)
        print convert + "\n"
        convert = ""
        lineCount += 1
        lexema = ""
print "Tokens\n"
print result
print "\n"
_file.close
print "tabla de simbolos\n"
print simbol.tableSimbols
with open("files/simbols","w") as _simbolsFile:
    _simbolsFile.write(json.dumps(simbol.tableSimbols))
_simbolsFile.close
