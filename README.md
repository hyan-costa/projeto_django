# projeto_django (mecânica)
* OBS: Em Desenvolvimento...

Essa aplicação tem a função de ajudar oficinas mecânicas e lavajatos a gerenciar seus serviços.
Para rodar a aplicação, basta fazer o git clone do repositório.
Depois disso, com o Django e o python instalados, basta executar os seguites 
 comandos abaixo para aplicar as migrações:

* No arquivo settings.py você pode perceber que estou usando mysql 


        python3 manage.py makemigrations
        --------------------------------
        python3 manage.py migrate

* Crie um super usuário para gerenciar a aplicação com maior facilidade  com o seguinte comando: 


        python3 manage.py createsuperuser

* Depois, basta iniciar o servidor com o comando:

    
        python3 manage.py runserver