# Contenido de la demo Piulet Hostel (Barcelona) (es/ca/en/fr). Hechos de piulethostel.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación doble privada','Dormitorio de 4 camas','Dormitorios de 6 y 8 camas'],'ca':['Habitació doble privada','Dormitori de 4 llits','Dormitoris de 6 i 8 llits'],'en':['Private double room','4-bed dorm','6- and 8-bed dorms'],'fr':['Chambre double privée','Dortoir de 4 lits','Dortoirs de 6 et 8 lits']}
RD={
'es':['Con baño privado, wifi, enchufe de 220v y aire acondicionado.','Cada cama con luz individual, cargador USB y cortina para la privacidad; wifi y aire acondicionado.','Las mismas camas de calidad con luz individual, cargador USB y cortina; wifi y aire acondicionado.'],
'ca':['Amb bany privat, wifi, endoll de 220v i aire condicionat.','Cada llit amb llum individual, carregador USB i cortina per a la privacitat; wifi i aire condicionat.','Els mateixos llits de qualitat amb llum individual, carregador USB i cortina; wifi i aire condicionat.'],
'en':['With private bathroom, wifi, 220v socket and air conditioning.','Each bed with personal light, USB charger and a privacy curtain; wifi and air conditioning.','The same quality beds with personal light, USB charger and curtain; wifi and air conditioning.'],
'fr':['Avec salle de bains privée, wifi, prise 220v et climatisation.','Chaque lit avec lumière individuelle, chargeur USB et rideau d\'intimité ; wifi et climatisation.','Les mêmes lits de qualité avec lumière individuelle, chargeur USB et rideau ; wifi et climatisation.']}
ART={
'hero':('arches',3201,['#f2e9df','#e4c6a4','#b98a5a','#4a5a2f','#2b3519']),
'intro':('hills',3202,['#e5ecd8','#f2e7c6','#f4cf8c','#a3c095','#77a072','#4f7a4c']),
'r1':('columns',3211,['#f1e8de','#f7f0e8','#b8893e','#4a5a2f','#2b3519']),
'r2':('arches',3212,['#efe6dc','#ddbf9c','#ad7f52','#4a5a2f','#2b3519']),
'r3':('columns',3213,['#eee5da','#f6efe6','#c08c40','#53653a','#30401f']),
'g1':('hills',3221,['#e6ecd9','#f1e6c4','#f6cf8a','#a9c19e','#80a085','#587767']),
'g2':('arches',3222,['#f0e7dd','#e0c29f','#b38556','#4a5a2f','#2b3519']),
'g3':('skyline',3223,['#3d4a2c','#e2a160','#f6d59e','#3b482b','#2c3720','#1c2414']),
'g4':('columns',3224,['#f1e8de','#f7f0e8','#b8893e','#4a5a2f','#2b3519']),
'g5':('hills',3225,['#e3ead6','#f0e5c2','#f4cf8c','#9fbf96','#6f9a72','#4d7550']),
'g6':('arches',3226,['#efe6dc','#dbbd99','#a97c50','#4a5a2f','#2b3519'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Piulet Hostel · Hostel pequeño en el Eixample de Barcelona, en Enric Granados',see_rooms='Ver habitaciones',hero_k='Barcelona · Eixample',hero_t='Arquitectura catalana, confort moderno',hero_s='Un hostel pequeño y acogedor en Enric Granados, a 10 min a pie de plaza Catalunya, con terraza llena de plantas.',
 intro_t='Piulet: el canto de los pájaros',intro_p1='Piulet significa el canto de los pájaros en catalán; por eso sus habitaciones llevan nombres de aves locales y la terraza tiene plantas regionales pensadas para que los pájaros se sientan seguros.',
 intro_p2='Camas y colchones de muy buena calidad, cada una con luz propia, cargador USB y cortina. Cocina completa, terraza y equipo de recepción de 9 de la mañana a 11 de la noche.',
 stats=['Eixample','Terraza con plantas','Cocina completa','De 18 a 45 años'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Habitación doble privada y dormitorios de 4, 6 y 8 camas.',
 svcs=['Wifi gratis','Aire acondicionado','Terraza','Cocina completa','Servicio de lavandería','Consigna de equipaje','Luz y cargador USB en cada cama','Arquitectura y diseño catalán'],
 loc_p="Carrer d'Enric Granados, 30 · Barcelona, en el Eixample, a 10 min a pie de plaza Catalunya.",
 chips=['¿Qué habitaciones tiene?','¿Hay límite de edad?','¿A qué hora es el check-in?','¿Cómo se reserva?']),
'ca':dict(title="Piulet Hostel · Hostel petit a l'Eixample de Barcelona, a Enric Granados",see_rooms='Veure habitacions',hero_k='Barcelona · Eixample',hero_t='Arquitectura catalana, confort modern',hero_s='Un hostel petit i acollidor a Enric Granados, a 10 min a peu de plaça Catalunya, amb terrassa plena de plantes.',
 intro_t='Piulet: el cant dels ocells',intro_p1='Piulet vol dir el cant dels ocells; per això les seves habitacions porten noms d\'ocells locals i la terrassa té plantes autòctones pensades perquè els ocells s\'hi sentin segurs.',
 intro_p2='Llits i matalassos de molt bona qualitat, cadascun amb llum pròpia, carregador USB i cortina. Cuina completa, terrassa i equip de recepció de 9 del matí a 11 de la nit.',
 stats=['Eixample','Terrassa amb plantes','Cuina completa','De 18 a 45 anys'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Habitació doble privada i dormitoris de 4, 6 i 8 llits.',
 svcs=['Wifi gratis','Aire condicionat','Terrassa','Cuina completa','Servei de bugaderia','Consigna d\'equipatge','Llum i carregador USB a cada llit','Arquitectura i disseny català'],
 loc_p="Carrer d'Enric Granados, 30 · Barcelona, a l'Eixample, a 10 min a peu de plaça Catalunya.",
 chips=['Quines habitacions té?','Hi ha límit d\'edat?','A quina hora és el check-in?','Com es reserva?']),
'en':dict(title='Piulet Hostel · Small hostel in Barcelona\'s Eixample, on Enric Granados',see_rooms='See the rooms',hero_k='Barcelona · Eixample',hero_t='Catalan architecture, modern comfort',hero_s='A small, cosy hostel on Enric Granados, a 10 min walk from plaza Catalunya, with a terrace full of plants.',
 intro_t='Piulet: the singing of birds',intro_p1='Piulet means the singing of birds in Catalan, so its rooms are named after local birds and the terrace has regional plants that create a safe space for birds.',
 intro_p2='Very good quality beds and mattresses, each with its own light, USB charger and curtain. Full kitchen, terrace and a front desk team from 9am till 11pm.',
 stats=['Eixample','Terrace with plants','Full kitchen','Ages 18 to 45'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='A private double room and 4, 6 and 8-bed dorms.',
 svcs=['Free wifi','Air conditioning','Terrace','Full kitchen','Laundry service','Luggage storage','Light and USB charger at every bed','Catalan design and architecture'],
 loc_p="Carrer d'Enric Granados, 30 · Barcelona, in the Eixample, a 10 min walk from plaza Catalunya.",
 chips=['What rooms does it have?','Is there an age limit?','What time is check-in?','How do I book?']),
'fr':dict(title="Piulet Hostel · Petite auberge dans l'Eixample de Barcelone, rue Enric Granados",see_rooms='Voir les chambres',hero_k='Barcelone · Eixample',hero_t='Architecture catalane, confort moderne',hero_s='Une petite auberge chaleureuse rue Enric Granados, à 10 min à pied de la plaza Catalunya, avec une terrasse pleine de plantes.',
 intro_t='Piulet : le chant des oiseaux',intro_p1='Piulet signifie le chant des oiseaux en catalan ; ses chambres portent donc des noms d\'oiseaux locaux et la terrasse accueille des plantes régionales pour que les oiseaux s\'y sentent en sécurité.',
 intro_p2='Lits et matelas de très bonne qualité, chacun avec lumière individuelle, chargeur USB et rideau. Cuisine équipée, terrasse et équipe d\'accueil de 9 h du matin à 11 h du soir.',
 stats=['Eixample','Terrasse végétalisée','Cuisine équipée','De 18 à 45 ans'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Une chambre double privée et des dortoirs de 4, 6 et 8 lits.',
 svcs=['Wifi gratuit','Climatisation','Terrasse','Cuisine équipée','Service de blanchisserie','Consigne à bagages','Lumière et chargeur USB à chaque lit','Architecture et design catalans'],
 loc_p="Carrer d'Enric Granados, 30 · Barcelone, dans l'Eixample, à 10 min à pied de la plaza Catalunya.",
 chips=['Quelles chambres a-t-il ?','Y a-t-il une limite d\'âge ?','À quelle heure est le check-in ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
R='https://hotels.cloudbeds.com/%s/reservation/of802O'
BOOK=dict(mode='engine',url={l:R%l for l in ('es','ca','en','fr')})
D=dict(name='Piulet Hostel',ac='#4a5a2f',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address="Carrer d'Enric Granados, 30 · Barcelona",phones=['+34 672 224 284'],emails=['hola@piulethostel.com'],maps="Piulet Hostel, Carrer d'Enric Granados 30, Barcelona",t=T)
META=dict(repo='demo-piulet-hostel-barcelona',name='Piulet Hostel',legal_name='GESTIÓ LLÚRIA, S.L. (nombre comercial PIULET HOSTEL)',registry_ids=['CIF B67580050','Registro Mercantil de Barcelona, hoja B-545497'],
 url='https://www.piulethostel.com/',domain='piulethostel.com',municipality='Barcelona',province='Barcelona',sector='hostel en el Eixample',
 read_at='2026-10-29T08:05:00+01:00',created_at='2026-10-29T08:25:00+01:00',built_at='2026-10-29T08:25:00+01:00',audit_date='2026-10-29T07:51:00+01:00',
 rating=dict(value=4.5,coincide=['telefono'],date='2026-10-29T06:56:39+01:00',url='https://www.google.com/maps/place/Piulet+hostel/@41.3903594,2.1592606,17z/data=!4m9!3m8!1s0x12a4a37d87b1d18d:0x2980af7362607d1e!5m2!4m1!1i2!8m2!3d41.3903594!4d2.1592606!16s%2Fg%2F11vyqmq6gt?hl=es&entry=ttu&g_ep=EgoyMDI2MTAyMC4wIKXMDSoASAFQAw%3D%3D'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van a su motor Cloudbeds (hotels.cloudbeds.com/reservation/of802O, el mismo que enlaza su pagina Book Now), con prefijo de idioma. La demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Cómo son las camas?','K02'),('¿Qué servicios tiene?','K03'),('¿A qué hora es el check-in?','K04'),('¿Incluye desayuno?','K05'),('¿Hay límite de edad?','K06'),('¿Dónde está?','K07'),('¿Qué ver cerca?','K08'),('¿Cómo es la terraza?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el correo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una cama libre mañana','K10'),('¿Hay parking?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Com són els llits?','K02'),('Quins serveis té?','K03'),('A quina hora és el check-in?','K04'),('Inclou esmorzar?','K05'),('Hi ha límit d\'edat?','K06'),('On és?','K07'),('Què es pot veure a prop?','K08'),('Com és la terrassa?','K09'),('Com reservo?','K10'),('Quin és el correu?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha un llit lliure demà','K10'),('Hi ha pàrquing?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What are the beds like?','K02'),('What facilities does it have?','K03'),('What time is check-in?','K04'),('Is breakfast included?','K05'),('Is there an age limit?','K06'),('Where is it?','K07'),('What is there to see nearby?','K08'),('What is the terrace like?','K09'),('How do I book?','K10'),('What is the email?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free bed tomorrow','K10'),('Is there parking?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Comment sont les lits ?','K02'),('Quels services propose-t-il ?','K03'),('À quelle heure est le check-in ?','K04'),('Le petit-déjeuner est-il inclus ?','K05'),('Y a-t-il une limite d\'âge ?','K06'),('Où est-ce ?','K07'),('Que voir à proximité ?','K08'),('Comment est la terrasse ?','K09'),('Comment réserver ?','K10'),('Quel est l\'e-mail ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a un lit libre demain','K10'),('Y a-t-il un parking ?',None),('Y a-t-il une piscine ?',None)]}
