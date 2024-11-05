import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    
    def __str__(self):
        return f"{self.titulo} por {self.autor},{self.genero}"

# Criar uma lista de lirvos   
biblioteca = []

# Lista para armazenamento
generos = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, genero):
    novo_livro = Livro(titulo, autor, genero)
    biblioteca.append(novo_livro)
    generos.append(genero)
    print(f'{novo_livro.titulo} foi adicionado à biblioteca.')

# Função para listar os livros a biblioteca
def listar_livros():
    print('Livros na Biblioteca: ')
    for livro in biblioteca:
        print(livro)

# Livros para serem adicionados
adicionar_livro('Dom Quixote', 'Miguel de Cervantes', 'Paródia.')
adicionar_livro('1984', 'George Orwell', 'Ficção Científica.')
adicionar_livro('O Senhor dos Anéis - A Sociedade do Anél', 'J.R.R. Tolkien', 'Fantasia.')
adicionar_livro('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia.')
adicionar_livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Infantil.')
adicionar_livro('O Senhor dos Anéis - As Duas Torres.')

# Lista todos os livros na biblioteca
listar_livros()

# Contagem de livro por genero
contagem_por_genero = {}
for livro in biblioteca:
    genero = livro.genero
    contagem_por_geneno[genero] = contagem_por_genero.get(genero, 0) + 1

# Criar um grafíco de barras
plt.bar(contagem_por_genero.keys(), contagem_por_genero.values(), color='skyblue')
plt.xlabel('Gênero')
plt.ylabel('Número de Livros.')
plt.title('Distribuição de Livros na Biblioteca por Gênerod')
plt.show()
