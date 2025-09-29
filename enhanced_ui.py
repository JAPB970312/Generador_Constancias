# enhanced_ui.py - Nuevas características para ui.py

class EnhancedApp(App):
    def __init__(self):
        super().__init__()
        self.add_advanced_features()
    
    def add_advanced_features(self):
        # Panel de previsualización múltiple
        self.preview_tabs = QTabWidget()
        
        # Editor de estilos avanzado
        self.style_preset_combo = QComboBox()
        self.style_preset_combo.addItems(["Formal", "Moderno", "Académico", "Personalizado"])
        self.style_preset_combo.currentTextChanged.connect(self.apply_style_preset)
        
        # Controles de calidad de salida
        self.quality_slider = QSlider(Qt.Orientation.Horizontal)
        self.quality_slider.setRange(1, 5)  # Calidad 1-5
        self.quality_slider.setValue(3)