def Commentaire:

    def __init__(self, id, id_auteur, contenu, id_publication):
        self.__id = id
        self.__id_auteur = id_auteur
        self.contenu = contenu
        self.__id_publication = id_publication

    def __str__(self):
        return f"{self.contenu}"

