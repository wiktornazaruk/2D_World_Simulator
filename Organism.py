from enum import Enum
 
class OrganismType(Enum):
    HUMAN = 0
    WOLF = 1
    SHEEP = 2
    ANTELOPE = 3
    FOX = 4
    TURTLE = 5
    GRASS = 6
    SOWTHISTLE = 7
    GUARANA = 8
    BELLADONNA = 9
    HOGWEED = 10

organism_types = {
    "Human": OrganismType.HUMAN,
    "Wolf": OrganismType.WOLF,
    "Sheep": OrganismType.SHEEP,
    "Antelope": OrganismType.ANTELOPE,
    "Fox": OrganismType.FOX,
    "Turtle": OrganismType.TURTLE,
    "Grass": OrganismType.GRASS,
    "SowThistle": OrganismType.SOWTHISTLE,
    "Guarana": OrganismType.GUARANA,
    "Belladonna": OrganismType.BELLADONNA,
    "Hogweed": OrganismType.HOGWEED
}

organisms = [ 
    "Human",
	"Wolf",
	"Sheep",
	"Antelope",
	"Fox",
	"Turtle",
	"Grass",
	"SowThistle",
	"Guarana",
	"Belladonna",
	"Hogweed" ]

def convert_organism_to_type(organism):
    return organism_types[organism]