# office_processor_task.py
import os
from document_processor import get_processor

def process_single_office_document(task_data):
    """
    Función para procesamiento paralelo de documentos Office
    """
    try:
        template_path, record, font_map, placeholder_map, output_dir = task_data
        
        data_map = {
            placeholder: record.get(column_name, '') 
            for placeholder, column_name in placeholder_map.items()
        }

        name_for_file = data_map.get('{{TEXT_1}}', f'Constancia_temp')
        clean_name = "".join(c for c in str(name_for_file) if c.isalnum() or c in (' ', '-', '_')).rstrip()
        output_filename = os.path.join(output_dir, f"{clean_name}.pdf")

        processor = get_processor(template_path)
        processor.process(data_map, font_map)
        processor.save_as_pdf(output_filename)

        return True, name_for_file, output_filename, None
    
    except Exception as e:
        return False, None, None, str(e)