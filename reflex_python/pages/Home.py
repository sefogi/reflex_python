import reflex as rx

@rx.page(route='/', title= 'inicio')
def home():
    return rx.box(
        rx.heading('Welcome to home page',  style={"color": "blue", "fontSize": "24px"}),
        rx.text('esta es una pagina creada con reflex', style={"fontFamily": "Arial", "color": "gray"}),
        rx.button(
            'haz click aqui', 
            on_click=lambda: rx.window_alert('Boton presionado'),
            style={"backgroundColor": "green", "color": "white", "padding": "10px", "borderRadius": "5px"}
        ),
        style={"padding": "20px", "textAlign": "center"}
    )
