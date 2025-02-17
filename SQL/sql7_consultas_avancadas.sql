-- ATIVIDADE PRÁTICA DO MÓDULO 16 - SQL: CONSULTAS AVANÇADAS
-- 1. Use o banco de dados restaurante
USE restaurante;

-- 2. Crie uma view chamada resumo_pedido do join entre essas tabelas:
-- pedidos: id, quantidade e data
-- clientes: nome e email
-- funcionarios: nome
-- produtos: nome, preco

CREATE OR REPLACE VIEW resumo_pedido AS
SELECT pe.id_pedido, pe.quantidade, pe.data_pedido, c.nome AS cliente,
	c.email, f.nome AS funcionario, pr.nome AS produto, pr.preco
FROM pedidos pe
JOIN clientes c ON pe.id_cliente = c.id_cliente
JOIN funcionarios f ON pe.id_funcionario = f.id_funcionario
JOIN produtos pr ON pe.id_produto = pr.id_produto
GROUP BY id_pedido ORDER BY id_pedido;


-- 3. Selecione o id do pedido, nome do cliente e o total (quantidade * preco) de cada pedido da view resumo_pedido
SELECT id_pedido, cliente, SUM(quantidade * preco) AS total FROM resumo_pedido GROUP BY id_pedido ORDER BY total DESC;


-- 4. Atualiza o view resumo pedido, adicionando campo total
CREATE OR REPLACE VIEW resumo_pedido AS
SELECT pe.id_pedido, pe.quantidade, pe.data_pedido, c.nome AS cliente,
	c.email, f.nome AS funcionario, pr.nome AS produto, pr.preco,
    SUM(pe.quantidade * pr.preco) AS total
FROM pedidos pe
JOIN clientes c ON pe.id_cliente = c.id_cliente
JOIN funcionarios f ON pe.id_funcionario = f.id_funcionario
JOIN produtos pr ON pe.id_produto = pr.id_produto
GROUP BY id_pedido ORDER BY id_pedido;


-- 5. Repita a consulta da questão 3, utilizando o campo total adicionado
SELECT id_pedido, cliente, total FROM resumo_pedido ORDER BY total DESC;


-- 6. Repita a consulta da pergunta anterior, com uso do EXPLAIN para verificar e compreender o JOIN que está oculto na nossa query
EXPLAIN SELECT id_pedido, cliente, total FROM resumo_pedido ORDER BY total DESC;


-- 7. Crie uma função chamada ‘BuscaIngredientesProduto’, que irá retornar os ingredientes da tabela info produtos,
-- quando passar o id de produto como argumento (entrada) da função.
DELIMITER //
CREATE FUNCTION BuscaIngredientesProduto(idProduto INT)
RETURNS VARCHAR(200)
READS SQL DATA
BEGIN
	DECLARE ingredientes VARCHAR (200);
    SELECT ip.ingredientes INTO ingredientes FROM info_produtos ip WHERE ip.id_produto = idProduto;
    RETURN ingredientes;
END //
DELIMITER ;

SHOW FUNCTION STATUS;


-- 8. Execute a função ‘BuscaIngredientesProduto’ com o id de produto 10
SELECT BuscaIngredientesProduto(10);

-- 9. Crie uma função chamada ‘mediaPedido’ que irá retornar uma mensagem dizendo que 
-- o total do pedido é acima, abaixo ou igual a média de todos os pedidos, quando passar o id do pedido como argumento da função
SELECT AVG(total) FROM resumo_pedido;

DELIMITER //
CREATE FUNCTION mediaPedido(idPedido INT)
RETURNS VARCHAR (20)
READS SQL DATA
BEGIN
	DECLARE media DECIMAL(10,2);
    DECLARE vlr_pedido DECIMAL(10,2);
    DECLARE resposta VARCHAR(20);
    
    SELECT AVG(total) INTO media FROM resumo_pedido;
    SELECT total INTO vlr_pedido FROM resumo_pedido WHERE id_pedido = idPedido;
    
    SET resposta = CASE
		WHEN vlr_pedido < media THEN 'Abaixo da média'
        WHEN vlr_pedido > media THEN 'Acima da média'
        ELSE 'Na média'
    END;
    
    RETURN resposta;
END //
DELIMITER ;


-- 10. Execute a função ‘mediaPedido’ com o id de pedido 5 e depois 6.
SELECT mediaPedido(5);
SELECT mediaPedido(6);

-- 11. Como submeter sua entrega: Salve o script como “consultas_avancadas.sql” e envie o arquivo para os tutores no campo de entrega.