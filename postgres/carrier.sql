CREATE DATABASE transportadora;
GRANT ALL PRIVILEGES ON DATABASE transportadora TO postgres;

\connect transportadora;

CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nome CHARACTER VARYING (255),
  endereco CHARACTER VARYING (255),
  cidade CHARACTER VARYING (255),
  estado CHAR (2),
  data_criacao TIMESTAMPTZ
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  data_criacao TIMESTAMPTZ,
  id_cliente NUMERIC
);

CREATE TABLE entregas (
  id SERIAL PRIMARY KEY,
  status CHARACTER VARYING (255),
  id_pedido NUMERIC
);


INSERT INTO clientes (nome, endereco, cidade, estado, data_criacao)
VALUES
  ('Pedro Augusto da Rocha',	'Rua Pedro Carlos Hoffman',	'Porto Alegre',	'RS', '2022-01-01 15:34:34'),
  ('Antonio Carlos Mamel',	'Av. Pinheiros', 'Belo Horizonte',	'MG', '2022-01-03 17:12:00'),
  ('Luiza Augusta Mhor',	'Rua Salto Grande',	'Niteroi',	'RJ', '2022-01-02 08:24:27'),
  ('Jane Ester',	'Av 7 de setembro',	'Erechim',	'RS', '2022-01-02 06:51:16'),
  ('Marcos Antônio dos Santos',	'Av Farrapos',	'Porto Alegre',	'RS', '2022-01-05 10:03:59');


INSERT INTO pedidos (data_criacao, id_cliente)
VALUES
  ('2022-01-01 15:34:34', 2),
  ('2022-01-03 17:12:00', 3),
  ('2022-01-02 08:24:27', 5),
  ('2022-01-02 06:51:16', 1),
  ('2022-01-05 10:03:59', 4);


INSERT INTO entregas (status, id_pedido)
VALUES
  ('Em transito', 2),
  ('Em processamento', 3),
  ('Em transito', 1),
  ('Entregue', 4),
  ('Em transito', 5);
