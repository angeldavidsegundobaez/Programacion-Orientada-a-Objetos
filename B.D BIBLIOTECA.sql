SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE biblioteca CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE biblioteca;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE autor(
    id_autor INT AUTO_INCREMENT,
    nombre_autor VARCHAR(70) NOT NULL UNIQUE,
    nacionalidad VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_autor)
);

CREATE TABLE libro(
    id_libro INT AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    id_autor INT,
    fecha_publicacion DATE,
    PRIMARY KEY(id_libro)
);

CREATE TABLE lector(
    id_lector INT AUTO_INCREMENT,
    nombre_lector VARCHAR(60) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    correo VARCHAR(80),
    telefono VARCHAR(10),
    PRIMARY KEY(id_lector)
);

CREATE TABLE prestamo(
    id_prestamo INT AUTO_INCREMENT,
    fecha_prestamo DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_libro INT,
    id_lector INT,
    fecha_devolucion DATE,
    PRIMARY KEY(id_prestamo)
);

SHOW TABLES;

-- RELACIONES Y RESTRICCIONES
ALTER TABLE libro ADD CONSTRAINT fk_autor_libro
FOREIGN KEY(id_autor) REFERENCES autor(id_autor);

ALTER TABLE prestamo ADD CONSTRAINT fk_libro_prestamo
FOREIGN KEY(id_libro) REFERENCES libro(id_libro);

ALTER TABLE prestamo ADD CONSTRAINT fk_lector_prestamo
FOREIGN KEY(id_lector) REFERENCES lector(id_lector);

-- Inserción de autores
INSERT INTO autor (nombre_autor, nacionalidad) VALUES 
('Gabriel García Márquez', 'Colombiano'),
('Isabel Allende', 'Chilena'),
('Mario Vargas Llosa', 'Peruano'),
('Julio Cortázar', 'Argentino'),
('Jorge Luis Borges', 'Argentino'),
('Miguel de Cervantes', 'Español'),
('Jane Austen', 'Británica'),
('Haruki Murakami', 'Japonés'),
('J.K. Rowling', 'Británica'),
('Stephen King', 'Estadounidense');

SELECT * FROM autor;

-- Inserción de libros
INSERT INTO libro (titulo, genero, id_autor, fecha_publicacion) VALUES
('Cien años de soledad', 'Realismo mágico', 1, '1967-05-30'),
('La casa de los espíritus', 'Novela', 2, '1982-01-01'),
('La ciudad y los perros', 'Novela', 3, '1963-01-01'),
('Rayuela', 'Ficción', 4, '1963-06-28'),
('El Aleph', 'Cuento', 5, '1949-01-01'),
('Don Quijote de la Mancha', 'Novela', 6, '1605-01-01'),
('Orgullo y prejuicio', 'Romance', 7, '1813-01-28'),
('Kafka en la orilla', 'Ficción', 8, '2002-09-12'),
('Harry Potter y la piedra filosofal', 'Fantasía', 9, '1997-06-26'),
('El resplandor', 'Terror', 10, '1977-01-28');

SELECT * FROM libro;

-- Inserción de lectores
INSERT INTO lector (nombre_lector, apellidos, correo, telefono) VALUES
('Juan', 'Pérez Gómez', 'juan.perez@mail.com', '5551234567'),
('María', 'García López', 'maria.garcia@mail.com', '5552345678'),
('Carlos', 'Fernández Ruiz', 'carlos.fernandez@mail.com', '5553456789'),
('Laura', 'Martínez Díaz', 'laura.martinez@mail.com', '5554567890'),
('Pedro', 'Rodríguez Torres', 'pedro.rodriguez@mail.com', '5555678901'),
('Ana', 'Sánchez Moreno', 'ana.sanchez@mail.com', '5556789012'),
('Luis', 'Ramírez Gómez', 'luis.ramirez@mail.com', '5557890123'),
('Sofía', 'Torres Castillo', 'sofia.torres@mail.com', '5558901234'),
('Javier', 'López Jiménez', 'javier.lopez@mail.com', '5559012345'),
('Elena', 'Gómez Vázquez', 'elena.gomez@mail.com', '5550123456');

SELECT * FROM lector;

-- Inserción de préstamos
INSERT INTO prestamo (id_libro, id_lector, fecha_devolucion) VALUES
(1, 1, '2025-03-01'),
(2, 2, '2025-03-05'),
(3, 3, '2025-03-10'),
(4, 4, '2025-03-12'),
(5, 5, '2025-03-15'),
(6, 6, '2025-03-20'),
(7, 7, '2025-03-25'),
(8, 8, '2025-03-28'),
(9, 9, '2025-04-01'),
(10, 10, '2025-04-05');

SELECT * FROM prestamo;



