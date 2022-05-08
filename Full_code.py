n = 8192
def is_prime(n) : 
    if n == 0 : 
        return False
    if n == 1 : 
        return False
    for i in range(int(n**(0.5)) + 1) : 
        if i in [0,1] : 
            pass
        else : 
            if n % i == 0 : 
                return False
    return True

def liste_primes(n) : 
    liste = [2] 
    for i in range(n+1) : 
        #print(i, liste)
        if i in [0,1,2] : 
            pass
        else : 
            prime = True
            for p in liste : 
                #print(p)
                if i % p == 0 : 
                    prime = False
                    break
            if prime : 
                liste.append(i)
    return liste

def find_puissance_2(n) : 
    primes = liste_primes(n)
    if (n-1) in primes : 
        print("Le complémentaire de 1 qui est", n-1, "est premier")
    paires_cc = []
    paires_pc = []
    paires_pp = []
    for i in range(int(n / 4) - 1) : 
        if (2*i+3) in primes : 
            if (n - 2 * i - 3) in primes : 
                paires_pp.append([2 * i + 3, n - 2 * i - 3])
            else : 
                paires_pc.append([2 * i + 3, n - 2 * i - 3])
        else : 
            if (n - 2 * i - 3) in primes : 
                paires_pc.append([2 * i + 3, n - 2 * i - 3])
            else : 
                paires_cc.append([2 * i + 3, n - 2 * i - 3])
    print("Composés-composés", len(paires_cc))
    print("Premiers-composés", len(paires_pc))
    print("Premiers-premiers", len(paires_pp))
    return [paires_cc, paires_pc, paires_pp]
def Goldbach(n) : 
    return find_puissance_2(n)[-1]
#n = 64

#a = find_puissance_2(n)

def trouver_restes(n) :
    #Cette fonction prend en argument une puissance de 2 (64, 128...) et va retourner
    #tous les nombres premiers impairs nécessaires à la recherche des nombres composés 
    #inférieurs à n. Ensuite, les restes seront les restes de 128 par chacun de 
    #ces nombres premiers. 
    #Par exemple, pour n = 128, les nombres premiers impairs nécessaires seront 
    #[3,5,7,11] et les restes seront [2,3,2,7]
    nb_premiers_a_tester = liste_primes(int(n**(0.5)))[1:]
    # print(nb_premiers_a_tester)
    restes = []
    for i in nb_premiers_a_tester :
        restes.append(n%i)
    # print(restes)
    return nb_premiers_a_tester, restes
    
premiers_impairs, restes = trouver_restes(n)

def trouver_multiples(n, premiers_impairs) :
    #Ici, on va créer la liste de tous les multiples de 3
    #Ensuite la liste de tous les multiples de 5 sans les multiples de 3 que l'on a déjà pris avant (on ne prend pas 15 par exemple)
    #On continue avec 7 et ainsi de suite avec tous les nombres premiers impairs jusqu'à sqrt(n).
    #Cette manière de créer ces listes nous permettra de trouver toutes les paires complémentaires à n formées de 2 nombres composés.
    
    deja_pris = []
    multiples = []
    for i, premier in enumerate(premiers_impairs) : 
        p_multiples = []
        for j in range(int(n/premier)+1) : 
            if (j not in [0,1]) and (premier * j not in deja_pris) and (j % 2 == 1) : 
                p_multiples.append(premier * j)
                deja_pris.append(premier * j)
        multiples.append(p_multiples)
    return multiples

multiples = trouver_multiples(n, premiers_impairs)
# print(multiples)

def trouver_paires_composees(multiples, premiers_impairs, restes,n) : 
    deja_utilises = []
    utilises = []
    for i, reste in enumerate(restes[:-1]) : 
        #premiers_impairs[i] sera le nombre premier associé à reste
        for k in range(len(restes) - i - 1) : 
            for j in multiples[i+1+k] : 
                if (j % premiers_impairs[i] == reste) and (n-j) not in premiers_impairs : 
                    if j not in utilises : 
                        deja_utilises.append([[j, n-j], premiers_impairs[i]])
                        utilises.append(j)
    return deja_utilises, len(deja_utilises)

utilises, total = trouver_paires_composees(multiples, premiers_impairs, restes,n)
                
def preuve_Goldbach(n) : 
    premiers_impairs, restes = trouver_restes(n)
    multiples = trouver_multiples(n, premiers_impairs)
    utilises, total = trouver_paires_composees(multiples, premiers_impairs, restes,n)
    n_divise_par_2 = int(n / 2) #On prend que les nombres impairs, ça correspond à 1 nombre sur 2
    premiers = len(liste_primes(n)) - 1 #On compte le nombre de nombres premiers
    composes = n_divise_par_2 - 1 - premiers #On compte le nombre de nombres composés
    reste_composes = composes - 2 * total #On enlève des nombres composés les paires composé-composé
    reste_premiers = premiers - reste_composes #On enlève des nombres premiers ceux qui sont complémentaires à un nombre composé
    
    print("Total", total)
    print("Premiers", premiers)
    print("Composés", composes)
    print("reste_premiers", reste_premiers)
    print("reste_composés", reste_composes)
    return reste_premiers - 1 #On regarde combien de nombres premiers il nous reste en prenant en compte le mauvais cas où 1 serait complémentaire à un nombre premier.

nb_paires = int(preuve_Goldbach(n) / 2)

print("Il y a", nb_paires, "paires de Goldbach pour n =", n)

print("")
find_puissance_2(n)
