import time
import PySimpleGUI as sg
import tkinter as tk
from screensaver.aircraft import Aircraft
from screensaver.direction import Direction
from screensaver.position import Position

from screensaver.territory import Territory

# TODO: review https://www.pysimplegui.org/en/latest/readme/#layouts-are-funny-lol
TERRITORY = Territory(max_latitude=10, max_longitude=10)
CELL_SIZE = 50
WINDOW_SIZE = (800, 600)
WINDOW_COLOR = "white"
GRID_COLOR = "#DDDDDD"
BORDER_COLOR = "#ff0000"


def draw_grid_and_plane(canvas: tk.Canvas, aircraft: Aircraft):
    # Borra todo el contenido del canvas


    # Dibuja las líneas verticales del grid
    for i in range(0, WINDOW_SIZE[0], CELL_SIZE):
        canvas.create_line(
            i,
            0,
            i,
            WINDOW_SIZE[1],
            fill=GRID_COLOR if i != TERRITORY.max_latitude else BORDER_COLOR,
        )

    # Dibuja las líneas horizontales del grid
    for i in range(0, WINDOW_SIZE[1], CELL_SIZE):
        canvas.create_line(
            0,
            i,
            WINDOW_SIZE[0],
            i,
            fill=GRID_COLOR if i != TERRITORY.max_longitude else BORDER_COLOR,
        )

    arrow_coords = []
    if aircraft.current_direction() == Direction.North:
        arrow_coords = [
            aircraft.current_position().longitude * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
            (aircraft.current_position().longitude + 0.5) * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.South:
        arrow_coords = [
            aircraft.current_position().longitude * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            (aircraft.current_position().longitude + 0.5) * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.East:
        arrow_coords = [
            aircraft.current_position().longitude * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            (aircraft.current_position().latitude + 0.5) * CELL_SIZE,
            aircraft.current_position().longitude * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.West:
        arrow_coords = [
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            aircraft.current_position().longitude * CELL_SIZE,
            (aircraft.current_position().latitude + 0.5) * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.NorthEast:
        arrow_coords = [
            aircraft.current_position().longitude * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.NorthWest:
        arrow_coords = [
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
            aircraft.current_position().longitude * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
            aircraft.current_position().longitude * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.SouthEast:
        arrow_coords = [
            aircraft.current_position().longitude * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
        ]
    elif aircraft.current_direction() == Direction.SouthWest:
        arrow_coords = [
            (aircraft.current_position().longitude + 1) * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            aircraft.current_position().longitude * CELL_SIZE,
            aircraft.current_position().latitude * CELL_SIZE,
            aircraft.current_position().longitude * CELL_SIZE,
            (aircraft.current_position().latitude + 1) * CELL_SIZE,
        ]
    canvas.create_polygon(arrow_coords, fill="black")


def main():

    sg.theme("dark grey 9")
    layout = [
        [sg.Text("Presione el botón para activar el screensaver")],
        [sg.Button("Iniciar screensaver"), sg.Button("Salir")],
    ]

    window = sg.Window("Screensaver de aviones", layout)
    while True:
        event, values = window.read()
        if event == "Iniciar screensaver":
            root = tk.Tk()
            root.title("Screensaver de aviones")
            canvas = tk.Canvas(
                root, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1], bg=WINDOW_COLOR
            )
            canvas.pack()

            initial_position = Position(longitude=0, latitude=0)
            aircraft_1 = Aircraft.create(
                initial_position, TERRITORY, direction=Direction.NorthEast
            )
            aircraft_2 = Aircraft.create(
                initial_position.go_down_right(), TERRITORY, direction=Direction.North
            )
            while True:
                aircraft_1.move()
                aircraft_2.move()
                draw_grid_and_plane(canvas, aircraft_1)
                draw_grid_and_plane(canvas, aircraft_2)
                # Actualiza el canvas y espera un breve periodo de tiempo
                root.update()
                time.sleep(0.3)

        if event == sg.WIN_CLOSED or event == "Salir":
            break

    window.close()


if __name__ == "__main__":
    main()
