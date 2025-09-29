# features.py
class AdvancedFeatures:
    @staticmethod
    def add_watermark(output_path, watermark_text):
        """Añade marca de agua a los PDFs generados"""
        doc = fitz.open(output_path)
        for page in doc:
            page.insert_text((50, 50), watermark_text, 
                           fontsize=8, color=(0.8, 0.8, 0.8), rotate=45)
        doc.save(output_path)
        doc.close()
    
    @staticmethod
    def merge_pdfs(pdf_list, output_path):
        """Combina múltiples PDFs en uno"""
        merged_doc = fitz.open()
        for pdf_path in pdf_list:
            with fitz.open(pdf_path) as doc:
                merged_doc.insert_pdf(doc)
        merged_doc.save(output_path)
        merged_doc.close()
    
    @staticmethod
    def compress_pdf(input_path, output_path, quality='medium'):
        """Comprime PDF para reducir tamaño"""
        compression_levels = {
            'low': 1,
            'medium': 4, 
            'high': 8
        }
        doc = fitz.open(input_path)
        doc.save(output_path, 
                garbage=4, 
                deflate=True, 
                clean=True,
                compression_level=compression_levels.get(quality, 4))
        doc.close()