import hashlib
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="traintrack")
cursor = db.cursor()


def executeSQL(sql):
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("Error:", e)
        db.rollback()


teamSQL = """
INSERT INTO league_team (id, team_code, name, category, league, town) VALUES
(1, 'UDLZ001', 'UD Las Zocas', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Las Zocas'),
(2, 'CDTF002', 'CD Tenerife', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Santa Cruz de Tenerife'),
(3, 'CDM003', 'CD Marino', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Playa de las Américas'),
(4, 'UDI004', 'UD Icodense', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Icod de los Vinos'),
(5, 'CDL005', 'CD Laguna', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'San Cristóbal de La Laguna'),
(6, 'UDGI006', 'UD Guía de Isora', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Guía de Isora'),
(7, 'CDT007', 'CD Tejina', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Tejina'),
(8, 'CDUSY008', 'CD Unión Sur Yaiza', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Yaiza'),
(9, 'CDB009', 'CD Buzanada', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Buzanada'),
(10, 'UDT010', 'UD Tacoronte', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Tacoronte'),
(11, 'UDI011', 'UD Ibarra', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Ibarra'),
(12, 'CDA012', 'CD Atalaya', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Atalaya'),
(13, 'UDCS013', 'UD Cruz Santa', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Cruz Santa'),
(14, 'CDT014', 'CD Tegueste', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'Tegueste'),
(15, 'CDSI015', 'CD San Isidro', 'Prebenjamin', 'Liga Prebenjamin Tenerife', 'San Isidro'),
(16, 'UDLZ420572', 'UD Las Zocas', 'Benjamin', 'Liga Benjamin Tenerife', 'Las Zocas'),
(17, 'CDTF2380472', 'CD Tenerife', 'Benjamin', 'Liga Benjamin Tenerife', 'Santa Cruz de Tenerife'),
(18, 'CDM423940', 'CD Marino', 'Benjamin', 'Liga Benjamin Tenerife', 'Playa de las Américas'),
(19, 'UDI644226', 'UD Icodense', 'Benjamin', 'Liga Benjamin Tenerife', 'Icod de los Vinos'),
(20, 'CDL325633', 'CD Laguna', 'Benjamin', 'Liga Benjamin Tenerife', 'San Cristóbal de La Laguna'),
(21, 'UDGI6446424', 'UD Guía de Isora', 'Benjamin', 'Liga Benjamin Tenerife', 'Guía de Isora'),
(22, 'CDT2566242', 'CD Tejina', 'Benjamin', 'Liga Benjamin Tenerife', 'Tejina'),
(23, 'CDUSY0592', 'CD Unión Sur Yaiza', 'Benjamin', 'Liga Benjamin Tenerife', 'Yaiza'),
(24, 'CDB995895', 'CD Buzanada', 'Benjamin', 'Liga Benjamin Tenerife', 'Buzanada'),
(25, 'UDT01072940', 'UD Tacoronte', 'Benjamin', 'Liga Benjamin Tenerife', 'Tacoronte'),
(26, 'UDI01187490', 'UD Ibarra', 'Benjamin', 'Liga Benjamin Tenerife', 'Ibarra'),
(27, 'CDA01225235', 'CD Atalaya', 'Benjamin', 'Liga Benjamin Tenerife', 'Atalaya'),
(28, 'UDCS0133858', 'UD Cruz Santa', 'Benjamin', 'Liga Benjamin Tenerife', 'Cruz Santa'),
(29, 'CDT01415556', 'CD Tegueste', 'Benjamin', 'Liga Benjamin Tenerife', 'Tegueste'),
(30, 'CDSI01533573', 'CD San Isidro', 'Benjamin', 'Liga Benjamin Tenerife', 'San Isidro'),
(31, 'UDLZ82482', 'UD Las Zocas', 'alevin', 'Liga alevin Tenerife', 'Las Zocas'),
(32, 'CDTF257746', 'CD Tenerife', 'alevin', 'Liga alevin Tenerife', 'Santa Cruz de Tenerife'),
(33, 'CDM62993', 'CD Marino', 'alevin', 'Liga alevin Tenerife', 'Playa de las Américas'),
(34, 'UDI0525', 'UD Icodense', 'alevin', 'Liga alevin Tenerife', 'Icod de los Vinos'),
(35, 'CDL29592', 'CD Laguna', 'alevin', 'Liga alevin Tenerife', 'San Cristóbal de La Laguna'),
(36, 'UDGI9250', 'UD Guía de Isora', 'alevin', 'Liga alevin Tenerife', 'Guía de Isora'),
(37, 'CDT48924', 'CD Tejina', 'alevin', 'Liga alevin Tenerife', 'Tejina'),
(38, 'CDUSY93924', 'CD Unión Sur Yaiza', 'alevin', 'Liga alevin Tenerife', 'Yaiza'),
(39, 'CDB48294', 'CD Buzanada', 'alevin', 'Liga alevin Tenerife', 'Buzanada'),
(40, 'UDT48054', 'UD Tacoronte', 'alevin', 'Liga alevin Tenerife', 'Tacoronte'),
(41, 'UDI481485', 'UD Ibarra', 'alevin', 'Liga alevin Tenerife', 'Ibarra'),
(42, 'CDA82385', 'CD Atalaya', 'alevin', 'Liga alevin Tenerife', 'Atalaya'),
(43, 'UDCS25395', 'UD Cruz Santa', 'alevin', 'Liga alevin Tenerife', 'Cruz Santa'),
(44, 'CDT028495', 'CD Tegueste', 'alevin', 'Liga alevin Tenerife', 'Tegueste'),
(45, 'CDSI48205', 'CD San Isidro', 'alevin', 'Liga alevin Tenerife', 'San Isidro'),
(46, 'UDLZ9148', 'UD Las Zocas', 'infantil', 'Liga infantil Tenerife', 'Las Zocas'),
(47, 'CDTF18935', 'CD Tenerife', 'infantil', 'Liga infantil Tenerife', 'Santa Cruz de Tenerife'),
(48, 'CDM8593', 'CD Marino', 'infantil', 'Liga infantil Tenerife', 'Playa de las Américas'),
(49, 'UDI59381', 'UD Icodense', 'infantil', 'Liga infantil Tenerife', 'Icod de los Vinos'),
(50, 'CDL914952', 'CD Laguna', 'infantil', 'Liga infantil Tenerife', 'San Cristóbal de La Laguna'),
(51, 'UDGI029148', 'UD Guía de Isora', 'infantil', 'Liga infantil Tenerife', 'Guía de Isora'),
(52, 'CDT850572', 'CD Tejina', 'infantil', 'Liga infantil Tenerife', 'Tejina'),
(53, 'CDUSY244805', 'CD Unión Sur Yaiza', 'infantil', 'Liga infantil Tenerife', 'Yaiza'),
(54, 'CDB725052', 'CD Buzanada', 'infantil', 'Liga infantil Tenerife', 'Buzanada'),
(55, 'UDT927405', 'UD Tacoronte', 'infantil', 'Liga infantil Tenerife', 'Tacoronte'),
(56, 'UDI32056', 'UD Ibarra', 'infantil', 'Liga infantil Tenerife', 'Ibarra'),
(57, 'CDA21052', 'CD Atalaya', 'infantil', 'Liga infantil Tenerife', 'Atalaya'),
(58, 'UDCS294063', 'UD Cruz Santa', 'infantil', 'Liga infantil Tenerife', 'Cruz Santa'),
(59, 'CDT202528', 'CD Tegueste', 'infantil', 'Liga infantil Tenerife', 'Tegueste'),
(60, 'CDS3250', 'CD San Isidro', 'infantil', 'Liga infantil Tenerife', 'San Isidro');

"""
executeSQL(teamSQL)
# Generamos las contraseñas SHA-256 para los equipos
try:
    cursor.execute("SELECT id, team_code FROM league_team")
    teams = cursor.fetchall()
    for team in teams:
        team_id, team_code = team
        team_password = hashlib.sha256(team_code.encode()).hexdigest()
        cursor.execute(
            f"UPDATE league_team SET team_password = '{team_password}' WHERE id = {team_id}"
        )
        db.commit()
    print("Contraseñas de los equipos actualizadas")
except Exception as e:
    print("Error al actualizar contraseñas:", e)
    db.rollback()


# sqlTrainers = """
# INSERT INTO members_trainer (id, email, password, name, surname, birth, address1, address2, phone, team_id) VALUES
# (1, 'juangarcia@example.com', 'juan123', 'Juan', 'García', '1990-05-15', 'Calle Los Molinos', 'Edificio Atlántico', '+34 666 111 111',1),
# (2, 'anarodriguez@example.com', 'ana456', 'Ana', 'Rodríguez', '1985-09-20', 'Avenida Tres de Mayo', 'Bloque A', '+34 666 222 222',2),
# (3, 'pedrolopez@example.com', 'pedro789', 'Pedro', 'López', '1988-02-10', 'Calle La Marina', 'Portal 3', '+34 666 333 333',3),
# (4, 'mariamartinez@example.com', 'maria123', 'María', 'Martínez', '1992-11-08', 'Avenida de Anaga', 'Nº 15', '+34 666 444 444',4),
# (5, 'davidhernandez@example.com', 'david456', 'David', 'Hernández', '1980-07-25', 'Calle San Juan', 'Piso 2', '+34 666 555 555',5),
# (6, 'lauraperez@example.com', 'laura789', 'Laura', 'Pérez', '1983-04-30', 'Avenida de Venezuela', 'Apartamento 8', '+34 666 666 666',6),
# (7, 'javiergonzalez@example.com', 'javier123', 'Javier', 'González', '1995-01-12', 'Calle Nuestra Señora de Candelaria', 'Nº 20', '+34 666 777 777',7),
# (8, 'sarasanchez@example.com', 'sara456', 'Sara', 'Sánchez', '1987-08-17', 'Avenida de los Majuelos', 'Escalera B', '+34 666 888 888',8),
# (9, 'carlosfernandez@example.com', 'carlos789', 'Carlos', 'Fernández', '1991-06-03', 'Calle La Paz', 'Nº 5', '+34 666 999 999',9),
# (10, 'elenagomez@example.com', 'elena123', 'Elena', 'Gómez', '1986-03-18', 'Avenida de Los Menceyes', 'Piso 1', '+34 666 101 010',10),
# (11, 'migueldiaz@example.com', 'miguel456', 'Miguel', 'Díaz', '1982-12-22', 'Calle San Sebastián', 'Portal 7', '+34 666 111 222',11),
# (12, 'carmenalonso@example.com', 'carmen789', 'Carmen', 'Alonso', '1993-10-05', 'Avenida de La Salle', 'Apartamento 12', '+34 666 222 333',12),
# (13, 'franciscomorales@example.com', 'francisco123', 'Francisco', 'Morales', '1984-07-11', 'Calle Santa Úrsula', 'Bloque D', '+34 666 333 444',13),
# (14, 'isabeljimenez@example.com', 'isabel456', 'Isabel', 'Jiménez', '1990-04-28', 'Avenida Venezuela', 'Nº 25', '+34 666 444 555',14),
# (15, 'alejandroruiz@example.com', 'alejandro789', 'Alejandro', 'Ruiz', '1989-09-14', 'Calle La Libertad', 'Piso 3', '+34 666 555 666',15),
# (16, 'luisgomez@example.com', 'luis123', 'Luis', 'Gómez', '1987-06-25', 'Calle Los Pinos', 'Edificio Central', '+34 666 666 666',16),
# (17, 'elenarodriguez@example.com', 'elena456', 'Elena', 'Rodríguez', '1984-02-14', 'Avenida de Los Robles', 'Bloque B', '+34 666 777 777',17),
# (18, 'sergiofernandez@example.com', 'sergio789', 'Sergio', 'Fernández', '1990-11-30', 'Calle La Montaña', 'Portal 5', '+34 666 888 888',18),
# (19, 'luciagarcia@example.com', 'lucia123', 'Lucía', 'García', '1983-08-12', 'Avenida Las Palmeras', 'Nº 10', '+34 666 999 999',19),
# (20, 'jorgeperez@example.com', 'jorge456', 'Jorge', 'Pérez', '1995-03-07', 'Calle Las Rosas', 'Piso 4', '+34 666 101 010',20),
# (21, 'mariafernandez@example.com', 'maria789', 'María', 'Fernández', '1986-09-23', 'Avenida Los Girasoles', 'Escalera C', '+34 666 111 111',21),
# (22, 'albertogomez@example.com', 'alberto123', 'Alberto', 'Gómez', '1981-12-17', 'Calle Los Almendros', 'Apartamento 3', '+34 666 222 222',22),
# (23, 'laurarodriguez@example.com', 'laura456', 'Laura', 'Rodríguez', '1992-07-03', 'Avenida de Las Flores', 'Nº 30', '+34 666 333 333',23),
# (24, 'pablofernandez@example.com', 'pablo789', 'Pablo', 'Fernández', '1988-04-18', 'Calle Las Margaritas', 'Piso 5', '+34 666 444 444',24),
# (25, 'sandraruiz@example.com', 'sandra123', 'Sandra', 'Ruiz', '1980-10-22', 'Avenida Los Tilos', 'Portal 9', '+34 666 555 555',25),
# (26, 'raulrodriguez@example.com', 'raul456', 'Raúl', 'Rodríguez', '1993-01-05', 'Calle Las Orquídeas', 'Nº 35', '+34 666 666 666',26),
# (27, 'cristinaperez@example.com', 'cristina789', 'Cristina', 'Pérez', '1985-05-30', 'Avenida Las Azucenas', 'Bloque E', '+34 666 777 777',27),
# (28, 'juanfernandez@example.com', 'juan123', 'Juan', 'Fernández', '1982-02-13', 'Calle Las Dalias', 'Apartamento 7', '+34 666 888 888',28),
# (29, 'rosariogarcia@example.com', 'rosario456', 'Rosario', 'García', '1989-07-28', 'Avenida Las Acacias', 'Piso 6', '+34 666 999 999',29),
# (30, 'danielruiz@example.com', 'daniel789', 'Daniel', 'Ruiz', '1991-03-15', 'Calle Los Lirios', 'Escalera D', '+34 666 101 010',30),
# (31, 'mariaperez@example.com', 'maria123', 'María', 'Pérez', '1984-06-10', 'Calle Las Hortensias', 'Edificio A', '+34 666 202 020',31),
# (32, 'carlosrodriguez@example.com', 'carlos456', 'Carlos', 'Rodríguez', '1996-02-20', 'Avenida Los Pinos', 'Nº 40', '+34 666 303 030',32),
# (33, 'luisaflores@example.com', 'luisa789', 'Luisa', 'Flores', '1987-09-05', 'Calle Las Camelias', 'Piso 7', '+34 666 404 040',33),
# (34, 'davidsanchez@example.com', 'david123', 'David', 'Sánchez', '1990-04-01', 'Avenida Las Margaritas', 'Bloque F', '+34 666 505 050',34),
# (35, 'patriciamartinez@example.com', 'patricia456', 'Patricia', 'Martínez', '1983-11-15', 'Calle Los Girasoles', 'Portal 11', '+34 666 606 060',35),
# (36, 'sergioalvarez@example.com', 'sergio789', 'Sergio', 'Álvarez', '1988-01-30', 'Avenida Las Acacias', 'Apartamento 10', '+34 666 707 070',36),
# (37, 'luciamartin@example.com', 'lucia123', 'Lucía', 'Martín', '1992-08-25', 'Calle Los Pinos', 'Piso 8', '+34 666 808 080',37),
# (38, 'javierlopez@example.com', 'javier456', 'Javier', 'López', '1981-03-10', 'Avenida Las Palmeras', 'Escalera E', '+34 666 909 090',38),
# (39, 'mariagarcía@example.com', 'maria789', 'María', 'García', '1984-10-26', 'Calle Las Azucenas', 'Nº 45', '+34 666 010 101',39),
# (40, 'carlosrodriguez@example.com', 'carlos123', 'Carlos', 'Rodríguez', '1989-07-12', 'Avenida Los Tilos', 'Bloque G', '+34 666 111 212',40),
# (41, 'juliamartinez@example.com', 'julia456', 'Julia', 'Martínez', '1993-04-05', 'Calle Las Rosas', 'Apartamento 11', '+34 666 212 323',41),
# (42, 'davidjimenez@example.com', 'david789', 'David', 'Jiménez', '1986-11-20', 'Avenida Las Hortensias', 'Piso 9', '+34 666 323 434',42),
# (43, 'lauramartinez@example.com', 'laura123', 'Laura', 'Martínez', '1981-06-03', 'Calle Los Lirios', 'Escalera F', '+34 666 434 545',43),
# (44, 'albertoperez@example.com', 'alberto456', 'Alberto', 'Pérez', '1985-01-18', 'Avenida Las Margaritas', 'Nº 50', '+34 666 545 656',44),
# (45, 'luciagonzalez@example.com', 'lucia789', 'Lucía', 'González', '1990-08-08', 'Calle Las Camelias', 'Portal 13', '+34 666 656 767',45),
# (46, 'andreslopez@example.com', 'andres123', 'Andrés', 'López', '1988-05-20', 'Calle Los Robles', 'Edificio B', '+34 666 767 878',46),
# (47, 'miguelrodriguez@example.com', 'miguel456', 'Miguel', 'Rodríguez', '1991-09-15', 'Avenida Los Pinos', 'Bloque H', '+34 666 878 989',47),
# (48, 'anamartin@example.com', 'ana789', 'Ana', 'Martín', '1983-02-28', 'Calle Las Margaritas', 'Portal 15', '+34 666 989 090',48),
# (49, 'sergiogonzalez@example.com', 'sergio123', 'Sergio', 'González', '1994-07-05', 'Avenida Las Azucenas', 'Nº 55', '+34 666 090 101',49),
# (50, 'luciamartinez@example.com', 'lucia456', 'Lucía', 'Martínez', '1980-10-10', 'Calle Los Lirios', 'Escalera G', '+34 666 101 212',50),
# (51, 'danielgarcia@example.com', 'daniel789', 'Daniel', 'García', '1985-03-25', 'Avenida Las Palmeras', 'Piso 10', '+34 666 212 323',51),
# (52, 'patricialopez@example.com', 'patricia123', 'Patricia', 'López', '1992-08-08', 'Calle Las Orquídeas', 'Apartamento 12', '+34 666 323 434',52),
# (53, 'sergioruiz@example.com', 'sergio789', 'Sergio', 'Ruiz', '1987-01-15', 'Avenida Los Girasoles', 'Nº 60', '+34 666 434 545',53),
# (54, 'elenagonzalez@example.com', 'elena456', 'Elena', 'González', '1982-06-30', 'Calle Las Camelias', 'Portal 17', '+34 666 545 656',54),
# (55, 'carlosrodriguez@example.com', 'carlos789', 'Carlos', 'Rodríguez', '1990-11-12', 'Avenida Las Acacias', 'Bloque I', '+34 666 656 767',55),
# (56, 'laurasanchez@example.com', 'laura123', 'Laura', 'Sánchez', '1984-04-28', 'Calle Los Pinos', 'Edificio C', '+34 666 767 878',56),
# (57, 'pedromartinez@example.com', 'pedro456', 'Pedro', 'Martínez', '1989-09-10', 'Avenida de Los Robles', 'Piso 11', '+34 666 878 989',57),
# (58, 'anaruiz@example.com', 'ana789', 'Ana', 'Ruiz', '1981-12-05', 'Calle La Montaña', 'Bloque J', '+34 666 989 090',58),
# (59, 'javiergarcia@example.com', 'javier123', 'Javier', 'García', '1993-07-20', 'Avenida Las Palmeras', 'Portal 20', '+34 666 090 101',59),
# (60, 'luciamartin@example.com', 'lucia456', 'Lucía', 'Martín', '1986-02-15', 'Calle Las Azucenas', 'Piso 12', '+34 666 101 212',60);
# """

# # executeSQL(sqlTrainers)
# try:
#     cursor.execute("SELECT id, password FROM members_trainer")
#     trainers = cursor.fetchall()
#     for trainer in trainers:
#         trainer_id, trainer_password = trainer
#         hashed_password = hashlib.sha256(trainer_password.encode()).hexdigest()
#         cursor.execute(
#             f"UPDATE members_trainer SET password = '{hashed_password}' WHERE id = {trainer_id}"
#         )
#         db.commit()
#     print("Contraseñas de entrenadores actualizadas")
# except Exception as e:
#     print("Error al actualizar contraseñas:", e)
#     db.rollback()

# db.close()
