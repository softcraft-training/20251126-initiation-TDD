# Testing

## C’est quoi un test ?

Action manuelle ou automatisée vérifiant dans un contexte donné qu'un autre code a les effets attendus au regard d'un exemple d'un concept particulier.

## Pourquoi ?

Ecrire des tests automatisés offre plusieurs avantages :

- Valider que le code fait ce que l'on pense.
- Faciliter la détection des régressions.
- Faciliter le refactoring.
- Documenter le code.

## Test unitaire, test d’intégration, test fonctionnel, etc, quelles différences ?

Attention la taxonomie des tests et notamment la définition de "unitaire" est sans fin et peut différer en fonction des contextes d'entreprises. 

- **Unitaire :** test vérifiant les attendus d’une brique unitaire (fonction, classe, module, etc) d'un système. Ils sont généralement peu couteux à écrire car isolés et très rapides à executer.
- **Intégration**  : test vérifiant les attendus de sous ensembles d'un système une fois connectées ensemble. Ils sont généralement plus lents et plus couteux à mettre en place que les tests unitaires.
- **Fonctionnel** :  test vérifiant les attendus métier d’un système ou de sous ensembles de celui-ci.  Ils sont généralement plus lents et plus couteux à mettre en place que les tests unitaires.
- **Acceptance** : test vérifiant les attendus d’un cas d’usage métier d’un système ou de sous ensembles de celui-ci.  Ils sont généralement plus lents et plus couteux à mettre en place que les tests unitaires.
- **End 2 End :** test vérifiant les attendus d’un système ou les entrées sont une simulation d'un utilisateur réel via une IHM. Ils sont généralement très lents à executer et peuvent etre fragiles et compliqués à écrire.
- **Tests de performance, Test de sécurité, Tests exploratoires, Tests de mutation, Tests de propriétés, Tests de contrats, etc**

## Comment je m’y prends ?

Le pattern des 3A :

- **ARRANGE** : code permettant de mettre en place le contexte pour le code à tester.
    - *Exemple :* Etant donné A égal à 10 et B égal à 2.
- **ACT** : code exécutant l’action qu’on cherche à valider.
    - *Exemple :* Quant on divise A par B.
- **ASSERT** :  code vérifiant les effets attendus du code testé.
    - *Exemple :* Alors on doit obtenir 2.

Dans le meme esprit, il existe une variante avec le pattern : **GIVEN, WHEN, THEN**

## Ok mais je vérifie quoi ?

On vérifie généralement les effets attendus d'exemples de deux types de cas d'utilisation :

- **Cas nominal** : cas ou les exemples d'utilisation correspondent aux cas généraux (happy path).
    - *Exemple :* Prenons le cas de la division, des exemples de cas généraux sont 1/2, 3/7, etc.
- **Cas à la marge** : cas ou les exemples d'utilisation correspondent à des erreurs, des exceptions, des cas non généraux.
    - *Exemple :* Prenons le cas de la division, un exemple de cas à la marge est la division par 0.

## Ça marche ! Et de quoi j'ai besoin ?

De quoi écrire les tests (bibliothèque de tests, bibliothèque d'assertions) et de quoi exécuter les tests (test runner). Dans la grande majorité des cas les frameworks de tests contiennent tout ce qu'il faut pour démarrer (tests, assertions, runner).

## Mise en pratique

**Objectif** : Ecrire son premier test

**Temps** : 15 minutes

- **L'initialisation**
    
    Lancer les commandes dans un shell :
    
    ```bash
    mkdir src
    cd src
    "" > deepThought.py
    "" > test_deepThought.py
    python -m pip install pytest
    ```
    
- **Le code à tester**
    
    Ecrire dans le fichier `deepThought.py` :
    
    ```python
    def answerToTheUltimateQuestionOfLifeTheUniverseAndEverything():
        return "oups"
    ```
    
- **Le code de test**
    
    Ecrire dans le fichier `test_deepThought.py` :
    
    ```python
    import pytest
    from deepThought import answerToTheUltimateQuestionOfLifeTheUniverseAndEverything
    
    def test_deepThought():
    	assert answerToTheUltimateQuestionOfLifeTheUniverseAndEverything() == "42"
    ```
    
- **Lancer les tests**
    
    Lancer la commande `python -m pytest` dans un shell :
    
    ![Untitled](img1.png)
    

## C'est quoi les bonnes pratiques ?

Ecrire des tests unitaires de bonne qualité necessite de suivre quelques règles :

- **Fast** : les tests doivent etre rapides à l'execution afin d'obtenir une bonne expèrience développeur.
- **Independent** : les tests doivent etre isolés et ne pas dépendre entre eux ou de dépendances tierces.
- **Repeatable** : les tests doivent etre deterministes et ne pas varier en fonction d'éléments extérieurs.
- **Self-validating** : les tests doivent auto-suffisants et se suffire à eux-meme afin de déterminer un succès ou un échec.
- **Through** : les tests doivent aussi bien prendre en considération le happy path que les scénarios négatifs.


## C'est quoi les bonnes pratiques ?

Ecrire des tests unitaires de bonne qualité necessite de suivre quelques règles :

- **Fast** : les tests doivent etre rapides à l'execution afin d'obtenir une bonne expèrience développeur.
- **Independent** : les tests doivent etre isolés et ne pas dépendre entre eux ou de dépendances tierces.
- **Repeatable** : les tests doivent etre deterministes et ne pas varier en fonction d'éléments extérieurs.
- **Self-validating** : les tests doivent auto-suffisants et se suffire à eux-meme afin de déterminer un succès ou un échec.
- **Through** : les tests doivent aussi bien prendre en considération le happy path que les scénarios négatifs.

## Et sinon TDD (Test Driven Development) ?

TDD n’est pas une technique d’écriture de tests mais un cycle de développement guidé par les tests (le fait d’avoir des tests est une conséquence du cycle) :

- **RED** : écrire un test et le faire échouer.
- **GREEN** : écrire le code de production minimum permettant de faire passer le test en succès.
- **REFACTOR** : nettoyer le code (Duplication, Lisibilité, Code Smells...).

Et on recommence :) Ecrire des tests unitaires avec TDD offre plusieurs avantages :

- Clarifie l'objectif avant de passer à l'implémentation du code.
- Encourage le développement incrémetal grace aux baby steps.
- Décourage le couplage de code et l'over engineering.

## Mise en pratique

**Objectif** : Initiation à TDD

**Temps** : 30 minutes

- **Le métier**
    
    Construire une fonction fizzBuzz qui transforme un entier en chaine de caractères selon les règles suivantes :
    
    - Pour les multiples de 3, remplacer le nombre par Fizz
    - Pour les multiples de 5, remplacer le nombre par Buzz
    - Pour les multiples et 3 et de 5, remplacer le nombre par FizzBuzz
    - Pour les autres nombres, retourner le nombre
    
    ```bash
    1 => 1
    2 => 2
    3 => Fizz
    4 => 4
    5 => Buzz
    6 => Fizz
    15 => FizzBuzz
    ```
    
- **L'initialisation**
    
    Lancer les commandes dans un shell :
    
    ```bash
    mkdir src
    cd src
    "" > fizzbuzz.py
    "" > test_fizzbuzz.py
    python -m pip install pytest
    ```
    
- **Itération 1**
    - **RED**
        
        Ecrire un test dans le fichier `test_fizzbuzz.py` et le faire échouer :
        
        ```python
        import pytest
        from fizzbuzz import fizzbuzz
        
        def test_siNombreEstUnAlors1():
        	assert fizzbuzz(1) == "1"
        ```
        
    - **GREEN**
        
        Ecrire le code de production minimum dans le fichier `fizzbuzz.py` permettant de faire passer le test en succès :
        
        ```python
        def fizzbuzz(entry):
        	return "1"
        ```
        
    - **REFACTOR**
        
        RAS
        
- **Itération 2**
    - **RED**
        
        Ecrire un test dans le fichier `test_fizzbuzz.py` et le faire échouer :
        
        ```python
        // siNombreEstUnAlors1
        
        def test_siNombreNiMultipleDeTroisNiMultipleDeCinqAlorsNombre():
        	assert fizzbuzz(2) == "2"
        ```
        
    - **GREEN**
        
        Ecrire le code de production minimum dans le fichier `fizzbuzz.py` permettant de faire passer le test en succès :
        
        ```python
        def fizzbuzz(entry):
        	return str(entry);
        ```
        
    - **REFACTOR**
        
        Nettoyer le code :
        
        ```python
        casesNotMultipleOf3Nor5 = [(1, "1"), (2, "2")]
        
        @pytest.mark.parametrize("entry,expected", casesNotMultipleOf3Nor5)
        def test_siNombreNiMultipleDeTroisNiMultipleDeCinqAlorsNombre(entry, expected):
        	assert fizzbuzz(entry) == expected
        ```
        
- **Itération 3**
    - **RED**
        
        Ecrire un test dans le fichier `test_fizzbuzz.py` et le faire échouer :
        
        ```python
        // siNombreNiMultipleDeTroisNiMultipleDeCinqAlorsNombre
        
        def test_siNombreMultipleDeTroisAlorsFizz():
        	assert fizzbuzz(3) == "Fizz"
        ```
        
    - **GREEN**
        
        Ecrire le code de production minimum dans le fichier `fizzbuzz.py` permettant de faire passer le test en succès :
        
        ```python
        def fizzbuzz(entry):
        	if entry == 3:
            return 'Fizz'
        	else:
        		return str(entry);
        ```
        
    - **REFACTOR**
        
        RAS
        
- **Itération 4**
    - **RED**
        
        Ecrire un test dans le fichier `test_fizzbuzz.py` et le faire échouer :
        
        ```tsx
        // siNombreNiMultipleDeTroisNiMultipleDeCinqAlorsNombre
        
        casesFizz = [(3, "Fizz"), (6, "Fizz")]
        
        @pytest.mark.parametrize("entry,expected", casesFizz)
        def test_siNombreMultipleDeTroisAlorsFizz(entry, expected):
        	assert fizzbuzz(entry) == expected
        ```
        
    - **GREEN**
        
        Ecrire le code de production dans le fichier `fizzbuzz.py` minimum permettant de faire passer le test en succès :
        
        ```python
        def fizzbuzz(entry):
          if entry % 3 == 0: 
        		return "Fizz"
        	else:
        		return str(entry)
        ```
        
    - **REFACTOR**
        
        Nettoyer le code :
        
        ```python
        def fizzbuzz(entry):
          if isMultipleOf3(entry): 
        		return "Fizz"
        	else:
        		return str(entry)
        
        def isMultipleOf3(number): 
          return number % 3 == 0
        ```

## Exercice

**Objectif** : Pratique de TDD

**Temps** : 60 à 90 minutes

**Sujet** : [Tennis Kata](https://codingdojo.org/fr/kata/Tennis/)

