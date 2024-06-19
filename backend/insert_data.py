import hashlib
import MySQLdb
import os
from django.conf import settings

# Establecer la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# Configurar las configuraciones de Django
settings.configure()
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

shieldsSQL = """
INSERT INTO league_shields (route,team_id) VALUES
('data/img/Shields/Zocas.png',1),
('data/img/Shields/CD_Tenerife.png',2),
('data/img/Shields/CD_Marino.png',3),
('data/img/Shields/Icodense.png',4),
('data/img/Shields/CD_LAGUNA.png',5),
('data/img/Shields/Guia_isora.png',6),
('data/img/Shields/Tejina.png',7),
('data/img/Shields/Union_Sur_Yaiza.png',8),
('data/img/Shields/CD_Buzanada.png',9),
('data/img/Shields/Tacoronte.png',10),
('data/img/Shields/Ibarra.png',11),
('data/img/Shields/Atalaya.png',12),
('data/img/Shields/UD_CRUZ_SANTA.png',13),
('data/img/Shields/Tegueste.png',14),
('data/img/Shields/San_Isidro.png',15),
('data/img/Shields/Zocas.png',16),
('data/img/Shields/CD_Tenerife.png',17),
('data/img/Shields/CD_Marino.png',18),
('data/img/Shields/Icodense.png',19),
('data/img/Shields/CD_LAGUNA.png',20),
('data/img/Shields/Guia_isora.png',21),
('data/img/Shields/Tejina.png',22),
('data/img/Shields/Union_Sur_Yaiza.png',23),
('data/img/Shields/CD_Buzanada.png',24),
('data/img/Shields/Tacoronte.png',25),
('data/img/Shields/Ibarra.png',26),
('data/img/Shields/Atalaya.png',27),
('data/img/Shields/UD_CRUZ_SANTA.png',28),
('data/img/Shields/Tegueste.png',29),
('data/img/Shields/San_Isidro.png',30),
('data/img/Shields/Zocas.png',31),
('data/img/Shields/CD_Tenerife.png',32),
('data/img/Shields/CD_Marino.png',33),
('data/img/Shields/Icodense.png',34),
('data/img/Shields/CD_LAGUNA.png',35),
('data/img/Shields/Guia_isora.png',36),
('data/img/Shields/Tejina.png',37),
('data/img/Shields/Union_Sur_Yaiza.png',38),
('data/img/Shields/CD_Buzanada.png',39),
('data/img/Shields/Tacoronte.png',40),
('data/img/Shields/Ibarra.png',41),
('data/img/Shields/Atalaya.png',42),
('data/img/Shields/UD_CRUZ_SANTA.png',43),
('data/img/Shields/Tegueste.png',44),
('data/img/Shields/San_Isidro.png',45),
('data/img/Shields/Zocas.png',46),
('data/img/Shields/CD_Tenerife.png',47),
('data/img/Shields/CD_Marino.png',48),
('data/img/Shields/Icodense.png',49),
('data/img/Shields/CD_LAGUNA.png',50),
('data/img/Shields/Guia_isora.png',51),
('data/img/Shields/Tejina.png',52),
('data/img/Shields/Union_Sur_Yaiza.png',53),
('data/img/Shields/CD_Buzanada.png',54),
('data/img/Shields/Tacoronte.png',55),
('data/img/Shields/Ibarra.png',56),
('data/img/Shields/Atalaya.png',57),
('data/img/Shields/UD_CRUZ_SANTA.png',58),
('data/img/Shields/Tegueste.png',59),
('data/img/Shields/San_Isidro.png',60);
"""

executeSQL(shieldsSQL)

# sqlUsers = """
# INSERT INTO auth_user (id, password, username, first_name, last_name, email) VALUES
# (1, 'juan123', 'juangarcia@example.com', 'Juan', 'García', 'juangarcia@example.com'),
# (2, 'ana456', 'anarodriguez@example.com', 'Ana', 'Rodríguez', 'anarodriguez@example.com'),
# (3, 'pedro789', 'pedrolopez@example.com', 'Pedro', 'López', 'pedrolopez@example.com'),
# (4, 'maria123', 'mariamartinez@example.com', 'María', 'Martínez', 'mariamartinez@example.com'),
# (5, 'david456', 'davidhernandez@example.com', 'David', 'Hernández', 'davidhernandez@example.com'),
# (6, 'laura789', 'lauraperez@example.com', 'Laura', 'Pérez', 'lauraperez@example.com'),
# (7, 'javier123', 'javiergonzalez@example.com', 'Javier', 'González', 'javiergonzalez@example.com'),
# (8, 'sara456', 'sarasanchez@example.com', 'Sara', 'Sánchez', 'sarasanchez@example.com'),
# (9, 'carlos789', 'carlosfernandez@example.com', 'Carlos', 'Fernández', 'carlosfernandez@example.com'),
# (10, 'elena123', 'elenagomez@example.com', 'Elena', 'Gómez', 'elenagomez@example.com'),
# (11, 'miguel456', 'migueldiaz@example.com', 'Miguel', 'Díaz', 'migueldiaz@example.com'),
# (12, 'carmen789', 'carmenalonso@example.com', 'Carmen', 'Alonso', 'carmenalonso@example.com'),
# (13, 'francisco123', 'franciscomorales@example.com', 'Francisco', 'Morales', 'franciscomorales@example.com'),
# (14, 'isabel456', 'isabeljimenez@example.com', 'Isabel', 'Jiménez', 'isabeljimenez@example.com'),
# (15, 'alejandro789', 'alejandroruiz@example.com', 'Alejandro', 'Ruiz', 'alejandroruiz@example.com'),
# (16, 'luis123', 'luisgomez@example.com', 'Luis', 'Gómez', 'luisgomez@example.com'),
# (17, 'elena456', 'elenarodriguez@example.com', 'Elena', 'Rodríguez', 'elenarodriguez@example.com'),
# (18, 'sergio789', 'sergiofernandez@example.com', 'Sergio', 'Fernández', 'sergiofernandez@example.com'),
# (19, 'lucia123', 'luciagarcia@example.com', 'Lucía', 'García', 'luciagarcia@example.com'),
# (20, 'jorge456', 'jorgeperez@example.com', 'Jorge', 'Pérez', 'jorgeperez@example.com'),
# (21, 'maria789', 'mariafernandez@example.com', 'María', 'Fernández', 'mariafernandez@example.com'),
# (22, 'alberto123', 'albertogomez@example.com', 'Alberto', 'Gómez', 'albertogomez@example.com'),
# (23, 'laura456', 'laurarodriguez@example.com', 'Laura', 'Rodríguez', 'laurarodriguez@example.com'),
# (24, 'pablo789', 'pablofernandez@example.com', 'Pablo', 'Fernández', 'pablofernandez@example.com'),
# (25, 'sandra123', 'sandraruiz@example.com', 'Sandra', 'Ruiz', 'sandraruiz@example.com'),
# (26, 'raul456', 'raulrodriguez@example.com', 'Raúl', 'Rodríguez', 'raulrodriguez@example.com'),
# (27, 'cristina789', 'cristinaperez@example.com', 'Cristina', 'Pérez', 'cristinaperez@example.com'),
# (28, 'juan123', 'juanfernandez@example.com', 'Juan', 'Fernández', 'juanfernandez@example.com'),
# (29, 'rosario456', 'rosariogarcia@example.com', 'Rosario', 'García', 'rosariogarcia@example.com'),
# (30, 'daniel789', 'danielruiz@example.com', 'Daniel', 'Ruiz', 'danielruiz@example.com'),
# (31, 'maria123', 'mariaperez@example.com', 'María', 'Pérez', 'mariaperez@example.com'),
# (32, 'carlos456', 'carlosrodriguez@example.com', 'Carlos', 'Rodríguez', 'carlosrodriguez@example.com'),
# (33, 'luisa789', 'luisaflores@example.com', 'Luisa', 'Flores', 'luisaflores@example.com'),
# (34, 'david123', 'davidsanchez@example.com', 'David', 'Sánchez', 'davidsanchez@example.com'),
# (35, 'patricia456', 'patriciamartinez@example.com', 'Patricia', 'Martínez', 'patriciamartinez@example.com'),
# (36, 'sergio789', 'sergioalvarez@example.com', 'Sergio', 'Álvarez', 'sergioalvarez@example.com'),
# (37, 'lucia123', 'luciamartin@example.com', 'Lucía', 'Martín', 'luciamartin@example.com'),
# (38, 'javier456', 'javierlopez@example.com', 'Javier', 'López', 'javierlopez@example.com'),
# (39, 'maria789', 'mariagarcía@example.com', 'María', 'García', 'mariagarcía@example.com'),
# (40, 'carlos789', 'carlosrodriguez1@example.com', 'Carlos', 'Rodríguez', 'carlosrodriguez1@example.com'),
# (41, 'julia456', 'juliamartinez@example.com', 'Julia', 'Martínez', 'juliamartinez@example.com'),
# (42, 'david789', 'davidjimenez@example.com', 'David', 'Jiménez', 'davidjimenez@example.com'),
# (43, 'laura123', 'lauramartinez@example.com', 'Laura', 'Martínez', 'lauramartinez@example.com'),
# (44, 'alberto456', 'albertoperez@example.com', 'Alberto', 'Pérez', 'albertoperez@example.com'),
# (45, 'lucia789', 'luciagonzalez@example.com', 'Lucía', 'González', 'luciagonzalez@example.com'),
# (46, 'andres123', 'andreslopez@example.com', 'Andrés', 'López', 'andreslopez@example.com'),
# (47, 'miguel456', 'miguelrodriguez@example.com', 'Miguel', 'Rodríguez', 'miguelrodriguez@example.com'),
# (48, 'ana789', 'anamartin@example.com', 'Ana', 'Martín', 'anamartin@example.com'),
# (49, 'sergio123', 'sergiogonzalez@example.com', 'Sergio', 'González', 'sergiogonzalez@example.com'),
# (50, 'lucia456', 'luciamartinez1@example.com', 'Lucía', 'Martín', 'luciamartinez@example.com'),
# (51, 'daniel789', 'danielgarcia@example.com', 'Daniel', 'García', 'danielgarcia@example.com'),
# (52, 'patricia123', 'patricialopez@example.com', 'Patricia', 'López', 'patricialopez@example.com'),
# (53, 'sergio789', 'sergioruiz@example.com', 'Sergio', 'Ruiz', 'sergioruiz@example.com'),
# (54, 'elena456', 'elenagonzalez@example.com', 'Elena', 'González', 'elenagonzalez@example.com'),
# (55, 'carlos789', 'carlosrodriguez3@example.com', 'Carlos', 'Rodríguez', 'carlosrodriguez3@example.com'),
# (56, 'laura123', 'laurasanchez@example.com', 'Laura', 'Sánchez', 'laurasanchez@example.com'),
# (57, 'pedro456', 'pedromartinez@example.com', 'Pedro', 'Martínez', 'pedromartinez@example.com'),
# (58, 'ana789', 'anaruiz@example.com', 'Ana', 'Ruiz', 'anaruiz@example.com'),
# (59, 'javier123', 'javiergarcia@example.com', 'Javier', 'García', 'javiergarcia@example.com'),
# (60, 'lucia456', 'luciamartin2@example.com', 'Lucía', 'Martín', 'luciamartin@example.com');
# """
# executeSQL(sqlUsers)


# try:
#     cursor.execute(
#         "SELECT id, password FROM auth_user WHERE password NOT LIKE 'pbkdf2_sha256%'"
#     )
#     users = cursor.fetchall()
#     for user in users:
#         user_id, password = user
#         # Aplicar make_password para encriptar y formatear correctamente la contraseña
#         hashed_password = make_password(password)
#         cursor.execute(
#             f"UPDATE auth_user SET password = '{hashed_password}' WHERE id = {user_id}"
#         )
#         db.commit()
#     print("Contraseñas de los usuarios actualizadas")
# except Exception as e:
#     print("Error al actualizar contraseñas:", e)
#     db.rollback()

# sqlTrainers = """
# INSERT INTO members_trainer (id, birth, address1, address2, phone, team_id, user_id) VALUES
# (1, '1990-05-15', 'Calle Los Molinos', 'Edificio Atlántico', '+34 666 111 111',1, 1),
# (2, '1985-09-20', 'Avenida Tres de Mayo', 'Bloque A', '+34 666 222 222',2, 2),
# (3, '1988-02-10', 'Calle La Marina', 'Portal 3', '+34 666 333 333',3, 3),
# (4, '1992-11-08', 'Avenida de Anaga', 'Nº 15', '+34 666 444 444',4, 4),
# (5, '1980-07-25', 'Calle San Juan', 'Piso 2', '+34 666 555 555',5, 5),
# (6, '1983-04-30', 'Avenida de Venezuela', 'Apartamento 8', '+34 666 666 666',6, 6),
# (7, '1995-01-12', 'Calle Nuestra Señora de Candelaria', 'Nº 20', '+34 666 777 777',7, 7),
# (8, '1987-08-17', 'Avenida de los Majuelos', 'Escalera B', '+34 666 888 888',8, 8),
# (9, '1991-06-03', 'Calle La Paz', 'Nº 5', '+34 666 999 999',9, 9),
# (10, '1986-03-18', 'Avenida de Los Menceyes', 'Piso 1', '+34 666 101 010',10, 10),
# (11, '1982-12-22', 'Calle San Sebastián', 'Portal 7', '+34 666 111 222',11, 11),
# (12, '1993-10-05', 'Avenida de La Salle', 'Apartamento 12', '+34 666 222 333',12, 12),
# (13, '1984-07-11', 'Calle Santa Úrsula', 'Bloque D', '+34 666 333 444',13, 13),
# (14, '1990-04-28', 'Avenida Venezuela', 'Nº 25', '+34 666 444 555',14, 14),
# (15, '1989-09-14', 'Calle La Libertad', 'Piso 3', '+34 666 555 666',15, 15),
# """

# (16, '1987-06-25', 'Calle Los Pinos', 'Edificio Central', '+34 666 666 666',16, 16),
# (17, '1984-02-14', 'Avenida de Los Robles', 'Bloque B', '+34 666 777 777',17, 17),
# (18, '1990-11-30', 'Calle La Montaña', 'Portal 5', '+34 666 888 888',18, 18),
# (19, '1983-08-12', 'Avenida Las Palmeras', 'Nº 10', '+34 666 999 999',19, 19),
# (20, '1995-03-07', 'Calle Las Rosas', 'Piso 4', '+34 666 101 010',20, 20),
# (21, '1986-09-23', 'Avenida Los Girasoles', 'Escalera C', '+34 666 111 111',21, 21),
# (22, '1981-12-17', 'Calle Los Almendros', 'Apartamento 3', '+34 666 222 222',22, 22),
# (23, '1992-07-03', 'Avenida de Las Flores', 'Nº 30', '+34 666 333 333',23, 23),
# (24, '1988-04-18', 'Calle Las Margaritas', 'Piso 5', '+34 666 444 444',24, 24),
# (25, '1980-10-22', 'Avenida Los Tilos', 'Portal 9', '+34 666 555 555',25, 25),
# (26, '1993-01-05', 'Calle Las Orquídeas', 'Nº 35', '+34 666 666 666',26, 26),
# (27, '1985-05-30', 'Avenida Las Azucenas', 'Bloque E', '+34 666 777 777',27, 27),
# (28, '1982-02-13', 'Calle Las Dalias', 'Apartamento 7', '+34 666 888 888',28, 28),
# (29, '1989-07-28', 'Avenida Las Acacias', 'Piso 6', '+34 666 999 999',29, 29),
# (30, '1991-03-15', 'Calle Los Lirios', 'Escalera D', '+34 666 101 010',30, 30),
# (31, '1984-06-10', 'Calle Las Hortensias', 'Edificio A', '+34 666 202 020',31, 31),
# (32, '1996-02-20', 'Avenida Los Pinos', 'Nº 40', '+34 666 303 030',32, 32),
# (33, '1987-09-05', 'Calle Las Camelias', 'Piso 7', '+34 666 404 040',33, 33),
# (34, '1990-04-01', 'Avenida Las Margaritas', 'Bloque F', '+34 666 505 050',34, 34),
# (35, '1983-11-15', 'Calle Los Girasoles', 'Portal 11', '+34 666 606 060',35, 35),
# (36, '1988-01-30', 'Avenida Las Acacias', 'Apartamento 10', '+34 666 707 070',36, 36),
# (37, '1992-08-25', 'Calle Los Pinos', 'Piso 8', '+34 666 808 080',37, 37),
# (38, '1981-03-10', 'Avenida Las Palmeras', 'Escalera E', '+34 666 909 090',38, 38),
# (39, '1984-10-26', 'Calle Las Azucenas', 'Nº 45', '+34 666 010 101',39, 39),
# (40, '1989-07-12', 'Avenida Los Tilos', 'Bloque G', '+34 666 111 212',40, 40),
# (41, '1993-04-05', 'Calle Las Rosas', 'Apartamento 11', '+34 666 212 323',41, 41),
# (42, '1986-11-20', 'Avenida Las Hortensias', 'Piso 9', '+34 666 323 434',42, 42),
# (43, '1981-06-03', 'Calle Los Lirios', 'Escalera F', '+34 666 434 545',43, 43),
# (44, '1985-01-18', 'Avenida Las Margaritas', 'Nº 50', '+34 666 545 656',44, 44),
# (45, '1990-08-08', 'Calle Las Camelias', 'Portal 13', '+34 666 656 767',45, 45),
# (46, '1988-05-20', 'Calle Los Robles', 'Edificio B', '+34 666 767 878',46, 46),
# (47, '1991-09-15', 'Avenida Los Pinos', 'Bloque H', '+34 666 878 989',47, 47),
# (48, '1983-02-28', 'Calle Las Margaritas', 'Portal 15', '+34 666 989 090',48, 48),
# (49, '1994-07-05', 'Avenida Las Azucenas', 'Nº 55', '+34 666 090 101',49, 49),
# (50, '1980-10-10', 'Calle Los Lirios', 'Escalera G', '+34 666 101 212',50, 50),
# (51, '1985-03-25', 'Avenida Las Palmeras', 'Piso 10', '+34 666 212 323',51, 51),
# (52, '1992-08-08', 'Calle Las Orquídeas', 'Apartamento 12', '+34 666 323 434',52, 52),
# (53, '1987-01-15', 'Avenida Los Girasoles', 'Nº 60', '+34 666 434 545',53, 53),
# (54, '1982-06-30', 'Calle Las Camelias', 'Portal 17', '+34 666 545 656',54, 54),
# (55, '1990-11-12', 'Avenida Las Acacias', 'Bloque I', '+34 666 656 767',55, 55),
# (56, '1984-04-28', 'Calle Los Pinos', 'Edificio C', '+34 666 767 878',56, 56),
# (57, '1989-09-10', 'Avenida de Los Robles', 'Piso 11', '+34 666 878 989',57, 57),
# (58, '1981-12-05', 'Calle La Montaña', 'Bloque J', '+34 666 989 090',58, 58),
# (59, '1993-07-20', 'Avenida Las Palmeras', 'Portal 20', '+34 666 090 101',59, 59),
# (60, '1986-02-15', 'Calle Las Azucenas', 'Piso 12', '+34 666 101 212',60, 60);

# executeSQL(sqlTrainers)

db.close()
