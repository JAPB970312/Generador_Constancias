# settings_manager.py
import configparser

class SettingsManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.settings_file = "app_settings.ini"
        self.load_settings()
    
    def load_settings(self):
        """Carga configuración persistente"""
        if os.path.exists(self.settings_file):
            self.config.read(self.settings_file, encoding='utf-8')
        else:
            self.set_default_settings()
    
    def set_default_settings(self):
        """Configuración por defecto"""
        self.config['DEFAULT'] = {
            'output_quality': 'high',
            'default_font': 'Arial',
            'auto_open_folder': 'True',
            'backup_enabled': 'True',
            'max_threads': '4'
        }
        self.save_settings()