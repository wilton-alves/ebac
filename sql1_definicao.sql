-- Tarefa prática do módulo 'SQL: Linguagem de Definição de Dados'

CREATE DATABASE restaurante; #Criando o Banco de dados
USE restaurante; #Utilizando o Banco de dados

-- 1. Crie a tabela de Funcionários (funcionarios):
CREATE TABLE IF NOT EXISTS funcionarios(
id_funcionario INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
nome VARCHAR(255),
cpf VARCHAR(14),
data_nascimento DATE,
endereco VARCHAR(255),
telefone VARCHAR(15),
email VARCHAR(100),
cargo VARCHAR(100),
salario DECIMAL(10,2),
data_admissao DATE
);

-- 2. Crie a Tabela de Clientes (clientes)
CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
nome VARCHAR(255),
cpf VARCHAR(14),
data_nascimento DATE,
endereco VARCHAR(255),
telefone VARCHAR(15),
email VARCHAR(100),
data_cadastro DATE
);

-- 3. Crie a Tabela de Produtos (produtos)
CREATE TABLE IF NOT EXISTS produtos(
id_produto INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
nome VARCHAR(255),
descricao TEXT,
preco DECIMAL(10,2),
categoria VARCHAR(100)
);

-- 4. Crie a Tabela de Pedidos (pedidos)
CREATE TABLE IF NOT EXISTS pedidos(
id_pedido INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
id_cliente INT, FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
id_funcionario INT, FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario),
id_produto INT, FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
quantidade INT,
preco DECIMAL(10,2),
data_pedido DATE,
status_pedido VARCHAR(50)
);

-- 5. Crie a tabela de informações adicionais dos produtos (info_produtos)
CREATE TABLE IF NOT EXISTS info_produtos(
id_info INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
id_produto INT, FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
ingredientes TEXT,
fornecedor VARCHAR(255)
);