class Forum:

    def __init__ (self, id, nom, descrption = ""):
        self.__id = id
        self.nom = nom
        self.descrption = descrption
        self.publications_forums = []

    def __str__(self):
        return f"{self.__id} {self.__nom}"

