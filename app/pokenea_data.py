import random

# Arreglo "quemado" de Pokeneas
POKENEAS = [
    {
        "id": 1,
        "nombre": "El Paisa Legendario",
        "altura": "1.75m",
        "habilidad": "Echar carreta con estilo",
        "imagen": "naranjado.jpg", # Nombre de tu imagen en S3
        "frase_filosofica": "El que madruga, encuentra todo abierto, mijo."
    },
    {
        "id": 2,
        "nombre": "La Montañera Veloz",
        "altura": "1.60m",
        "habilidad": "Bajar lomas sin cansarse",
        "imagen": "negro.jpg", # Nombre de tu imagen en S3
        "frase_filosofica": "Despacio voy, porque de afán no queda sino el cansancio."
    },
    {
        "id": 3,
        "nombre": "El Silletero",
        "altura": "1.80m",
        "habilidad": "Cargar flores con precisión",
        "imagen": "morado.png",
        "frase_filosofica": "Con paciencia y saliva, el elefante se monta en la hormiga."
    },
    {
        "id": 4,
        "nombre": "La Guasca Mística",
        "altura": "1.65m",
        "habilidad": "Adivinar el futuro con arepas",
        "imagen": "rosado.png",
        "frase_filosofica": "La arepa es como la vida: cada mordisco es un nuevo comienzo."
    },
    {
        "id": 5,
        "nombre": "El Enyucado",
        "altura": "1.70m",
        "habilidad": "Resistencia extrema a los chismes",
        "imagen": "gris.jpg",
        "frase_filosofica": "Más vale solo que mal acompañado... pero con café, mejor."
    },
    {
        "id": 6,
        "nombre": "El Chismoso del Balcón",
        "altura": "1.72m",
        "habilidad": "Enterarse de todo sin salir de casa",
        "imagen": "rojo.jpg",
        "frase_filosofica": "El que no oye consejo, no llega a viejo... ni se entera del chisme."
    },
    {
        "id": 7,
        "nombre": "La Fiestera Incansable",
        "altura": "1.68m",
        "habilidad": "Bailar hasta el amanecer sin perder el glamour",
        "imagen": "verde.png",
        "frase_filosofica": "La vida es una fiesta, y yo no me la pierdo por nada."
    },
    {
        "id": 8,
        "nombre": "El Tintero de la Esquina",
        "altura": "1.78m",
        "habilidad": "Preparar el tinto perfecto en cualquier momento",
        "imagen": "amarillo.png",
        "frase_filosofica": "Un buen tinto arregla cualquier problema."
    },
    {
        "id": 9,
        "nombre": "La Comelona de Empanadas",
        "altura": "1.63m",
        "habilidad": "Comer empanadas sin quemarse la lengua",
        "imagen": "cafe.png",
        "frase_filosofica": "Empanada que no se come, se pierde."
    },
    {
        "id": 10,
        "nombre": "El Conductor de Chiva",
        "altura": "1.85m",
        "habilidad": "Maniobrar en cualquier terreno con música a todo volumen",
        "imagen": "azul.jpg",
        "frase_filosofica": "El camino es largo, pero la gozadera es eterna."
    }
]

def get_random_pokenea():
    """Retorna un Pokenea seleccionado de forma aleatoria."""
    return random.choice(POKENEAS)