# Define the Room class.

class Room:
    """
Représente une pièce dans un jeu d'aventure textuel.

Cette classe permet de définir un espace du jeu, avec un nom, une description
et des sorties menant vers d'autres pièces. Elle facilite la navigation dans
l'environnement grâce à ses méthodes de consultation des sorties.

    Attributs
    ---------
    name : str
        Le nom de la pièce.
    description : str
        Description textuelle de l'endroit où se trouve le joueur.
    exits : dict[str, Room]
        Dictionnaire associant une direction (ex : "nord") à une autre pièce Room.

    Méthodes
    --------
    get_exit(direction)
        Retourne la pièce située dans la direction donnée, ou None si elle n'existe pas.
    get_exit_string()
        Retourne une chaîne listant les directions disponibles depuis cette pièce.
    get_long_description()
        Retourne une description détaillée de la pièce et de ses sorties.

    Exceptions
    ----------
    Aucune exception spécifique n'est levée par cette classe.

    Exemples
    --------
    >>> salle = Room("Hall", "dans le hall d'entrée")
    >>> salle.exits["nord"] = Room("Cuisine", "dans la cuisine lumineuse")
    >>> salle.name
    'Hall'
    >>> salle.get_exit("nord").name
    'Cuisine'
    >>> salle.get_exit("sud") is None
    True
    >>> "nord" in salle.get_exit_string()
    True
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
