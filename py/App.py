from datetime import datetime

import pymongo


# Conexión con la base de datos
client = pymongo.MongoClient("localhost", 27017)

# Si no está la base de datos creada la crea
db = client.eventos_andalucia

# datos creados para añadir a la coleccion

datos = [
    {
        "titulo": "Feria de Abril de Sevilla",
        "descripcion": "La Feria de Abril de Sevilla es una de las festividades más emblemáticas de Andalucía, donde se disfrutan casetas, sevillanas y corridas de toros.",
        "categoria": "Feria",
        "ubicacion": "Recinto Ferial de Sevilla",
        "fecha": {
			"fechaInicio": "2024-04-14",
			"fechaFin": "2024-04-20"
		},
        "precio": 0,
        "capacidad_maxima": 1000000
    },
    {
        "titulo": "Semana Santa de Málaga",
        "descripcion": "La Semana Santa de Málaga es famosa por sus procesiones con tronos de gran tamaño y belleza, acompañados de bandas de música.",
        "categoria": "Semana Santa",
        "ubicacion": "Calles de Málaga",
        "fecha": {
			"fechaInicio": "2024-03-24",
			"fechaFin": "2024-03-31"
		},
        "precio": 0,
        "capacidad_maxima": 300000
    },
    {
        "titulo": "Carreras de Caballos de Sanlúcar de Barrameda",
        "descripcion": "Este evento se celebra en las playas de Sanlúcar y es uno de los espectáculos ecuestres más antiguos de España.",
        "categoria": "Carrera de Caballos",
        "ubicacion": "Playa de Sanlúcar de Barrameda",
        "fecha": {
			"fechaInicio": "2024-08-28",
			"fechaFin": "2024-08-30"
		},
        "precio": 0,
        "capacidad_maxima": 40000
    },
    {
        "titulo": "Fiestas Colombinas de Huelva",
        "descripcion": "Las Fiestas Colombinas celebran la partida de Cristóbal Colón hacia América con actividades culturales y festivas.",
        "categoria": "Fiesta Tradicional",
        "ubicacion": "Recinto Colombino de Huelva",
        "fecha": {
			"fechaInicio": "2024-07-29",
			"fechaFin": "2024-08-05"
		},
        "precio": 0,
        "capacidad_maxima": 200000
    },
    {
        "titulo": "Cascamorras de Baza y Guadix",
        "descripcion": "Una celebración única donde los participantes se embadurnan de pintura para capturar al Cascamorras.",
        "categoria": "Fiesta Tradicional",
        "ubicacion": "Calles de Baza",
        "fecha": {
			"fechaInicio": "2024-07-13",
			"fechaFin": "2024-07-21"
		},
        "precio": 0,
        "capacidad_maxima": 30000
    },
    {
        "titulo": "Eternal Running de Iznájar",
        "descripcion": "Una carrera extrema con obstáculos que desafía a los participantes a superarse a sí mismos.",
        "categoria": "Carrera",
        "ubicacion": "Playa de Valdearenas",
        "fecha": {
			"fechaInicio": "2024-10-20",
			"fechaFin": "2024-10-20"
		},
        "precio": 20,
        "capacidad_maxima": 2000
    },
    {
        "titulo": "Fiesta del Ajoblanco, Almáchar",
        "descripcion": "El primer sábado de septiembre, Almáchar celebra la Fiesta del Ajoblanco, una sopa fría tradicional.",
        "categoria": "Fiesta Gastronómica",
        "ubicacion": "Calles de Almáchar",
        "fecha": {
			"fechaInicio": "2024-09-07",
			"fechaFin": "2024-09-07"
		},
        "precio": 0,
        "capacidad_maxima": 10000
    },
    {
        "titulo": "Feria de la Vendimia Palma del Condado",
        "descripcion": "En septiembre se celebra la Real Feria de La Palma del Condado, una de las más antiguas de Andalucía.",
        "categoria": "Feria",
        "ubicacion": "Plaza de España de Palma del Condado",
        "fecha": {
			"fechaInicio": "2024-09-19",
			"fechaFin": "2024-09-21"
		},
        "precio": 0,
        "capacidad_maxima": 15000
    },
	{
        "titulo": "Romería de la Virgen de la Cabeza",
        "descripcion": "Una de las romerías más antiguas de España, con miles de peregrinos que suben al Santuario del Cerro del Cabezo.",
        "categoria": "Romería de Cabeza",
        "ubicacion": "Santuario El Cerro del Cabezo",
        "fecha": {
			"fechaInicio": "2024-04-25",
			"fechaFin": "2024-04-28"
		},
        "precio": 0,
        "capacidad_maxima": 800000
    },
    {
        "titulo": "Feria de las Maravillas de Maro",
        "descripcion": "Maro celebra su feria y fiestas patronales en torno al 8 de septiembre, en honor a la Virgen de las Maravillas.",
        "categoria": "Feria",
        "ubicacion": "Ferial de Maro",
        "fecha": {
			"fechaInicio": "2024-10-09",
			"fechaFin": "2024-10-13"
		},
        "precio": 0,
        "capacidad_maxima": 8000
    },
    {
        "titulo": "Día de la Sopa Perota",
        "descripcion": "A principios de octubre, Álora celebra el Día de la Sopa Perota, una fiesta para promocionar productos típicos de la zona.",
        "categoria": "Fiesta Gastronómica",
        "ubicacion": "Plaza Baja de la Despedía de Álora",
        "fecha": {
			"fechaInicio": "2024-10-05",
			"fechaFin": "2024-10-05"
		},
        "precio": 0,
        "capacidad_maxima": 12000
    },
    {
        "titulo": "Feria de Artesanía de El Granado",
        "descripcion": "El Granado acoge en octubre su Feria de Artesanía, con expositores de diversos oficios artesanales.",
        "categoria": "Feria",
        "ubicacion": "Plaza de España de Granado",
        "fecha": {
			"fechaInicio": "2024-10-11",
			"fechaFin": "2024-10-16"
		},
        "precio": 5,
        "capacidad_maxima": 5000
    },
    {
        "titulo": "Feria Regional del Jamón, Aracena",
        "descripcion": "Durante el tercer fin de semana de octubre, se celebra la Feria Regional del Jamón y del Cerdo Ibérico en Aracena.",
        "categoria": "Feria Gastronómica",
        "ubicacion": "Pabellón ferial de Aracena",
        "fecha": {
			"fechaInicio": "2024-10-17",
			"fechaFin": "2024-10-21"
		},
        "precio": 0,
        "capacidad_maxima": 20000
    },
    {
        "titulo": "Fiestas Patronales de Torrox",
        "descripcion": "El primer fin de semana de octubre se celebra la Feria de Torrox en honor a sus patronos, la Virgen de las Nieves y San Roque.",
        "categoria": "Feria",
        "ubicacion": "Plaza de la Constitución de Torrox",
        "fecha": {
			"fechaInicio": "2024-10-03",
			"fechaFin": "2024-10-06"
		},
        "precio": 0,
        "capacidad_maxima": 15000
    },
    {
        "titulo": "Fiesta de los Patios, Córdoba",
        "descripcion": "Durante dos semanas en mayo, Córdoba celebra la Fiesta de los Patios, donde se abren al público los patios de casas particulares decorados con flores.",
        "categoria": "Fiesta Tradicional",
        "ubicacion": "Patios de Córdoba",
        "fecha": {
			"fechaInicio": "2024-05-1",
			"fechaFin": "2024-05-15"
		},
        "precio": 0,
        "capacidad_maxima": 50000
    },
    
    {
        "titulo": "Festival de Música y Danza de Granada",
        "descripcion": "El Festival de Música y Danza de Granada es uno de los eventos culturales más importantes de la ciudad, con conciertos y actuaciones de danza.",
        "categoria": "Festival",
        "ubicacion": "Edificio Corral del Carbón",
        "fecha": {
			"fechaInicio": "2024-06-20",
			"fechaFin": "2024-06-22"
		},
        "precio": 0,
        "capacidad_maxima": 30000
    },
    {
        "titulo": "Festival de la Guitarra de Córdoba",
        "descripcion": "Un evento anual que reúne a los mejores guitarristas del mundo para actuaciones y talleres.",
        "categoria": "Festival",
        "ubicacion": "Teatro Góngora de Córdoba",
        "fecha": {
			"fechaInicio": "2024-07-01",
			"fechaFin": "2024-07-03"
		},
        "precio": 25,
        "capacidad_maxima": 2000
    },
    {
        "titulo": "Noches en los Jardines del Alcázar, Sevilla",
        "descripcion": "Conciertos al aire libre en el magnífico entorno de los jardines del Real Alcázar.",
        "categoria": "Concierto",
        "ubicacion": "Real Alcázar de Sevilla",
        "fecha": {
			"fechaInicio": "2024-07-15",
			"fechaFin": "2024-07-15"
		},
        "precio": 15,
        "capacidad_maxima": 500
    },
    {
        "titulo": "Festival de Flamenco de Jerez",
        "descripcion": "Un festival que celebra el arte del flamenco con actuaciones de canto, baile y guitarra.",
        "categoria": "Festival",
        "ubicacion": "Teatro Villamarta",
        "fecha": {
			"fechaInicio": "2024-02-20",
			"fechaFin": "2024-02-22"
		},
        "precio": 30,
        "capacidad_maxima": 1000
    },
    {
        "titulo": "Feria de San Lucas",
        "descripcion": "La última gran feria de Andalucía en el año, con casetas, atracciones y eventos taurinos.",
        "categoria": "Feria",
        "ubicacion": "Recinto Ferial de Jaén",
        "fecha": {
			"fechaInicio": "2024-08-12",
			"fechaFin": "2024-08-22"
		},
        "precio": 0,
        "capacidad_maxima": 50000
    },
    {
        "titulo": "Noche en Blanco en Málaga",
        "descripcion": "Una noche donde los museos, monumentos y espacios culturales de Málaga abren sus puertas al público con actividades especiales.",
        "categoria": "Evento Cultural",
        "ubicacion": "Calles de Málaga",
        "fecha": {
			"fechaInicio": "2024-05-12",
			"fechaFin": "2024-05-12"
		},
        "precio": 0,
        "capacidad_maxima": 30000
    },
    {
        "titulo": "Fiesta de la Primavera de Córdoba",
        "descripcion": "Celebración de la llegada de la primavera con eventos y actividades en toda la ciudad.",
        "categoria": "Fiesta Tradicional",
        "ubicacion": "Calles de Córdoba",
        "fecha": {
			"fechaInicio": "2024-03-21",
			"fechaFin": "2024-03-22"
		},
        "precio": 0,
        "capacidad_maxima": 20000
    },
    {
        "titulo": "Festival Internacional de Teatro Clásico de Almagro",
        "descripcion": "Un festival que presenta obras de teatro clásico en escenarios históricos.",
        "categoria": "Festival",
        "ubicacion": "Corral de Comdedias Plaza Mayor",
        "fecha": {
			"fechaInicio": "2024-07-05",
			"fechaFin": "2024-07-07"
		},
        "precio": 20,
        "capacidad_maxima": 1500
    },
    {
        "titulo": "Festival de Jazz de Granada",
        "descripcion": "Uno de los festivales de jazz más importantes de España, con actuaciones de músicos internacionales.",
        "categoria": "Festival",
        "ubicacion": "Edificio Corral del Carbón",
        "fecha": {
			"fechaInicio": "2024-11-02",
			"fechaFin": "2024-11-04"
		},
        "precio": 30,
        "capacidad_maxima": 3000
    },
    {
        "titulo": "Festival de Cine Europeo de Sevilla",
        "descripcion": "Un evento que celebra el cine europeo con proyecciones, talleres y encuentros con cineastas.",
        "categoria": "Festival",
        "ubicacion": "Cinesur Nervión Plaza",
        "fecha": {
			"fechaInicio": "2024-11-07",
			"fechaFin": "2024-11-10"
		},
        "precio": 3,
        "capacidad_maxima": 10000
    },
    {
        "titulo": "Fiesta de la Virgen del Carmen",
        "descripcion": "El 16 de julio, Málaga celebra la Fiesta de la Virgen del Carmen, patrona de los marineros, con procesiones marítimas.",
        "categoria": "Fiesta Religiosa",
        "ubicacion": "Calles de Málaga",
        "fecha": {
			"fechaInicio": "2024-08-16",
			"fechaFin": "2024-08-16"
		},
        "precio": 0,
        "capacidad_maxima": 20000
    },
    {
        "titulo": "Feria del Caballo de Jerez",
        "descripcion": "Un evento que celebra el mundo ecuestre con exhibiciones, competiciones y actividades relacionadas con los caballos.",
        "categoria": "Feria",
        "ubicacion": "Parque González Hontoria",
        "fecha": {
			"fechaInicio": "2024-05-04",
			"fechaFin": "2024-05-11"
		},
        "precio": 0,
        "capacidad_maxima": 60000
    },
    {
        "titulo": "Festival de la Luna Mora, Guaro",
        "descripcion": "Una celebración nocturna en el pueblo de Guaro con miles de velas iluminando las calles, música y actividades culturales.",
        "categoria": "Festival",
        "ubicacion": "Auditorio de la Luna Mora",
        "fecha": {
			"fechaInicio": "2024-09-06",
			"fechaFin": "2024-09-06"
		},
        "precio": 0,
        "capacidad_maxima": 15000
    },
    {
        "titulo": "Feria de la Manzanilla Sanlúcar",
        "descripcion": "Una feria dedicada al vino manzanilla, con degustaciones, actuaciones y actividades culturales.",
        "categoria": "Feria",
        "ubicacion": "Real de la Calzada",
        "fecha": {
			"fechaInicio": "2024-05-28",
			"fechaFin": "2024-06-02"
		},
        "precio": 0,
        "capacidad_maxima": 30000
    },
    {
        "titulo": "Fiesta de la Virgen de las Angustias",
        "descripcion": "Una fiesta religiosa en honor a la Virgen de las Angustias, patrona de Granada, con procesiones y eventos culturales.",
        "categoria": "Fiesta Religiosa",
        "ubicacion": "Calles de Granada",
        "fecha": {
			"fechaInicio": "2024-09-15",
			"fechaFin": "2024-09-15"
		},
        "precio": 0,
        "capacidad_maxima": 50000
    },
	{
		"titulo": "Semana Santa de Sevilla",
		"descripcion": "La Semana Santa de Sevilla es una de las más famosas del mundo, con procesiones de gran solemnidad y belleza.",
		"categoria": "Semana Santa",
		"ubicacion": "Calles de Sevilla",
		"fecha": {
			"fechaInicio": "2024-04-24",
			"fechaFin": "2024-04-31"
		},
		"precio": 0,
		"capacidad_maxima": 500000
	},
	{
		"titulo": "Semana Santa de Córdoba",
		"descripcion": "La Semana Santa de Córdoba es conocida por la sobriedad y elegancia de sus procesiones, destacando la figura del Cristo de los Faroles.",
		"categoria": "Semana Santa",
		"ubicacion": "Calles de Córdoba",
		"fecha": {
			"fechaInicio": "2024-03-24",
			"fechaFin": "2024-03-31"
		},
		"precio": 0,
		"capacidad_maxima": 200000
	},
	{
		"titulo": "Semana Santa de Granada",
		"descripcion": "La Semana Santa de Granada se caracteriza por la intensidad de sus celebraciones religiosas y la majestuosidad de sus pasos procesionales.",
		"categoria": "Semana Santa",
		"ubicacion": "Calles de Granada",
		"fecha": {
			"fechaInicio": "2024-03-24",
			"fechaFin": "2024-03-31"
		},
		"precio": 0,
		"capacidad_maxima": 150000
	},
	{
		"titulo": "Semana Santa de Almería",
		"descripcion": "La Semana Santa de Almería destaca por la participación popular y el fervor religioso de sus procesiones.",
		"categoria": "Semana Santa",
		"ubicacion": "Calles de Almería",
		"fecha": {
			"fechaInicio": "2024-03-24",
			"fechaFin": "2024-03-31"
		},
		"precio": 0,
		"capacidad_maxima": 100000
	},
	{
		"titulo": "Semana Santa de Jaén",
		"descripcion": "La Semana Santa de Jaén se distingue por la solemnidad de sus procesiones y la presencia de imágenes de gran valor artístico.",
		"categoria": "Semana Santa",
		"ubicacion": "Calles de Jaén",
		"fecha": {
			"fechaInicio": "2024-03-24",
			"fechaFin": "2024-03-31"
		},
		"precio": 0,
		"capacidad_maxima": 70000
	},
	{
		"titulo": "Concurso Oficial de Agrupaciones Carnavalescas (COAC)",
		"descripcion": "El COAC es el evento principal del Carnaval de Cádiz, donde se presentan chirigotas, comparsas, coros y cuartetos en competencia por el primer premio.",
		"categoria": "Carnaval",
		"ubicacion": "Gran Teatro Falla, Cádiz",
		"fecha": {
			"fechaInicio": "2024-02-03",
			"fechaFin": "2024-02-23"
		},
		"precio": 100,
		"capacidad_maxima": 10000
	},
	{
		"titulo": "Gran Cabalgata del Carnaval",
		"descripcion": "La Gran Cabalgata es uno de los eventos más esperados del Carnaval de Cádiz, con carrozas, comparsas y mucho humor que recorren las calles de la ciudad.",
		"categoria": "Carnaval",
		"ubicacion": "Calles de Cádiz",
		"fecha": {
			"fechaInicio": "2024-02-10",
			"fechaFin": "2024-02-10"
		},
		"precio": 0,
		"capacidad_maxima": 50000
	},
	{
		"titulo": "Carrusel de Coros",
		"descripcion": "El Carrusel de Coros es un evento donde diferentes coros del Carnaval de Cádiz ofrecen pequeñas actuaciones en diversos puntos de la ciudad, creando un ambiente festivo.",
		"categoria": "Carnaval",
		"ubicacion": "Calles de Cádiz",
		"fecha": {
			"fechaInicio": "2024-02-05",
			"fechaFin": "2024-02-25"
		},
		"precio": 0,
		"capacidad_maxima": 20000
	},
	{
		"titulo": "Pregón del Carnaval",
		"descripcion": "El Pregón marca el inicio oficial del Carnaval de Cádiz, con un discurso inaugural lleno de humor y crítica social.",
		"categoria": "Carnaval",
		"ubicacion": "Plaza de San Antonio, Cádiz",
		"fecha": {
			"fechaInicio": "2024-02-08",
			"fechaFin": "2024-02-08"
		},
		"precio": 0,
		"capacidad_maxima": 30000
	},
	{
		"titulo": "Entierro de la Sardina",
		"descripcion": "El Entierro de la Sardina es una ceremonia simbólica que marca el final del Carnaval de Cádiz, donde se despide a la sardina entre lamentos y bromas.",
		"categoria": "Carnaval",
		"ubicacion": "Playa de la Caleta, Cádiz",
		"fecha": {
			"fechaInicio": "2024-02-25",
			"fechaFin": "2024-02-25"
		},
		"precio": 0,
		"capacidad_maxima": 40000
	},
	{
		"titulo": "Llegada de Hermandades al Rocío",
		"descripcion": "Las Hermandades arriban a la aldea del Rocío en un ambiente de jubilo y fervor, acompañadas por miles de peregrinos.",
		"categoria": "Romería del Rocío",
		"ubicacion": "Aldea del Rocío",
		"fecha": {
			"fechaInicio": "2024-05-20",
			"fechaFin": "2024-05-20"
		},
		"precio": 0,
		"capacidad_maxima": 1200000
	},
	{
		"titulo": "Misa en la Ermita del Rocío",
		"descripcion": "Se celebra una emotiva misa en la Ermita del Rocío, donde los peregrinos veneran a la Virgen del Rocío.",
		"categoria": "Romería del Rocío",
		"ubicacion": "Ermita del Rocío, Almonte, Huelva",
		"fecha": {
			"fechaInicio": "2024-05-21",
			"fechaFin": "2024-05-21"
		},
		"precio": 0,
		"capacidad_maxima": 150000
	},
		{
		"titulo": "Salida de la Virgen del Rocío por las calles de Almonte",
		"descripcion": "Procesión de la Virgen del Rocío luciendo sus galas de Reina, con estreno de nuevo paso, por las calles de Almonte en un evento esperado por todos los rocieros.",
		"categoria": "Romería del Rocío",
		"ubicacion": "Calles de Almonte",
		"fecha": {
			"fechaInicio": "2024-05-22",
			"fechaFin": "2024-05-22"
		},
		"precio": 0,
		"capacidad_maxima": 500000
	},
	{
		"titulo": "Regreso de la Virgen del Rocío al Santuario",
		"descripcion": "La Patrona de Almonte regresa a su Santuario tras dos años de espera debido a la pandemia. La procesión por el camino de Los Llanos será un momento emocionante para todos los rocieros.",
		"categoria": "Romería del Rocío",
		"ubicacion": "Calles de Almonte",
		"fecha": {
			"fechaInicio": "2022-05-29",
			"fechaFin": "2022-05-29"
		},
		"precio": 0,
		"capacidad_maxima": 500000
	},
		{
		"titulo": "Inicio oficial de la Romería del Rocío 2022",
		"descripcion": "Comienza la Romería del Rocío con la presentación de hermandades, marcando el inicio de una celebración llena de devoción y alegría.",
		"categoria": "Romería del Rocío",
		"ubicacion": "Aldea del Rocío",
		"fecha": {
			"fechaInicio": "2022-06-03",
			"fechaFin": "2022-06-03"
		},
		"precio": 0,
		"capacidad_maxima": 1000000
	},
	{
		"titulo": "Misa de Pentecostés y Rosario por las calles de la aldea",
		"descripcion": "La Misa de Pentecostés es un momento especial durante la Romería, seguida del Rosario por las calles de la aldea, llenando el ambiente con devoción y música.",
		"categoria": "Romería del Rocío",
		"ubicacion": "Aldea del Rocío",
		"fecha": {
			"fechaInicio": "2022-06-05",
			"fechaFin": "2022-06-05"
		},
		"precio": 0,
		"capacidad_maxima": 1200000
	}
]

# inserta os documentos, si no está la coleccion creada la crea
db.eventos.insert_many(datos)




# Funciones de la aplicación luego llamadas desde el menú

def alta():
    while True:
        print("\n  ----- ALTA DE EVNTO ------")
        print("  Introduce los siguientes datos")

        titulo = input("    Título: ")
        descripcion = input("    Descripción: ")
        categoria = input("    Categoría: ")
        ubicacion = input("    Ubicación: ")
        fechaInicio = input("    Fecha de inicio (YYYY-MM-DD): ")
        fechaFin = input("    Fecha de fin (YYYY-MM-DD): ")
        precio = float(input("    Precio: "))
        capacidad_maxima = int(input("    Capacidad máxima: "))

        evento = {
            "titulo": titulo,
            "descripcion": descripcion,
            "categoria": categoria,
            "ubicacion": ubicacion,
            "fecha": {
                "fechaInicio": datetime.strptime(fechaInicio, "%Y-%m-%d"),
                "fechaFin": datetime.strptime(fechaFin, "%Y-%m-%d")
            },
            "precio": precio,
            "capacidad_maxima": capacidad_maxima
        }
        db.eventos.insert_one(evento)

        print("  ------------------------------")
        print("  Insertando documento ...")

        masDocumentos = input("\n  ¿Desea dar de alta otro evento (y/n): ")
        if masDocumentos.lower() != "y":
            break



def actualiza():
    while True:
        print("\n  -------- ACTUALIZACIÓN DE EVENTO --------")
        titulo = input("  Introduce el título del evento: ")

        evento = db.eventos.find_one({"titulo": titulo})

        if evento:

            # Solicitar nuevos datos

            print("\n  Para NO actualizar dejar en BLANCO")
            print("  ----------------------------------")
            nueva_descripcion = input(f"    Nueva descripción [{evento.get('descripcion')}]: ") or evento.get('descripcion')
            nueva_categoria = input(f"    Nueva categoría [{evento.get('categoria')}]: ") or evento.get('categoria')
            nueva_ubicacion = input(f"    Nueva ubicación [{evento.get('ubicacion')}]: ") or evento.get('ubicacion')
            nueva_fecha_inicio_input = input(
                f"    Nueva fecha de inicio (YYYY-MM-DD) [{evento.get('fecha', {}).get('fechaInicio')}]: ")
            nueva_fecha_inicio = datetime.strptime(nueva_fecha_inicio_input, '%Y-%m-%d') if nueva_fecha_inicio_input else evento.get('fecha', {}).get('fechaInicio')
            nueva_fecha_fin_input = input(
                f"    Nueva fecha de fin (YYYY-MM-DD) [{evento.get('fecha', {}).get('fechaFin')}]: ")
            nueva_fecha_fin = datetime.strptime(nueva_fecha_fin_input, '%Y-%m-%d') if nueva_fecha_fin_input else evento.get('fecha', {}).get('fechaFin')
            nuevo_precio = input(f"    Nuevo precio [{evento.get('precio')}]: ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else evento.get('precio')
            nueva_capacidad_maxima = input(f"    Nueva capacidad máxima [{evento.get('capacidad_maxima')}]: ")
            nueva_capacidad_maxima = int(nueva_capacidad_maxima) if nueva_capacidad_maxima else evento.get('capacidad_maxima')

            documento_act = {
                "descripcion": nueva_descripcion,
                "categoria": nueva_categoria,
                "ubicacion": nueva_ubicacion,
                "fecha": {
                    "fechaInicio": nueva_fecha_inicio,
                    "fechaFin": nueva_fecha_fin
                },
                "precio": nuevo_precio,
                "capacidad_maxima": nueva_capacidad_maxima
            }

            db.eventos.update_one({"titulo": evento["titulo"]}, {"$set": documento_act})
            print("  ------------------------------------")
            print("  Actualizando evento ...")

        else:
            print("\n  -------  ¡EVENTO NO ENCONTRADO!  --------")

        masDocumentos = input("\n  ¿Desea actualizar otro evento (y/n): ")
        if masDocumentos.lower() != "y":
            break




def eliminacionUno():
    while True:
        print("\n  -------- ELIMINACIÓN DE EVENTO ---------")
        titulo = input("  Introduce el titulo del evento: ")

        evento = db.eventos.find_one({"titulo": titulo})

        if evento:
            print("  Evento encontrado:")
            print("  Título:", evento["titulo"])
            print("  Descripción:", evento["descripcion"])
            print("  Categoría:", evento["categoria"])
            print("  Ubicación:", evento["ubicacion"])
            print("  Fecha de inicio:", evento["fecha"]["fechaInicio"].strftime("%Y-%m-%d"))
            print("  Fecha de fin:", evento["fecha"]["fechaFin"].strftime("%Y-%m-%d"))
            print("  Precio:", evento["precio"])
            print("  Capacidad máxima:", evento["capacidad_maxima"])

            confirmacion = input("\n  ¿Está seguro de que desea eliminar este evento? (y/n): ").lower()
            if confirmacion == 'y':
                db.eventos.delete_one({"titulo": titulo})
                print("  -------------------------------------------------------")
                print("  Eliminando evento...")
            else:
                print("  -------------------------------------------------------")
                print("  Eliminación cancelada.")
        else:
            print("\n  ¡EVENTO NO ENCONTRADO!")

        mas_eventos = input("\n  ¿Desea eliminar otro evento (y/n): ")
        if mas_eventos.lower() != "y":
            break


def eliminarTodos():
    print("\n  ----- ELIMINACIÓN DE TODOS LOS EVENTOS -----")
    print("\n  ¿Está seguro de que desea eliminar todos los eventos? (y/n): ")
    confirmacion = input().lower()

    if confirmacion == 'y':
        db.eventos.delete_many({})
        print("  --------------------------------------------------------")
        print("  Eliminando todos los eventos...")
    else:
        print("  --------------------------------------------------------")
        print("  Eliminación cancelada.")



def eliminarColeccion():
    print("\n  ----------- ELIMINACIÓN DE LA COLECCIÓN DE EVENTOS -----------")
    print("\n  ¿Está seguro de que desea eliminar la colección de eventos? (y/n): ")
    confirmacion = input().lower()

    if confirmacion == 'y':
        db.eventos.drop()
        print("  ---------------------------------------------------------------")
        print("  Eliminando la colección de eventos...")
    else:
        print("  ---------------------------------------------------------------")
        print("  Eliminación cancelada.")





# funcion auxiliar imprimir documentos con formato
def printearDocumento(documento):
    # para acceder a los valores del diccionario usamos get
    # ya que si accedemos usando [ ] y no existe nos da un error
    # y en mongodb no tienen que tener todos los documentos los mismos campos
    print("    Título:", documento.get("titulo"))
    print("    Descripción:", documento.get("descripcion"))
    print("    Categoría:", documento.get("categoria"))
    print("    Ubicación:", documento.get("ubicacion"))
    print("    Fecha de inicio:", documento.get("fecha").get("fechaInicio"))
    print("    Fecha de fin:", documento.get("fecha").get("fechaFin"))
    print("    Precio:", documento.get("precio"))
    print("    Capacidad máxima:", documento.get("capacidad_maxima"))
    print("  -------------------------------")



def mostrarTodos():
    print("\n  ----- MOSTRANDO TODOS LOS EVENTOS -----\n")

    # los vamos a ordenar por orden alfabetico del nombre
    documentos = db.eventos.find().sort("titulo", 1)

    for documento in documentos:
        printearDocumento(documento)



from datetime import datetime

def busqueda():
    while True:
        print("\n  ----------------------------------- FILTRADO DE EVENTOS --------------------------------")
        print("    1. Buscar todos los eventos de Semana Santa en Andalucía")
        print("    2. Encontrar todos los eventos de Carnavales en una ciudad específica de Andalucía")
        print("    3. Buscar eventos de la Romería del Rocío que tendrán lugar este año")
        print("    4. Encontrar ferias que están ocurriendo en una fecha específica en Andalucía")
        print("    5. Buscar eventos gratuitos en una ubicación específica de Andalucía")
        print("    6. Festivales que cuesten entre 10 y 30 euros")
        print("    7. Volver al menú principal")
        print("  -----------------------------------------------------------------------------------------")

        opcion = input("    Elige una opción: ")

        if opcion == '1':
            resultados = db.eventos.find({"categoria": "Semana Santa"})
            print("\n  Resultados de la búsqueda:")
            for resultado in resultados:
                printearDocumento(resultado)

        elif opcion == '2':
            ciudad = input("    Ciudad: ")
            resultados = db.eventos.aggregate([
                {"$lookup": {
                    "from": "ubicaciones",
                    "localField": "ubicacion",
                    "foreignField": "ubicacion",
                    "as": "ubicacion_info"
                }},
                {"$match": {"ubicacion_info.ciudad": ciudad, "categoria": "Carnaval"}}
            ])
            print("\n  Resultados de la búsqueda:")
            for resultado in resultados:
                printearDocumento(resultado)

        elif opcion == '3':
            resultados = db.eventos.find({
                "categoria": "Romería del Rocío",
                "fecha.fechaInicio": {"$gte": datetime(2024, 1, 1), "$lte": datetime(2024, 12, 31)}
            })
            print("\n  Resultados de la búsqueda:")
            for resultado in resultados:
                printearDocumento(resultado)

        elif opcion == '4':
            fecha = input("    Fecha (YYYY-MM-DD): ")
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
            resultados = db.eventos.find({
                "categoria": "Feria",
                "fecha.fechaInicio": {"$lte": fecha_dt},
                "fecha.fechaFin": {"$gte": fecha_dt}
            })
            print("\n  Resultados de la búsqueda:")
            for resultado in resultados:
                printearDocumento(resultado)

        elif opcion == '5':
            ciudad = input("    Ciudad: ")
            resultados = db.eventos.aggregate([
                {"$lookup": {
                    "from": "ubicaciones",
                    "localField": "ubicacion",
                    "foreignField": "ubicacion",
                    "as": "ubicacion_info"
                }},
                {"$match": {"ubicacion_info.ciudad": ciudad, "precio": 0}}
            ])
            print("\n  Resultados de la búsqueda:")
            for resultado in resultados:
                printearDocumento(resultado)

        elif opcion == '6':
            resultados = db.eventos.find({"categoria": "Festival", "precio": {"$gte": 10, "$lte": 30}})
            print("\n  Resultados de la búsqueda:")
            for resultado in resultados:
                printearDocumento(resultado)

        elif opcion == '7':
            break
        else:
            print("  Opción no válida. Inténtalo de nuevo.")



# Implementación MENU que se repite hasta que se elige la opción de salida
while True:

    # Menú gráfico de usuario
    print("\n\n########################################################")
    print("##                       MENÚ                         ##")
    print("########################################################")
    print("##                                                    ##")
    print("##  1. Alta de eventos                                ##")
    print("##  2. Actualización de eventos                       ##")
    print("##  3. Eliminación de eventos                         ##")
    print("##  4. Mostrar todos los eventos de una colección     ##")
    print("##  5. Filtrado de eventos                            ##")
    print("##  6. Eliminación total de eventos de colección      ##")
    print("##  7. Elimación de coleccion                         ##")
    print("##  8. SALIR                                          ##")
    print("##                                                    ##")
    print("########################################################")

    # Se pide al usuario que elija una opción del menú
    opt = input("  Elige una opción: ")

    # Estructura de control del menu que llamará a los métodos de las respectivas funciones
    if opt == "1":
        alta()
    elif opt == "2":
        actualiza()
    elif opt == "3":
        eliminacionUno()
    elif opt == "4":
        mostrarTodos()
    elif opt == "5":
        busqueda()
    elif opt == "6":
        eliminarTodos()
    elif opt == "7":
        eliminarColeccion()
    elif opt == "8":
        print("  Saliendo ...")
        break
    else:
        print(" ¡OPCIÓN INCORRECTA!")

