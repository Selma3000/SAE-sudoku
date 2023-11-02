
import copy
import time

#TROIS PETITES FONCTIONS DE TEST UTILISEES PLUS BAS#
def test(mess,eval,res):
    print(mess,(eval==res)*'OK'+(eval!=res)*'Try again')
def test_determine_valuations(mess,list_var,res):
    test=mess+'Ok'
    list_testee=determine_valuations(list_var)
    for el in list_testee :
        if el not in res:
            test=mess+'Try again'
            return test
    for el in res:
        if el not in list_testee :
            test=mess+'Try again'
            return test
    for i in range(len(list_testee)-1):
        if list_testee[i] in list_testee[i+1:]:
            test=mess+'wowowow y a du doublon là-difans'
            return test
    return test  

def test_for(mess,formu,res_for):
    res=True
    if (formu==[] and res_for!=[]) or (formu!=[] and res_for==[]):
        res=False
    for el1 in formu:
        for el2 in res_for:
            res=(set(el1)==set(el2))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    for el2 in res_for:
        for el1 in formu:
            res=(set(el2)==set(el1))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    res=False
    for i in range(len(formu)-1):
        for el in formu[i+1:]:
            if set(formu[i])==set(el):
                print(mess+'wowowow y a du doublon là-difans')
                return 
    print(mess+'Ok')
    
#A VOUS DE JOUER#
def evaluer_clause(clause, list_var):
    #on parcourt les clauses 
    for i in range(len(clause)):
        #si un des valeurs de la clause est positif 
        if clause[i]>0:
            #et si sa valeut dans listvar est aussi positif 
            if list_var[abs(clause[i])-1]== True:
                #on retourne vrai 
                return True
        #si une des valeurs est negatif     
        if clause[i]<0:
            #et si sa position dans listvar et sa polarité est fausse 
            #on prend valeur abs car sinon on sera out of range a cause du -1
            #qui nous permet d'accèder a la position exacte 
            if list_var[abs(clause[i])-1]== False:
                #on retourne vrai 
                return True 
    #on parcourt la clause pour le cas du none         
    for i in range(len(clause)):
        #si la valeur est None on retourne None 
        if list_var[abs(clause[i])-1] is None:
                return None
    #si on ne rencontre pas ce cas alors on retourne false 
    return False

    """  
    result = False
    unknow = False

    if len(clause)<1 :
        return result
    
    for i in clause:
        var = get(abs(i), list_var) # séléction la variable correspondant à la clause (absolue)
        if var == None :            # si var inconue (None) -> pas calculable -> pass
            unknow = True           # True si présance d'une var inconue
        else :
            if i<0 : var = not(var) # si clause negative -> inverse la valeur
        
            result = result or var  # calcul de la clause
        
        if result : return result   # si un résultat True alors clause True
    
    if not(result) and unknow :     # si resultat False et présance d'une var inconue donc potentielement True alors result = None
        result = None
        return result

    return result
    """
    '''Arguments : une liste d'entiers non nuls traduisant une clause,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
'''
    
clause1=[1,-2,3,-4]
list_var1=[True,True,False,None]
test("essai cas 1 evaluer_clause : ",evaluer_clause(clause1,list_var1),True)
clause2=[1,-2,3,-4]
list_var2=[False,True,False,None]
test("essai cas 2 evaluer_clause : ",evaluer_clause(clause2,list_var2),None)
clause3=[1,-2,3,-4]
list_var3=[None,True,False,True]
test("essai cas 3 evaluer_clause : ",evaluer_clause(clause3,list_var3),None)
clause4=[1,-3]
list_var4=[False,False,True]
test("essai cas 4 evaluer_clause : ",evaluer_clause(clause4,list_var4),False)
clause5=[]
list_var5=[False,False,True]
test("essai cas 5 evaluer_clause : ",evaluer_clause(clause5,list_var5),False)
clause6=[1,2,3]
list_var6=[False,False,True]
test("essai cas 6 evaluer_clause : ",evaluer_clause(clause6,list_var6),True)
clause7=[1,2,3,-4]
list_var7=[False,False,True,None]
test("essai cas 7 evaluer_clause : ",evaluer_clause(clause7,list_var7),True)
clause8 = [1, 2, 3]
list_var8 = [None, None, None]
test("essai cas 8 evaluer_clause : ", evaluer_clause(clause8, list_var8), None)
clause9 = [-1, -2, -3]
list_var9 = [False, False, False]
test("essai cas 9 evaluer_clause : ", evaluer_clause(clause9, list_var9), True)

clause10 = [1, 2, 3]
list_var10 = [True, True, True]
test("essai cas 10 evaluer_clause : ", evaluer_clause(clause10, list_var10), True)
clause11 = [-1, 2, -3, 4]
list_var11 = [False, True, False, True]
test("essai cas 11 evaluer_clause : ", evaluer_clause(clause11, list_var11), True)
clause12 = [1, -2, 3, -4]
list_var12 = [True, False, True, False]
test("essai cas 12 evaluer_clause : ", evaluer_clause(clause12, list_var12), True)

clause13 = [1,2,3]
list_var13 = [True,False,False]
test("essai cas 13 evaluer_clause : ", evaluer_clause(clause13, list_var13), True)

clause14 = [1,2,3,4]
list_var14 = [False,False,None,True]
test("essai cas 14 evaluer_clause : ", evaluer_clause(clause14, list_var14), True)

clause17 = [1, 2, 3, -4]
list_var17 = [True, None, None, None]
test("essai cas 17 evaluer_clause : ", evaluer_clause(clause17, list_var17), True)

clause15=[1,-2,3,-4]
list_var15=[None,None,None,None]
test("essai cas 15 evaluer_clause : ",evaluer_clause(clause15,list_var15),None)

clause16 = [-1,-2,-3]
list_var16 = [None,None,None]
test("essai cas 13 evaluer_clause : ", evaluer_clause(clause16, list_var16), None)

clause18 = [1, -2, -3, -4]
list_var18 = [None, None, None, False]
test("essai cas 18 evaluer_clause : ", evaluer_clause(clause18, list_var18), True)
clause19 = [-1, 2, -3, 4]
list_var19 = [None, None, None, None]
test("essai cas 19 evaluer_clause : ", evaluer_clause(clause19, list_var19), None)



def evaluer_cnf(formule,list_var):
    for i in range(len(formule)):
        if evaluer_clause(formule[i], list_var) == False:
            return False
        elif evaluer_clause(formule[i], list_var) is None:
            return None
    return True
'''Arguments : une liste de listes d'entiers 
    non nuls traduisant une formule,une liste de booléens informant
      de valeurs logiques connues (ou None dans le cas contraire) 
      pour un ensemble de variables
    Renvoie : None ou booléen
'''

for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var_for1_test1=[True,False,False,None]
test('test1 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test1),True)
list_var_for1_test2=[None,False,False,None]
test('test2 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test2),None)
list_var_for1_test3=[True,False,True,False]
test('test3 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test3),False)
list_var_for1_test3=[None,None,None,None]
test('test3 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test3),None)
list_var_for1_test3=[True,None,None,None]
test('test3 evaluer_cnf : ',evaluer_cnf(for1,list_var_for1_test3),None)

formule_test_1 = [[1, 2, -3], [3, -4], [4, 5], [2, 6]]
list_var_test_1 = [True, True, None, None, None, False]
test('Test 9 evaluer_cnf : ', evaluer_cnf(formule_test_1, list_var_test_1), None)


formule_test_2 = [[1, -2, 3], [4, 5], [-1, -5, -6], [3, -4]]
list_var_test_2 = [None, None, None, True, False, False]
test('Test 10 evaluer_cnf : ', evaluer_cnf(formule_test_2, list_var_test_2), None)

formule_test_3 = [[-1, 2, -3], [3, -4], [4, 5], [2, 6]]
list_var_test_3 = [False, True, True, None, None, None]
test('Test 11 evaluer_cnf : ', evaluer_cnf(formule_test_3, list_var_test_3), None)

formule_test_4 = [[1, -2, 3], [4, 5], [-1, -5, -6], [3, -4]]
list_var_test_4 = [None, None, None, True, True, False]
test('Test 12 evaluer_cnf : ', evaluer_cnf(formule_test_4, list_var_test_4), None)

def determine_valuations(list_var):
    if len(list_var)==0:
        return [list_var]
    list_val = [list_var]
    while None in list_val[0]:
        nvl_list = []
        for sublist in list_val:
            index = sublist.index(None)
            vraival = sublist[:index]+ [True]+sublist[index+1:]
            fauxval = sublist[:index]+ [False]+ sublist[index+1:]
            nvl_list.append(vraival)
            nvl_list.append(fauxval)
        list_val = nvl_list
    list_var = list_val
    return list_var
'''Arguments : une liste de booléens informant de valeurs logiques connues
      (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var
'''

list_var1=[True,None,False,None]
print(test_determine_valuations('res_test_determine_valuations cas 1 : ',list_var1,[[True, True, False, True], [True, False, False, True], [True, True, False, False], [True, False, False, False]]))
list_var2=[None,False,True,None,True,False]
print(test_determine_valuations('res_test_determine_valuations cas 2 : ',list_var2,[[True, False, True, True, True, False], [False, False, True, True, True, False], [True, False, True, False, True, False], [False, False, True, False, True, False]]))
list_var3=[False,True,True,False]
print(test_determine_valuations('res_test_determine_valuations cas 3 : ',list_var3,[[False, True, True, False]]))
list_var4=[None,None,None]
print(test_determine_valuations('res_test_determine_valuations cas 4 : ',list_var4,[[True, True, True], [False, True, True], [True, False, True], [False, False, True], [True, True, False], [False, True, False], [True, False, False], [False, False, False]]))

list_var5 = [True, False, True, None]

print(test_determine_valuations("Res_test_determine_valuations cas 1 : ", list_var5,[
    [True, False, True, True],
    [True, False, True, False]
]))
list_var6 = [None, None]

print(test_determine_valuations('res_test_determine_valuations cas 4 : ',list_var6,[[True, True], [True, False], [False, True], [False, False]]))



list_var8 = [None, None, None, None, None]
print(test_determine_valuations('res_test_determine_valuations cas 2 : ',list_var8 ,[
    [True, True, True, True, True],
    [True, True, True, True, False],
    [True, True, True, False, True],
    [True, True, True, False, False],
    [True, True, False, True, True],
    [True, True, False, True, False],
    [True, True, False, False, True],
    [True, True, False, False, False],
    [True, False, True, True, True],
    [True, False, True, True, False],
    [True, False, True, False, True],
    [True, False, True, False, False],
    [True, False, False, True, True],
    [True, False, False, True, False],
    [True, False, False, False, True],
    [True, False, False, False, False],
    [False, True, True, True, True],
    [False, True, True, True, False],
    [False, True, True, False, True],
    [False, True, True, False, False],
    [False, True, False, True, True],
    [False, True, False, True, False],
    [False, True, False, False, True],
    [False, True, False, False, False],
    [False, False, True, True, True],
    [False, False, True, True, False],
    [False, False, True, False, True],
    [False, False, True, False, False],
    [False, False, False, True, True],
    [False, False, False, True, False],
    [False, False, False, False, True],
    [False, False, False, False, False]
]  ))



'''def generate_valuations(variables):
    valuations = []
    num_variables = len(variables)

    def backtrack(index, current_valuation):
        if index == num_variables:
            valuations.append(list(current_valuation))
            return

        for value in (True, False, None):
            current_valuation[index] = value
            backtrack(index + 1, current_valuation)

    initial_valuation = [None] * num_variables
    backtrack(0, initial_valuation)

    return valuations

# Exemple d'utilisation
list_var1 = [True, None, False, None]
valuations1 = generate_valuations(list_var1)
print("Res_test_determine_valuations cas 1 : ", valuations1)

list_var2 = [None, False, True, None, True, False]
valuations2 = generate_valuations(list_var2)
print("Res_test_determine_valuations cas 2 : ", valuations2)

list_var3 = [False, True, True, False]
valuations3 = generate_valuations(list_var3)
print("Res_test_determine_valuations cas 3 : ", valuations3)

list_var4 = [None, None, None]
valuations4 = generate_valuations(list_var4)
print("Res_test_determine_valuations cas 4 : ", valuations4)
'''
def progress(list_var,list_chgmts):
    for i, valeur in enumerate(list_var):
        if valeur is None:
            list_var[i]= True
            list_chgmts.append([i, True])
            l1 = list_var
            l2 = list_chgmts
            return l1, l2
    l1 = list_var
    l2 = list_chgmts
    return l1, l2      
'''Arguments : list_var, list_chgmts définies comme précédemment
    Renvoie : l1,l2
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''

list_var=[True, None, None, None, None]
list_chgmts=[[0, True]]
l1=[True, True, None, None, None]
l2=[[0, True], [1, True]]
test("essai cas 1 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, False, None, None]
list_chgmts=[[0, True], [1, False], [2, False]]
l1=[True, False, False, True, None]
l2=[[0, True], [1, False], [2, False], [3, True]]
test("essai cas 2 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[None, None, None, None, None]
list_chgmts=[]
l1=[True, None, None, None, None]
l2=[[0, True]]
test("essai cas 3 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[False, None, None, None, None]
list_chgmts=[[0, False]]
l1=[False, True, None, None, None]
l2=[[0, False], [1, True]]
test("essai cas 4 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, None, None, None]
list_chgmts=[]
l1=[True, False, True, None, None]
l2=[[2, True]]
test("essai cas 5 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var=[True, False, False, None, None]
list_chgmts=[[2, False]]
l1=[True, False, False, True, None]
l2=[[2, False], [3, True]]
test("essai cas 6 progress : ",progress(list_var,list_chgmts),(l1,l2))

list_var7 = [None, None, None]
list_chgmts7 = []
l1_expectif7 = [True, None, None]
l2_expectif7 = [[0, True]]
test("Essai cas 7 progress : ", progress(list_var7, list_chgmts7), (l1_expectif7, l2_expectif7))

list_var8 = [False, None, None]
list_chgmts8 = [[0, False]]
l1_expectif8 = [False, True, None]
l2_expectif8 = [[0, False], [1, True]]
test("Essai cas 8 progress : ", progress(list_var8, list_chgmts8), (l1_expectif8, l2_expectif8))

list_var9 = [True, False, None]
list_chgmts9 = []
l1_expectif9 = [True, False, True]
l2_expectif9 = [[2, True]]
test("Essai cas 9 progress : ", progress(list_var9, list_chgmts9), (l1_expectif9, l2_expectif9))
list_var10 = [True, False, False, None]
list_chgmts10 = [[2, False]]
l1_expectif10 = [True, False, False, True]
l2_expectif10 = [[2, False], [3, True]]
test("Essai cas 10 progress : ", progress(list_var10, list_chgmts10), (l1_expectif10, l2_expectif10))
list_var11 = [None, None, None, None]
list_chgmts11 = []
l1_expectif11 = [True, None, None, None]
l2_expectif11 = [[0, True]]
test("Essai cas 11 progress : ", progress(list_var11, list_chgmts11), (l1_expectif11, l2_expectif11))


def retour(list_var,list_chgmts):

    if len(list_chgmts)==0 :
        l1 = list_var
        l2 = list_chgmts
        return l1,l2
    while list_chgmts :
        
        position, valeur= list_chgmts.pop()
        if list_var[position]== False:
            list_var[position]= None
        elif list_var[position] == True:
            list_var[position] = False
        if position<len(list_var) and list_var[position]== True or list_var[position]== False:
            list_var[position]= False
            list_chgmts.append([position, list_var[position]])
            l1= list_var
            l2=list_chgmts
            return l1,l2
    l1 = list_var
    l2 = list_chgmts  
    return l1, l2
    '''
    renvoie :l1,l2 avec :
    l1 : la liste actualisée des valeurs attribuées aux variables 
    l2 : la liste actualisée de l'ensemble des changements effectués depuis une formule initiale
    
    '''
list_var= [True, True, None, None, None]
list_chgmts= [[0, True], [1, True]]
l1= [True, False, None, None, None]
l2= [[0, True], [1, False]]
test("essai cas 1 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, None, None, None]
list_chgmts= [[0, True], [1, False]]
l1= [False, None, None, None, None]
l2= [[0, False]]
test("essai cas 2 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= []
l1= [True, False, False, True, None]
l2= []
test("essai cas 3 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, False, False]
list_chgmts= [[0, True], [1, False], [2, False], [3, False], [4, False]]
l1= [False, None, None, None, None]
l2= [[0, False]]
test("essai cas 4 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, True, False, True, None]
list_chgmts= [[1, True]]
l1= [True, False, False, True, None]
l2= [[1, False]]
test("essai cas 5 retour : ",retour(list_var,list_chgmts),(l1,l2))

list_var= [True, False, False, True, None]
list_chgmts= [[1, False]]
l1= [True, None, False, True, None]
l2= []
test("essai cas 6 retour : ",retour(list_var,list_chgmts),(l1,l2))
list_var13 = [None, None, None]
list_chgmts13 = []
l1_expectif13 = [None, None, None]
l2_expectif13 = []
test("Essai cas 7 retour : ", retour(list_var13, list_chgmts13), (l1_expectif13, l2_expectif13))
list_var14 = [False, None, None]
list_chgmts14 = [[0, False]]
l1_expectif14 = [None, None, None]
l2_expectif14 = []
test("Essai cas 8 retour : ", retour(list_var14, list_chgmts14), (l1_expectif14, l2_expectif14))

list_var15 = [True, False, None]
list_chgmts15 = []
l1_expectif15 = [True, False, None]
l2_expectif15 = []
test("Essai cas 9 retour : ", retour(list_var15, list_chgmts15), (l1_expectif15, l2_expectif15))


list_var16 = [True, False, False, None]
list_chgmts16 = []
l1_expectif16 = [True, False, False, None]
l2_expectif16 = []
test("Essai cas 10 retour : ", retour(list_var16, list_chgmts16), (l1_expectif16, l2_expectif16))

list_var19 = [True, False, False, None, None]
list_chgmts19 = [[0, True], [1, False], [2, False]]
l1_expectif19 = [False, None, None, None, None]
l2_expectif19 = [[0, False]]
test("Essai cas 19 retour : ", retour(list_var19, list_chgmts19), (l1_expectif19, l2_expectif19))

# list_var20 = [None, None, None, None, None]
# list_chgmts20 = [[0, True], [1, False], [2, True], [3, False], [4, True]]
# l1_expectif20 = [None, None, None, None, None]
# l2_expectif20 = [[0, True], [1, False], [2, True], [3, False], [4, True]]
# test("Essai cas 20 retour : ", retour(list_var20, list_chgmts20), (l1_expectif20, l2_expectif20))






def enlever_litt_for(formule,litteral):
    i= len(formule)-1
    while i>=0:
        clause= formule[i]
        if litteral>0:
            if litteral in clause:

                formule.pop(i)
            elif -litteral in clause:
                clause.remove(-litteral)
        if litteral<0:
            if litteral in clause:

                formule.pop(i)

            elif -litteral in clause:
                clause.remove(-litteral)
        i-=1
    return formule
'''
   formule_simplifiee = []
    for clause in formule:
        if litteral in clause:
            continue
        if -litteral in clause:
            clause.remove(-litteral)
        formule_simplifiee.append(clause)
    return formule_simplifiee
'''
'''Arguments :
formule : comme précédemment
litteral : un entier non nul traduisant la valeur logique prise par une variable
    Renvoie : la formule simplifiée
'''

for1=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt1=4
test('essai cas 1 enlever_litt_for : ',enlever_litt_for(for1,litt1),[[-1, 2, 3], [-1, -2, -5], []])

for2=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt2=5
test('essai cas 2 enlever_litt_for : ',enlever_litt_for(for2,litt2),[[1,2,4],[-1,2,3,-4],[-1,-2],[-4]])

for3=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt3=-5
test('essai cas 3 enlever_litt_for : ',enlever_litt_for(for3,litt3),[[-1,2,3,-4],[-3,4],[-2,3,4],[-4]])

for6 = [[1, 2, 3], [1, -2, -3], [1, 2, 3, 4], [4, 5]]
litt6 = 1
test('Essai cas 6 enlever_litt_for : ', enlever_litt_for(for6, litt6), [[4, 5]])

for7 = [[1, 2, 3], [-1, -2, -3], [1, 2, -3], [-1, -2, 3]]
litt7 = 4
test('Essai cas 7 enlever_litt_for : ', enlever_litt_for(for7, litt7), [[1, 2, 3], [-1, -2, -3], [1, 2, -3], [-1, -2, 3]])

for8 = []
litt8 = 5
test('Essai cas 8 enlever_litt_for : ', enlever_litt_for(for8, litt8), [])

for5 = [[1, 2, 3], [-1, -2, -3], [1, 2, -3], [-1, -2, 3]]
litt5 = 3
test('Essai cas 5 enlever_litt_for : ', enlever_litt_for(for5, litt5), [ [-1, -2],[1, 2]])



def init_formule_simpl_for(formule_init,list_var):
    formule_simplifiee = []

    for clause in formule_init:
        clause_simplifiee = []

        for litteral in clause:
            is_negatif = False
            if litteral < 0:
                litteral = -litteral
                is_negatif = True

            if litteral in list_var:
                index = list_var.index(litteral)
                if list_var[index] is not None:
                    if (list_var[index] and not is_negatif) or (not list_var[index] and is_negatif):
                        # Le littéral est évalué à True, donc la clause est satisfaite.
                        break
                else:
                    clause_simplifiee.append(litteral)
            else:
                clause_simplifiee.append(litteral)

        if not any([(litteral in list_var) and (list_var[list_var.index(litteral)] is None) for litteral in clause]):
            # La clause est entièrement évaluée, on ne la conserve pas.
            continue

        formule_simplifiee.append(clause_simplifiee)

    return formule_simplifiee

    return 
    '''
    Renvoie : La formule simplifiée en tenant compte des valeurs logiques renseignées dans list_var
'''

"""
list_var_for1=[False, None, None, False, None]
for1=[[-5, -3, 4, -1], [3], [5, -2], [-2, 1, -4], [1, -3]]
cor_for1=[[3], [5, -2], [-3]]
test_for('test1_init_formule_simpl_for : ',init_formule_simpl_for(for1,list_var_for1),cor_for1)

list_var_for2= [False, True, False, True, False]
for2= [[3, 2, 1], [-1, -2, 5]]
cor_for2=[]
test_for('test2_init_formule_simpl_for : ',init_formule_simpl_for(for2,list_var_for2),cor_for2)

list_var_for3= [None, None, None, True, None]
for3= [[-5, -1], [-1, -3], [4], [-4, 1], [-2, -1, 3]]
cor_for3=[[-5, -1], [-1, -3], [1], [-2, -1, 3]]
test_for('test3_init_formule_simpl_for : ',init_formule_simpl_for(for3,list_var_for3),cor_for3)
"""


def retablir_for(formule_init,list_chgmts):
    
    
    '''Arguments : une formule initiale et une liste de changements à apporter sur un
    ensemble de variables (chaque changement étant une liste [i,bool] avec i l'index qu'occupe
    la variable dans list_var et bool la valeur logique qui doit lui être assignée) 
    Renvoie : la formule simplifiée en tenant compte de l'ensemble des changements
'''
    
'''
formule_init=[[1, 2, 4, -5], [-1, 2, 3, -4], [-1, -2, -5], [-3, 4, 5], [-2, 3, 4, 5], [-4, 5]]
list_chgmts1=[[0, True], [1, True], [2, False]]
form1=[[-5], [4, 5], [-4, 5]]

list_chgmts2=[[0, True], [1, True], [2, False], [3, True], [4, False]]
form2=[[]]

list_chgmts3=[[0, True], [1, True], [2, False], [3, False]]
form3=[[-5], [5]]
test('essai cas 1 retablir_for : ',retablir_for(formule_init,list_chgmts1),form1)
test('essai cas 2 retablir_for : ',retablir_for(formule_init,list_chgmts2),form2)
test('essai cas 3 retablir_for : ',retablir_for(formule_init,list_chgmts3),form3)

'''

def resol_parcours_arbre(formule_init,list_var,list_chgmts):
    if not formule_init:
        # Si la formule est vide, elle est automatiquement satisfaite.
        return (True, list_var)

    if not list_var:
        # Si la liste des variables est vide, la formule ne peut pas être satisfaite.
        return (False, [])

    if None not in list_var:
        # Si toutes les variables sont assignées, évaluez la formule.
        satisfiable = evaluer_cnf(formule_init, list_var)
        return (satisfiable, list_var)

    # Chercher la prochaine variable non affectée.
    index = list_var.index(None)

    # Essayez de progresser en affectant la variable à True.
    var_true = list_var.copy()

    var_true[index] = True

    new_var_true, new_chgmts_true = progress(var_true, list_chgmts)

    result_true = resol_parcours_arbre(formule_init, new_var_true, new_chgmts_true)

    if result_true[0]== True:
        # Si la progression avec True est satisfaisante, renvoyez le résultat.
        return resol_parcours_arbre(formule_init,new_var_true,new_chgmts_true)
    # Sinon, essayez de progresser en affectant la variable à False.
    var_false = list_var.copy()
    
    var_false[index] = False
  
    new_var_false, new_chgmts_false = progress(var_false, list_chgmts)

    result_false = resol_parcours_arbre(formule_init, new_var_false, new_chgmts_false)

    if result_false[0]:
        # Si la progression avec False est satisfaisante, renvoyez le résultat.
        return result_false

    # Si aucune des progressions n'est satisfaisante, retournez False.
    return (False, [])

    '''Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide'''
    
    

formule_init= [[1, 4, -5], [-1, -5], [2, -3, 5], [2, -4], [2, 4, 5], [-1, -2], [-1, 2, -3], [-2, 4, -5], [1, -2]] 
list_var= [True, True, False, True, None] 
list_chgmts= [[1, True]]
cor_resol=(False, [])
test('essai1_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[5], [3, -5, -1, -2], [1, -2, -5], [2, -5, 1, -3], [3]] 
list_var= [True, False, None, False, True] 
list_chgmts= [[0, True]]
cor_resol=(True,[True, False, True, False, True])
test('essai2_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True,[False, True, False, True, False])
test('essai3_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [] 
list_var= [False, True, False, None, None] 
list_chgmts= [[1, True]]
cor_resol=(True, [False, True, False, None, None] )
test('essai4_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

formule_init= [[-5, 2, -3, -4], [1, -5], [5, 2], [3, -2, 4], [5, -2, -1]] 
list_var= [] 
list_chgmts= [[1, True]]
cor_resol=(False, [] )
test('essai4_resol_parcours_arbre : ',resol_parcours_arbre(formule_init,list_var,list_chgmts),cor_resol)

# Test pour le cas où toutes les variables sont assignées
formule_test_all_assigned = [[1, 2, 3], [-1, -2, 3], [2, -3, 4]]
list_var_test_all_assigned = [True, True, False, False]
list_chgmts_test_all_assigned = []
cor_resol_test_all_assigned = (False, [True, True, False, False])
test('Test pour le cas où toutes les variables sont assignées : ', resol_parcours_arbre(formule_test_all_assigned, list_var_test_all_assigned, list_chgmts_test_all_assigned), cor_resol_test_all_assigned)


"""
if formule_init == True: # si la formule est satisfiable
        return True, list_var # renvoyer True et la valuation solution
    elif formule_init == False: # si la formule est non satisfiable
        return False, [] # renvoyer False et une liste vide

    for variable, valeur in list_chgmts:
        # Modifier la valuation en cours pour la variable
        list_var[variable] = valeur

        # Appliquer la nouvelle valuation aux branches du parcours
        est_satisfiable, valuation_solution = resol_parcours_arbre(formule_init, list_var, list_chgmts)

        if est_satisfiable: # si la formule est satisfiable
            return True, valuation_solution # renvoyer True et la valuation solution
        else: # si la formule est non satisfiable
            # Rétablir la valuation précédente pour la variable
            list_var[variable] = not valeur

    return False, [] # si aucune branch n'est satisfiable, renvoyer False et une liste vide
"""