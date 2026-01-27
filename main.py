import json
import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.lang import Builder

# ==================== VERIFICAR LOGO ====================
def verificar_logo():
    """Verifica si existe el archivo logo.png"""
    if os.path.exists('logo.png'):
        print("✅ Logo encontrado: logo.png")
        return True
    else:
        print("⚠️ Logo no encontrado, mostrando texto")
        return False

LOGO_EXISTE = verificar_logo()

# ==================== DISEÑO KV CON LOGO ====================
Builder.load_string('''
<PantallaInicio>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        
        # Logo o título
        BoxLayout:
            size_hint_y: 0.35
            orientation: 'vertical'
            
            # Logo (si existe)
            Image:
                source: 'logo.png' if app.logo_existe else ''
                size_hint: (0.8, 0.8)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                allow_stretch: True
                keep_ratio: True
                opacity: 1 if app.logo_existe else 0
            
             # Título
        Label:
            text: 'KCB RESTAURANT'
            font_size: dp(40)
            bold: True
            color: 0.83, 0.69, 0.22, 1
            halign: 'center'
            size_hint_y: 0.3
        
        # Estadísticas
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.2
            spacing: dp(10)
            padding: dp(10)
            
            canvas.before:
                Color:
                    rgba: 0.2, 0.2, 0.2, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(10)]
            
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: str(root.total_categorias)
                    font_size: dp(28)
                    bold: True
                    color: 0.83, 0.69, 0.22, 1
                    halign: 'center'
                Label:
                    text: 'Categorías'
                    font_size: dp(14)
                    color: 0.7, 0.7, 0.7, 1
                    halign: 'center'
            
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: str(root.total_productos)
                    font_size: dp(28)
                    bold: True
                    color: 0.83, 0.69, 0.22, 1
                    halign: 'center'
                Label:
                    text: 'Productos'
                    font_size: dp(14)
                    color: 0.7, 0.7, 0.7, 1
                    halign: 'center'
        
        # Botón principal
        Button:
            text: 'VER MENÚ'
            font_size: dp(28)
            size_hint_y: 0.25
            background_color: 0.83, 0.69, 0.22, 1
            background_normal: ''
            color: 0.1, 0.1, 0.1, 1
            bold: True
            on_press: root.ir_a_menu()
        
        # Espacio inferior
        Widget:
            size_hint_y: 0.2

<PantallaCategorias>:
    BoxLayout:
        orientation: 'vertical'
        
        # Barra superior
        BoxLayout:
            size_hint_y: 0.15
            orientation: 'horizontal'
            padding: dp(15)
            spacing: dp(10)
            
            canvas.before:
                Color:
                    rgba: 0.2, 0.2, 0.2, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            # Botón Atrás
            Button:
                text: 'Atras'
                font_size: dp(28)
                size_hint_x: 0.2
                background_color: 0.83, 0.69, 0.22, 1
                background_normal: ''
                color: 0.1, 0.1, 0.1, 1
                on_press: root.ir_a_inicio()
            
            # Título
            Label:
                text: 'CATEGORÍAS'
                font_size: dp(24)
                bold: True
                color: 0.83, 0.69, 0.22, 1
                halign: 'center'
                size_hint_x: 0.6
        
        # Lista de categorías
        ScrollView:
            size_hint: (1, 0.85)
            
            GridLayout:
                id: categorias_grid
                cols: 1
                spacing: dp(15)
                padding: [dp(20), dp(20)]
                size_hint_y: None
                height: self.minimum_height

<PantallaProductos>:
    BoxLayout:
        orientation: 'vertical'
        
        # Barra superior
        BoxLayout:
            size_hint_y: 0.15
            orientation: 'horizontal'
            padding: dp(15)
            spacing: dp(10)
            
            canvas.before:
                Color:
                    rgba: 0.2, 0.2, 0.2, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            # Botón Atrás
            Button:
                text: 'Atras'
                font_size: dp(28)
                size_hint_x: 0.2
                background_color: 0.83, 0.69, 0.22, 1
                background_normal: ''
                color: 0.1, 0.1, 0.1, 1
                on_press: root.ir_a_categorias()
            
            # Título
            Label:
                id: titulo_categoria
                text: ''
                font_size: dp(22)
                bold: True
                color: 0.83, 0.69, 0.22, 1
                halign: 'center'
                size_hint_x: 0.6
        
        # Lista de productos
        ScrollView:
            size_hint: (1, 0.85)
            
            GridLayout:
                id: productos_grid
                cols: 1
                spacing: dp(15)
                padding: [dp(20), dp(20)]
                size_hint_y: None
                height: self.minimum_height

<WidgetProducto>:
    orientation: 'vertical'
    size_hint_y: None
    height: dp(100)
    padding: [dp(15), dp(10)]
    spacing: dp(5)
    
    canvas.before:
        Color:
            rgba: 0.2, 0.2, 0.2, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10)]
        
        Color:
            rgba: 0.83, 0.69, 0.22, 0.5
        Line:
            rounded_rectangle: [self.x, self.y, self.width, self.height, dp(10)]
            width: dp(1.5)
    
    # Nombre del producto
    Label:
        text: root.nombre
        font_size: dp(20)
        bold: True
        color: 0.83, 0.69, 0.22, 1
        size_hint_y: 0.6
        text_size: self.width, None
        halign: 'left'
        valign: 'middle'
    
    # Precio y descripción
    BoxLayout:
        size_hint_y: 0.4
        spacing: dp(10)
        
        # Precio
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.4
            
            Label:
                text: 'Precio:'
                font_size: dp(14)
                color: 0.7, 0.7, 0.7, 1
                text_size: self.width, None
                halign: 'left'
            
            Label:
                text: 'L' + root.precio
                font_size: dp(18)
                color: 0.83, 0.69, 0.22, 1
                bold: True
                text_size: self.width, None
                halign: 'left'
        
        # Descripción
        Label:
            text: root.descripcion
            font_size: dp(15)
            color: 0.7, 0.7, 0.7, 1
            size_hint_x: 0.6
            text_size: self.width, None
            halign: 'left'
            valign: 'middle'
            shorten: True
''')

# ==================== WIDGET PERSONALIZADO PARA PRODUCTOS ====================
class WidgetProducto(BoxLayout):
    nombre = StringProperty("")
    precio = StringProperty("")
    descripcion = StringProperty("")

# ==================== CLASES ====================
class PantallaInicio(Screen):
    total_categorias = NumericProperty(0)
    total_productos = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cargar_datos()
    
    def cargar_datos(self):
        """Carga datos del menú JSON"""
        try:
            if not os.path.exists('menu.json'):
                print("❌ menu.json no encontrado, creando ejemplo...")
                self.crear_menu_ejemplo()
            
            with open('menu.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            categorias = datos.get('categorias', [])
            self.total_categorias = len(categorias)
            
            total_productos = 0
            for categoria in categorias:
                total_productos += len(categoria.get('productos', []))
            
            self.total_productos = total_productos
            print(f"✅ Datos cargados: {self.total_categorias} categorías, {self.total_productos} productos")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.total_categorias = 3
            self.total_productos = 9
    
    def crear_menu_ejemplo(self):
        """Crea un menu.json de ejemplo si no existe"""
        menu_ejemplo = {
            "restaurante": "KCB RESTAURANT",
            "categorias": [
                {
                    "nombre": " ENTRADAS",
                    "productos": [
                        {"nombre": "Ensalada César", "precio": 65, "descripcion": "Lechuga, crutones, queso parmesano"},
                        {"nombre": "Sopa del Día", "precio": 45, "descripcion": "Sopa casera cambia diariamente"}
                    ]
                },
                {
                    "nombre": "🥩 PLATOS PRINCIPALES",
                    "productos": [
                        {"nombre": "Filete KCB", "precio": 150, "descripcion": "Corte premium con salsa especial"},
                        {"nombre": "Pasta Alfredo", "precio": 85, "descripcion": "Pasta con salsa cremosa"}
                    ]
                },
                {
                    "nombre": "🥤 BEBIDAS",
                    "productos": [
                        {"nombre": "Jugo Natural", "precio": 25, "descripcion": "Naranja, piña o tamarindo"},
                        {"nombre": "Café Expresso", "precio": 15, "descripcion": "Café negro intenso"}
                    ]
                }
            ]
        }
        
        with open('menu.json', 'w', encoding='utf-8') as f:
            json.dump(menu_ejemplo, f, ensure_ascii=False, indent=2)
        print("✅ menu.json creado con datos de ejemplo")
    
    def ir_a_menu(self):
        """Navega a la pantalla de categorías"""
        print("Navegando a categorías...")
        # Forzar recarga de categorías
        self.manager.get_screen('categorias').cargar_categorias()
        self.manager.current = 'categorias'

class PantallaCategorias(Screen):
    def cargar_categorias(self):
        """Carga y muestra las categorías desde menu.json"""
        print("DEBUG: Intentando cargar categorías...")
        
        # Asegurarse de que tenemos acceso al GridLayout
        if not hasattr(self, 'ids'):
            print("❌ ERROR: self.ids no está disponible aún")
            return
            
        if 'categorias_grid' not in self.ids:
            print("❌ ERROR: categorias_grid no encontrado en ids")
            return
            
        grid = self.ids.categorias_grid
        grid.clear_widgets()
        
        try:
            # Verificar que el archivo existe
            if not os.path.exists('menu.json'):
                print("❌ menu.json no existe")
                grid.add_widget(Label(
                    text="Error: menu.json no encontrado",
                    font_size=dp(20),
                    color=(1, 0, 0, 1),
                    size_hint_y=None,
                    height=dp(50)
                ))
                return
            
            with open('menu.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            categorias = datos.get('categorias', [])
            print(f"DEBUG: Encontradas {len(categorias)} categorías")
            
            if not categorias:
                print("DEBUG: No hay categorías en el JSON")
                grid.add_widget(Label(
                    text="No hay categorías disponibles",
                    font_size=dp(20),
                    color=(0.83, 0.69, 0.22, 1),
                    size_hint_y=None,
                    height=dp(60)
                ))
                return
            
            # Crear botones para cada categoría
            for categoria in categorias:
                nombre = categoria.get('nombre', 'Categoría')
                num_productos = len(categoria.get('productos', []))
                
                btn = Button(
                    text=f"{nombre}\n({num_productos} productos)",
                    font_size=dp(20),
                    size_hint_y=None,
                    height=dp(100),
                    background_color=(0.2, 0.2, 0.2, 1),
                    background_normal='',
                    color=(0.83, 0.69, 0.22, 1),
                    bold=True,
                    halign='center'
                )
                
                # Configurar para texto multilínea
                btn.text_size = (self.width * 0.9, None)
                btn.valign = 'middle'
                
                # Asignar función al botón
                btn.bind(on_press=lambda instance, cat=categoria: self.mostrar_productos(cat))
                
                grid.add_widget(btn)
                print(f"DEBUG: Añadida categoría: {nombre}")
            
            print(f"✅ {len(categorias)} categorías cargadas exitosamente")
            
        except json.JSONDecodeError as e:
            print(f"❌ Error en JSON: {e}")
            grid.add_widget(Label(
                text="Error en formato JSON",
                font_size=dp(18),
                color=(1, 0, 0, 1),
                size_hint_y=None,
                height=dp(50)
            ))
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            grid.add_widget(Label(
                text=f"Error: {str(e)}",
                font_size=dp(18),
                color=(1, 0, 0, 1),
                size_hint_y=None,
                height=dp(50)
            ))
    
    def on_enter(self):
        """Se ejecuta cuando la pantalla se muestra"""
        print("PantallaCategorias.on_enter() llamado")
        self.cargar_categorias()
    
    def mostrar_productos(self, categoria):
        """Navega a la pantalla de productos"""
        print(f"Mostrando productos de: {categoria.get('nombre')}")
        pantalla_productos = self.manager.get_screen('productos')
        pantalla_productos.cargar_productos(categoria)
        self.manager.current = 'productos'
    
    def ir_a_inicio(self):
        """Regresa al inicio"""
        self.manager.current = 'inicio'

class PantallaProductos(Screen):
    def cargar_productos(self, categoria):
        """Carga productos de una categoría"""
        grid = self.ids.productos_grid
        grid.clear_widgets()
        
        nombre_categoria = categoria.get('nombre', 'Productos')
        self.ids.titulo_categoria.text = nombre_categoria
        
        productos = categoria.get('productos', [])
        
        if not productos:
            grid.add_widget(Label(
                text="No hay productos en esta categoría",
                font_size=dp(20),
                color=(0.7, 0.7, 0.7, 1),
                size_hint_y=None,
                height=dp(60)
            ))
            return
        
        for producto in productos:
            widget = WidgetProducto()
            widget.nombre = producto.get('nombre', 'Producto')
            widget.precio = str(producto.get('precio', 0))
            widget.descripcion = producto.get('descripcion', '')
            
            grid.add_widget(widget)
        
        print(f"✅ {len(productos)} productos cargados en '{nombre_categoria}'")
    
    def ir_a_categorias(self):
        """Regresa a categorías"""
        self.manager.current = 'categorias'

# ==================== APLICACIÓN ====================
class RestauranteApp(App):
    logo_existe = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logo_existe = LOGO_EXISTE
    
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        Window.size = (400, 700)
        
        # Crear pantallas
        sm = ScreenManager()
        
        pantalla_inicio = PantallaInicio(name='inicio')
        pantalla_categorias = PantallaCategorias(name='categorias')
        pantalla_productos = PantallaProductos(name='productos')
        
        sm.add_widget(pantalla_inicio)
        sm.add_widget(pantalla_categorias)
        sm.add_widget(pantalla_productos)
        
        return sm
    
    def on_start(self):
        print("=" * 50)
        print("🍽️ KCB RESTAURANT - App iniciada")
        print("=" * 50)

# ==================== CREAR LOGO SI NO EXISTE ====================
def crear_logo_simple():
    """Crea un logo simple si no existe"""
    if not os.path.exists('logo.png'):
        try:
            from PIL import Image, ImageDraw, ImageFont
            print("🖼️ Creando logo simple...")
            
            # Crear imagen
            img = Image.new('RGB', (400, 400), color=(30, 30, 30))
            draw = ImageDraw.Draw(img)
            
            # Dibujar círculo dorado
            draw.ellipse([50, 50, 350, 350], fill=(212, 175, 55), outline=(255, 215, 0), width=10)
            
            # Intentar añadir texto
            try:
                # Intentar con fuente Arial, sino usar default
                font = ImageFont.truetype("arial.ttf", 120)
            except:
                font = ImageFont.load_default()
            
            # Texto KCB
            draw.text((200, 200), "KCB", fill=(30, 30, 30), font=font, anchor="mm")
            
            # Guardar
            img.save('logo.png', 'PNG')
            print("✅ Logo creado: logo.png")
            
        except ImportError:
            print("⚠️ Instala Pillow para logo automático: pip install Pillow")
        except Exception as e:
            print(f"⚠️ Error creando logo: {e}")

# ==================== EJECUTAR ====================
if __name__ == '__main__':
    # Crear logo si no existe
    crear_logo_simple()
    
    # Actualizar variable
    LOGO_EXISTE = os.path.exists('logo.png')
    
    # Iniciar aplicación
    RestauranteApp().run()
