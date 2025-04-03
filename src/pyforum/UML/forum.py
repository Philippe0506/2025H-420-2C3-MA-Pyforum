class Forum:

    def __init__ (self, id, nom, descption = ""):
        self.__id = id
        self.nom = nom
        self.publications_forums = []

    def __str__(self):
        return f"{self.__id} {self.__nom}"

forum1 = Forum(111, "Salut")
forum1.sauvegarder_forum
print(forum1)