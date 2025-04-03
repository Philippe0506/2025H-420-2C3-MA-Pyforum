class Utilisateur:

    def __init__ (self, id, nom_utilisateur, email, mot_de_passe):
        self.__id = id
        self.__nom_utilisateur = nom_utilisateur
        self.__email = email
        self.__mot_de_passe = mot_de_passe
        self.forums_inscrits = []

    def __str__(self):
        return f"{self.__id} {self.__nom_utilisateur} {self.__email}"

utilisateur1 = Utilisateur(1, "Philippe", "123@gmail.com", 12345)
utilisateur1.sauvegarder_utilisateur
print(utilisateur1)

