
def evaluer_clause(clause,list_var):
     
    clause_values = []  # Tableau pour stocker les valeurs booléennes des littéraux dans la clause
    
    for literal in clause:
        variable_index = abs(literal) - 1
        if literal > 0:
            if list_var[variable_index] is True:
                clause_values.append(True)
            else:
                clause_values.append(False)
        elif literal < 0:
            if list_var[variable_index] is False:
                has_true_literal = True
                clause_values.append(True)
            else:
                clause_values.append(False)
        else:
            clause_values.append(None)

    if has_true_literal:
        return True, clause_values
    elif not clause:
        return True, clause_values
    else:
        return None, clause_values
clause1=[1,-2,3,-4]
list_var1=[True,True,False,None]
clause7=[1,2,3,-4]
list_var7=[False,False,True,None]
print(evaluer_clause(clause7,list_var7))

def evaluer_cnf(formule,list_var):
    for i in range(len(formule)):
        if evaluer_clause(formule[i], list_var)== False :
            # print("evaluer_clause()",evaluer_clause(formule[i], list_var))
            return False
        elif evaluer_clause(formule[i], list_var) is None:
            return None
    return True

def determine_valuations(list_var):
    if None not in list_var:
        return [list_var]
    list_val = [list_var]
    while None in list_val[0]:
        nvl_valuation = []
        for sublist in list_val:
            index = sublist.index(None)
            
            newvaluations1 = sublist[:index]+ [True]+sublist[index+1:]
            newvaluation2= sublist[:index]+ [False]+ sublist[index+1:]
            # print(newvaluations1, sublist[:index], sublist[index+1:])
            nvl_valuation.append(newvaluations1)
            nvl_valuation.append(newvaluation2)
        list_val= nvl_valuation
    return list_val
#a refaire seule sans exemple
'''Arguments : une liste de booléens informant de valeurs logiques connues
      (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var
'''

# list_var1=[True,None , False, None]

# print(determine_valuations(list_var1))

# list_var2=[None,False,True,None,True,False]

# print("true none false none",determine_valuations(list_var2))
# list_var3=[False,True,True,False]




def progress(list_var,list_chgmts):
    for i, valeur in enumerate(list_var):
        # print(i, valeur)
        if  valeur is None:
            # print(valeur)
            list_var[i]= True
            # print(list_var[i])
            list_chgmts.append([i,True])
            # print(list_chgmts)
            return list_var,list_chgmts
    return list_var, list_chgmts


list_var=[True, None, None, None, None]
list_chgmts=[[0, True]]
# print(progress(list_var, list_chgmts))



def retour(list_var,list_chgmts):
    if len(list_chgmts)==0:
        return list_var, list_chgmts
    
    while list_var :
        position, _ = list_chgmts.pop()
        
        if list_var[position] == False:
            list_var[position]= None
            
        elif  list_var[position]== True:
            list_var[position]= False
            
        if position<len(list_var) and list_var[position]== True or list_var[position]== False:
            list_var[position]= False
            list_chgmts.append([position, False])
            return list_var, list_chgmts
    return list_var, list_chgmts
'''  if list_chgmts==0  :
    # Rien à annuler, renvoyer les valeurs actuelles
        return list_var, list_chgmts
    # Parcourir la liste des changements à l'envers pour trouver le dernier changement
    for i in range(len(list_chgmts)-1,-1,-1):
        print("iteration",i,"listchangement",list_chgmts)
        position, valeur = list_chgmts[i]
        print("posde",position,"valde",valeur)
        #annuler le dernier changements qui a été inscrit a la lindice position dans listchgmt
        if list_var[position]== False:
            # print(list_var[position])
            list_var[position]= None
            # print(list_var[position])
        elif list_var[position]==True:
            list_var[position]= False
        #supprimer le dernier chgmt de la list
        list_chgmts.pop()
        if position == True:
            if position<len(list_var) :
                list_var[position]= False
                list_chgmts.append([position, valeur])
                return list_var, list_chgmts
    return list_var, list_chgmts
'''
# list_var= [True, True, None, None, None]
# list_chgmts= [[0, True], [1, True]]
# print(retour(list_var,list_chgmts))

# list_var1= [True, True, False, True, None]
# list_chgmts1= [[1, True]]
# print(retour(list_var1,list_chgmts1))

list_var2= [True, False, None, None, None]
list_chgmts2= [[0, True], [1, False]]
# print(retour(list_var2,list_chgmts2))



def enlever_litt_for(formule,litteral):
    i =0
    while i <len(formule):
        clause = formule[i]
        if litteral in clause:
            formule.pop(i)
        elif -litteral in clause:
            clause.remove(-litteral)
            i+=1
        #Si ni le littéral ni son opposé ne sont présents dans la clause,  
        #la boucle passe simplement à la clause suivante en incrémentant i
        else:
            i+=1
    return formule     
    
    """
    2eme solution qui parcourt la liste a lenvers 
    i = len(formule) - 1
    while i >= 0:
        clause = formule[i]
    
        # Vérifiez si le littéral ou son opposé apparaît dans la clause.
        if litteral in clause:
            # Si le littéral est présent, supprimez toute la clause car elle est satisfaite.
            formule.pop(i)
        elif -litteral in clause:
            # Si l'opposé du littéral est présent, supprimez l'opposé du littéral de la clause.
            clause.remove(-litteral)
        i -= 1        
    return formule  
    3eme sol
       formule_simplifiee = []
    for clause in formule:
        if litteral in clause:
            continue
        if -litteral in clause:
            clause.remove(-litteral)
        formule_simplifiee.append(clause)
    return formule_simplifiee 
    """
for1=[[1,2,4,-5],[-1,2,3,-4],[-1,-2,-5],[-3,4,5],[-2,3,4,5],[-4]]
litt1=4
# print(enlever_litt_for(for1, litt1))
#[[-1, 2, 3], [-1, -2, -5], []]

def init_formule_simpl_for(formule_init,list_var):
    formule_simplifiee = []

    for clause in formule_init:
        clause_satisfait = False

        for litt in clause:
            # Vérifiez si le littéral ou son opposé est déjà affecté.
            if litt > 0:
                print("litt =",litt)
                if list_var[litt - 1] == True:
                    print("1er if",list_var[litt - 1])
                    clause_satisfait = True
                    
            elif litt < 0:
                if list_var[-litt - 1] == False:
                    clause_satisfait = True
            
            elif list_var[-litt - 1] is None:
                clause_satisfait = None
        # Si la clause n'est pas déjà satisfaite, ajoutez-la à la formule simplifiée.
        if not clause_satisfait:
            formule_simplifiee.append(clause)

    return formule_simplifiee
    '''
    Renvoie : La formule simplifiée en tenant compte des valeurs logiques renseignées dans list_var
'''


# list_var_for1=[False, None, None, False, None]
# for1=[[-5, -3, 4, -1], [3], [5, -2], [-2, 1, -4], [1, -3]]
# # cor_for1=[[3], [5, -2], [-3]]
# print(init_formule_simpl_for(for1, list_var_for1))

# list_var_for3= [None, None, None, True, None]
# for3= [[-5, -1], [-1, -3], [4], [-4, 1], [-2, -1, 3]]
# # cor_for3=[[-5, -1], [-1, -3], [1], [-2, -1, 3]]
# print(for3, list_var_for3)