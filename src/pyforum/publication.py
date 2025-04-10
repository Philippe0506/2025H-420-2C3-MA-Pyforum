class Publication:

    def __init__(self, id, titre, contenu, id_auteur, id_forum):
        self.__id = id
        self.titre = titre
        self.__contenu = contenu
        self.__id_auteur = id_auteur
        self.__id_forum = id_forum
        liste_commentaire = []

    def __str__(self):
        return f"{self.__id} {self.titre}"

    