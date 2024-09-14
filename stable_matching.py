def stableMatching(n, menPreferences, womenPreferences):
# Do not change the function definition line.


   # Initially, all n men are unmarried
   unmarriedMen = list(range(n))
   # None of the men has a spouse yet, we denote this by the value None
   manSpouse = [None] * n                     
   # None of the women has a spouse yet, we denote this by the value None
   womanSpouse = [None] * n                     
   # Each man made 0 proposals, which means that
   # his next proposal will be to the woman number 0 in his list
   nextManChoice = [0] * n                      
  
   # While there exists at least one unmarried man:
   while unmarriedMen:
       # Pick an arbitrary unmarried man
       he = unmarriedMen[0]                     
       # Store his ranking in this variable for convenience
       hisPreferences = menPreferences[he]      
       # Find a woman to propose to
       she = hisPreferences[nextManChoice[he]]
       # Store her ranking in this variable for convenience
       herPreferences = womenPreferences[she]
       # Find the present husband of the selected woman (it might be None)
       currentHusband = womanSpouse[she]        
      
       # Write your code here
      
       # Now "he" proposes to "she".
       # Decide whether "she" accepts, and update the following fields
       # 1. manSpouse
       # 2. womanSpouse
       # 3. unmarriedMen
       # 4. nextManChoice
       if currentHusband is not None:
           if herPreferences[currentHusband] < herPreferences[he]:
               womanSpouse[she] = he
               manSpouse[he] = she
               unmarriedMen.pop(0)
               unmarriedMen.append(currentHusband)
       else:
            womanSpouse[she] = he
            manSpouse[he] = she
            unmarriedMen.pop(0)
           
       nextManChoice[he] += 1

   return manSpouse


# MenPreferences armazena a preferência de cada homen em uma lista, onde o índice da lista indica a preferência de cada homen
# ou seja, menPreferences[0][0] > menPreferences[0][1] > .... > menPreferences[0][n-1]. Isso para todos os homens
menPreferences = [
    [0,1,2],
    [2,1,0],
    [0,2,1]
]

# WomenPreferences armazena o valor da preferência que cada mulher tem por cada homen em seu respectivo índice
womenPreferences = [
    [1,0,2],
    [2,0,1],
    [0,2,1]
]

n = len(menPreferences)

# print(stableMatching(n, menPreferences, womenPreferences)) # Saida esperada = [1,2,0]