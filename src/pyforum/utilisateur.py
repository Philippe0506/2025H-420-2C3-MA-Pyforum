class Utilisateur:

    def __init__ (self, id, username, email, mot_de_passe):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__mot_de_passe = mot_de_passe
        self.forums_inscrits = []

    def __str__(self):
        return f"{self.__id} {self.__username} {self.__email}"

    def joindre_forum(self, forum):
        self.forums_inscrits.append(forum)



