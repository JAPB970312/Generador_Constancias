# template_manager.py
import json
import os
from dataclasses import dataclass

@dataclass
class TemplateConfig:
    name: str
    placeholders: list
    font_presets: dict
    layout_settings: dict

class TemplateManager:
    def __init__(self):
        self.templates_dir = "templates"
        self.load_templates()
    
    def save_template_config(self, template_path, config):
        """Guarda configuración de plantilla para reutilización"""
        config_path = f"{template_path}.config.json"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)