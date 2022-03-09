# Estudo sobre Orientação a Objetos

```bash
docker-compose up -d

docker-compose run app
```

Acesse o link

```
http://localhost:8080
```

08/03/2022

Criar classe separada pra ver o que é o produto

Criar modelo do produto

Melhorar cart

Carregar cart instanciado , sem usar variável de classe

Leio, transcrever de file para class Product

Escrevo, transcrever class Product para file

---

Rodar tanto em console como web. console.py and web.py

Clique no item que desejar.

Clique em Checkout! para finalizar a compra ou em Keep buying! para retornar a tela inicial e escolher mais opções.

Na tela seguinte ao do carrinho, você terá o valor total da compra. Clicando em Purchase!, a compra será finalizada.


22/02/2022

Disponibilizar a aplicação na Web - HTML - Sem framework, sem CSS

Transportar de CLI para versão WEB

Página de listagem, com os produtos - GET /products

Cada produto tem 1 link para - /cart/PRODUCT_ID

Lista de quantidade no cart e clicar em ADD no CART

Adicionado no carrinho, redirecionar para a listagem

Na listagem, botão de fechar a compra para /checkout

Em /checkout, link para /sucesso

Página /sucesso irá exibir mensagem final

Usar sessão com cookie para guardar o carrinho

Desafio é reusar o que já está disponível

python http.py - rodar servidor web

Continuar usando a base de administração de produtos

Interface web - funções, requisições HTTP
