# Define the Player class.
class Player():

"""
    Représente un joueur dans le jeu d'aventure.

    Cette classe permet de définir le personnage jouable, notamment son nom
    et sa position actuelle dans le monde du jeu. Le joueur peut se déplacer
    entre les différentes pièces grâce à la méthode move.

    Attributs
    ---------
    name : str
        Le nom du joueur.
    current_room : Room | None
        La pièce dans laquelle se trouve actuellement le joueur.

    Méthodes
    --------
    move(direction)
        Déplace le joueur vers la pièce située dans la direction donnée.
        Retourne True si le déplacement a réussi, False sinon.

    Exceptions
    ----------
    KeyError
        Levée si la direction donnée n'existe pas dans les sorties de la pièce.
    
    Exemples
    --------
    >>> p = Player("Quentin")
    >>> hall = Room("Hall", "dans le hall d'entrée")
    >>> cuisine = Room("Cuisine", "dans la cuisine lumineuse")
    >>> hall.exits["nord"] = cuisine
    >>> p.current_room = hall
    >>> p.move("nord")
    True
    >>> p.current_room.name
    'Cuisine'
"""

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    