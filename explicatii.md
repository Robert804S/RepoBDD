TDD = Test driven development
In aceasta tehnica de dezvoltare software, se creeaza mai intai cazurile de testare si apoi se scrie codul care sta la baza acestor cazuri de testare

BDD = Behavior Driven Development
BDD este o extensie a TDD unde, in loc sa scriem cazurile de testare, incepem prin a scrie un comportament
Mai tarziu, dezvoltam codul care este necesar pentru ca aplicatia noastra sa indeplineasca comportamentul

Scenariul definit in abordarea BDD faciliteaza colaborarea dezvoltatorilor, testerilor si oricaror altori stakeholderi interesati (business analysts, product owner, etc)
Adica este util in momentul in care interactionam cu alte persoane care nu au cunostinte tehnice 
pentru a le putea furniza informatii cu privire la testele pe care le-am facut


Structura unui framework BDD este urmatoarea (pe care o vom implementa si noi):

1. Folder features = Feature files (fisiere scrise intr-un limbaj mai natural (gherkin) care sa descrie scenariile de business)
   - Given (contextul in care se desfasoara actiunea)
   - When (actiunea pe care o facem)
   - Then (deznodamantul - verificarea pe care vrem sa o facem)

In cazul in care avem pasi care se reproduc in mai multe scenarii sau in toate, atunci putem sa le punem in Background (este ca setUp-ul din unittest)

2. Folder steps = Step definition files (maparea tehnica a fisierlor de business - feature files)

3. Folder pages = Pagini de mapare pentru elementele din browser (POM - page object model)
    - Vom avea fisiere pentru fiecare pagina a aplicatiei
    - base_page file (vom avea o clasa ce contine metode care pot fi folosite in mai multe clase, adica care sunt utile pentru toate paginile)

4. Fisier browser (care o sa contina instructiuni de instalare si deschidere browser)

5. Fisier environment (care o sa contina instantierea tuturor claselor de tip pages)



Metodologii de lucru:

1. Waterfall: 
   - metodologie mai stricta
   - orice modificare necesara dupa inceperea proiectului va trebui implementata intr-un proiect nou 
   - se planuieste tot la inceput, apoi se dezvolta, apoi se testeaza si apoi se da in piata
   - feedback-ul pt produs de la clienti se primeste tarziu, la final
   - de regula se dezvolta multa functionalitate

2. Agile:
    - o metodologie mai putin stricta, este flexibila si organizata
    - orice modificare aparuta in timpul implementarii, se poate modifica pe parcurs
    - se lucreaza in sprint-uri (de regula cicluri de 2 saptmani)
    - intr-un sprint se planifica, se dezvolta, se testeaza si se da in piata
    - feedback-ul pt produs de la clienti se primeste dupa fiecare sprint si se poate implementa in urmatoarele sprint-uri

Sprint = o perioada definita in care se implementeaza un anumit set de functionalitati

In general functionalitatile se pot grupa in felul urmator:
1. Componente majore (ex: pagina de cos de cumparaturi) - Epic
2. Functionalitati independente din acea componenta - Story
(adaugarea unui produs in cos, scoaterea unui produs din cos, incrementarea nr de produse, etc)

User Story:
As a customer I want to remove a product from my shopping cart
As a customer I want to increment or decrement the no. of products from my shopping cart
As a customer I want to add a voucher to my shopping cart

Comanda cu care rulam testele cu behave: behave -f html -o behave-report.html --tags=smoke