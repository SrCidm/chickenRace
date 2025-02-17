import turtle
import random
import time

# Constantes
WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_players():
    """
    Solicita al usuario que ingrese el número de jugadores y lo valida.
    """
    while True:
        players = input("Enter the number of players (2-5): ")
        
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 5:
                return players
            else:
                print("Invalid input. Please enter a number between 2 and 5.")
        else:
            print("Invalid input. Please enter a valid numeric value.")

def create_players(colors):
    """
    Crea y configura las tortugas para la carrera.
    """
    turtles = []
    spacingx = WIDTH // (len(colors)) 

    for i, color in enumerate(colors):
        # Registra las imágenes reducidas en tamaño
        turtle.register_shape(f"sprites/small_{color}_frame1.gif")
        turtle.register_shape(f"sprites/small_{color}_frame2.gif")
        turtle.register_shape(f"sprites/small_{color}_frame3.gif")

        racer = turtle.Turtle()
        racer.shape(f"sprites/small_{color}_frame1.gif")  # Usar la imagen redimensionada
        racer.left(90)
        racer.penup()
        racer.goto(-WIDTH // 1.2 + (i + 2) * spacingx, -HEIGHT // 2 + 50)
        turtles.append(racer)
    
    return turtles

def draw_finish_line():
    """
    Dibuja la línea de meta en la pantalla.
    """
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.goto(-WIDTH // 2, HEIGHT // 2 - 20)
    finish_line.pendown()
    finish_line.goto(WIDTH // 2, HEIGHT // 2 - 20)
    finish_line.hideturtle()

def race(turtles, colors):
    """
    Simula la carrera de gallinas y determina al ganador.
    """
    while True:
        for i, racer in enumerate(turtles):
            distance = random.randint(1, 20)
            racer.forward(distance)
            
            # Cambiar el "frame" para simular movimiento con el color correcto
            color = colors[i]
            if racer.shape() == f"sprites/small_{color}_frame1.gif":
                racer.shape(f"sprites/small_{color}_frame2.gif")
            elif racer.shape() == f"sprites/small_{color}_frame2.gif":
                racer.shape(f"sprites/small_{color}_frame3.gif")
            else:
                racer.shape(f"sprites/small_{color}_frame1.gif")
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[turtles.index(racer)]

def init_turtle():
    """
    Configura la ventana de turtle.
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Chicken Race Game!")
    screen.bgcolor("white")

def main():
    """
    Función principal del programa.
    """
    # Obtener el número de jugadores
    players = get_number_of_players()
    
    # Configurar la ventana de turtle
    init_turtle()
    
    # Dibujar la línea de meta
    draw_finish_line()
    
    # Seleccionar colores aleatorios para las tortugas
    random.shuffle(COLORS)
    colors = COLORS[:players]
    
    # Crear las tortugas
    turtles = create_players(colors)
    
    # Iniciar la carrera
    winner = race(turtles, colors)
    
    # Mostrar el resultado
    print(f"The winner is the {winner} Chicken!")
    
    # Pausar antes de cerrar la ventana
    time.sleep(3)

if __name__ == "__main__":
    main()