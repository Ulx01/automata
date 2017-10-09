class Automata:
    def automata(self,lexema,token):
        res = All()
        isIn = True
        if not lexema in " ":
            if lexema in res.L:
                token = res.tokens[lexema]
            else:
                if len(lexema) >= 1 and lexema[0] in ".":
                    for i in lexema:
                        if not i in res.U:
                            isIn = False
                            break
                    if isIn:
                        token = "%"
                else:
                    if len(lexema) >= 1 and lexema[0] in res.N:
                        token = "cant"
                    else:
                        isIn = False
            if not isIn:
                print "Error simbol "+lexema+" isn't in the language"
        return token, isIn


class ErrorManagement(object):
    def check_simbol(self, user_simbol, system_simbols):
        if(user_simbol in system_simbols):
            #print user_simbol+" Is in the lenguage"
            return True
        else:
            print "Syntax Error...simbol " +user_simbol+" isn't in the language"
            return False
        pass

class All(object):
    def __init__(self):
        #super(, self).__init__()
        #self.arg = arg
        self.L = ["PA","PR","LA","TA","SE","IN","PO","AS"]
        self.N = ["0","1","2","3","4","5","6","7","8","9"]
        self.M = ["."]
        self.U = list(set(self.L) | set(self.N) | set(self.M))
        #print self.U
        #self.table_simbols.append("pr")#load the simbols
        self.tokens = {"PA":"A","PR":"E","LA":"I","TA":"L","SE":"N","IN":"O","PO":"P","AS":"R","0":"S","1":"T"}

class TableSimbol(object):
    def __init__(self):
        self.tableSimbols = {}
