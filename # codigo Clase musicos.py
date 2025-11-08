
# Definimos la clase base
class Musico:
    def instrumento(self):
        """Método base que describe el instrumento del músico."""
        return "Toca un instrumento."

# Definimos la primera subclase
class Guitarrista(Musico):
    def instrumento(self):
        """Sobrescribe el método instrumento para un guitarrista."""
        return "Toca la guitarra. "

# Definimos la segunda subclase
class Baterista(Musico):
    def instrumento(self):
        """Sobrescribe el método instrumento para un baterista."""
        return "Toca la batería. "

    def new_method(self):
        return "Toca la batería. "

# Instanciamos los objetos
musico_generico = Musico()
guitarrista_jorge = Guitarrista()
baterista_claudia = Baterista()

# Demostramos el polimorfismo
print(musico_generico.instrumento() )
print(guitarrista_jorge.instrumento() )
print(baterista_claudia.instrumento() )