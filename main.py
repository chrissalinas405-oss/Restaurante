import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder

# Diseño en lenguaje KV
Builder.load_string('''
<PantallaInicio>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(20)
        
        Label:
            text: root.nombre_restaurante
            font_size: dp(36)
            bold: True
            color: 0.2, 0.4, 0.6, 1
            size_hint_y: 0.6
            
        Button:
            text: 'VER MENÚ'
            font_size: dp(24)
            size_hint_y: 0.3
            background_color: 0.2, 0.6, 0.4, 1
            on_press: root.ir_a_menu()

<PantallaCategorias>:
    ScrollView:
        GridLayout:
            id: categorias_grid
            cols: 1
            spacing: dp(10)
            padding: dp(20)
            size_hint_y: None
            height: self.minimum_height

<PantallaProductos>:
    ScrollView:
        GridLayout:
            id: productos_grid
            cols: 1
            spacing: dp(10)
            padding: dp(20)
            size_hint_y: None
            height: self.minimum_height

<ProductoWidget>:
    orientation: 'vertical'
    size_hint_y: None
    height: dp(80)
    padding: dp(10)
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10)]
    
    Label:
        text: root.nombre_producto
        font_size: dp(18)
        bold: True
        color: 0, 0, 0, 1
        size_hint_y: 0.6
    
    BoxLayout:
        size_hint_y: 0.4
        Label:
            text: f'Precio: L{root.precio_producto}'
            font_size: dp(16)
            color: 0.2, 0.5, 0.2, 1
        Label:
            text: root.descripcion_producto
            font_size: dp(14)
            color: 0.4, 0.4, 0.4, 1
            text_size: self.width, None
''')

# Pantallas de la aplicación
class PantallaInicio(Screen):
    nombre_restaurante = StringProperty("Restaurante App")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cargar_datos()
    
    def cargar_datos(self):
        try:
            with open('menu.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.nombre_restaurante = datos.get('restaurante', 'Restaurante App')
        except FileNotFoundError:
            print("Archivo menu.json no encontrado")
        except json.JSONDecodeError:
            print("Error en formato JSON")
    
    def ir_a_menu(self):
        self.manager.current = 'categorias'

class PantallaCategorias(Screen):
    def on_enter(self):
        # Limpiar widgets anteriores
        grid = self.ids.categorias_grid
        grid.clear_widgets()
        
        # Cargar categorías desde JSON
        try:
            with open('menu.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
                
                for categoria in datos.get('categorias', []):
                    btn = Button(
                        text=categoria['nombre'],
                        font_size=dp(20),
                        size_hint_y=None,
                        height=dp(70),
                        background_color=(0.3, 0.5, 0.7, 1)
                    )
                    # Pasar el ID de la categoría al callback
                    btn.bind(on_press=lambda instance, cat=categoria: self.mostrar_productos(cat))
                    grid.add_widget(btn)
                    
        except FileNotFoundError:
            grid.add_widget(Label(text="Error: menu.json no encontrado", color=(1,0,0,1)))
        except json.JSONDecodeError:
            grid.add_widget(Label(text="Error en formato JSON", color=(1,0,0,1)))
    
    def mostrar_productos(self, categoria):
        self.manager.get_screen('productos').cargar_productos(categoria)
        self.manager.current = 'productos'

class ProductoWidget(BoxLayout):
    nombre_producto = StringProperty("")
    precio_producto = StringProperty("")
    descripcion_producto = StringProperty("")

class PantallaProductos(Screen):
    def cargar_productos(self, categoria):
        grid = self.ids.productos_grid
        grid.clear_widgets()
        
        # Título de la categoría
        titulo = Label(
            text=categoria['nombre'],
            font_size=dp(28),
            bold=True,
            size_hint_y=None,
            height=dp(60),
            color=(0.2, 0.4, 0.6, 1)
        )
        grid.add_widget(titulo)
        
        # Botón para volver
        btn_volver = Button(
            text='← Volver a Categorías',
            font_size=dp(18),
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        btn_volver.bind(on_press=lambda x: setattr(self.manager, 'current', 'categorias'))
        grid.add_widget(btn_volver)
        
        # Mostrar productos
        for producto in categoria.get('productos', []):
            widget = ProductoWidget()
            widget.nombre_producto = producto['nombre']
            widget.precio_producto = str(producto['precio'])
            widget.descripcion_producto = producto.get('descripcion', '')
            grid.add_widget(widget)

# Aplicación principal
class RestauranteApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Fondo blanco
        
        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name='inicio'))
        sm.add_widget(PantallaCategorias(name='categorias'))
        sm.add_widget(PantallaProductos(name='productos'))
        
        return sm

if __name__ == '__main__':
    RestauranteApp().run()