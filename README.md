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
    - *Exemple : *****Prenons le cas de la division, des exemples de cas généraux sont 1/2, 3/7, etc.
- **Cas à la marge** : cas ou les exemples d'utilisation correspondent à des erreurs, des exceptions, des cas non généraux.
    - *Exemple : *****Prenons le cas de la division, un exemple de cas à la marge est la division par 0.

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
    
    ![Untitled](Testing%20940035c3cdc24a538985c8b350bf1e69/Untitled.png)
    

## C'est quoi les bonnes pratiques ?

Ecrire des tests unitaires de bonne qualité necessite de suivre quelques règles :

- **Fast** : les tests doivent etre rapides à l'execution afin d'obtenir une bonne expèrience développeur.
- **Independent** : les tests doivent etre isolés et ne pas dépendre entre eux ou de dépendances tierces.
- **Repeatable** : les tests doivent etre deterministes et ne pas varier en fonction d'éléments extérieurs.
- **Self-validating** : les tests doivent auto-suffisants et se suffire à eux-meme afin de déterminer un succès ou un échec.
- **Through** : les tests doivent aussi bien prendre en considération le happy path que les scénarios négatifs.
