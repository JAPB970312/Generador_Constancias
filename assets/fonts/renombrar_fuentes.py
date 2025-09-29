import os
import glob

def renombrar_fuentes_correctamente():
    """
    Renombra los archivos de fuentes con los nombres correctos
    """
    print("🔧 Iniciando renombrado de fuentes...")
    
    # Mapeo completo de nombres actuales a nombres correctos
    mapeo_renombres = {
        # Arial
        'arial.ttf': 'Arial Regular.ttf',
        'arialbd.ttf': 'Arial Bold.ttf', 
        'arialit.ttf': 'Arial Italic.ttf',
        'ARIALN.TTF': 'Arial Narrow Regular.ttf',
        'ARIALNB.TTF': 'Arial Narrow Bold.ttf',
        'ARIALNBI.TTF': 'Arial Narrow Bold Italic.ttf',
        'ARIALNI.TTF': 'Arial Narrow Italic.ttf',
        
        # Calibri
        'calibri.ttf': 'Calibri Regular.ttf',
        'calibriz.ttf': 'Calibri Bold Italic.ttf',
        
        # Segoe
        'segoepr.ttf': 'Segoe Print Regular.ttf',
        'segoeprb.ttf': 'Segoe Print Bold.ttf',
        'segoesc.ttf': 'Segoe Script Regular.ttf',
        'segoescb.ttf': 'Segoe Script Bold.ttf',
        'segoeui.ttf': 'Segoe UI Regular.ttf',
        'segoeuib.ttf': 'Segoe UI Bold.ttf',
        'segoeuii.ttf': 'Segoe UI Italic.ttf',
        'segoeuisi.ttf': 'Segoe UI Semilight.ttf',
        'segoeuz.ttf': 'Segoe UI Semibold.ttf',
        
        # Tahoma (corrigiendo "talnoma")
        'talnoma.ttf': 'Tahoma Regular.ttf',
        'talnomabd.ttf': 'Tahoma Bold.ttf',
        
        # Times New Roman
        'times.ttf': 'Times New Roman Regular.ttf',
        'timesbd.ttf': 'Times New Roman Bold.ttf',
        'timesbi.ttf': 'Times New Roman Bold Italic.ttf',
        'timesi.ttf': 'Times New Roman Italic.ttf',
        
        # Trebuchet MS (corrigiendo "trebuch")
        'trebuch.ttf': 'Trebuchet MS Regular.ttf',
        'trebuchd.ttf': 'Trebuchet MS Bold.ttf',
        'trebucbi.ttf': 'Trebuchet MS Bold Italic.ttf',
        'trebucit.ttf': 'Trebuchet MS Italic.ttf',
        
        # Verdana
        'verdana.ttf': 'Verdana Regular.ttf',
        'verdanab.ttf': 'Verdana Bold.ttf',
        'verdanai.ttf': 'Verdana Italic.ttf'
    }
    
    # Listar archivos actuales
    archivos_actuales = glob.glob("*.ttf") + glob.glob("*.TTF")
    print(f"📁 Archivos encontrados: {len(archivos_actuales)}")
    
    for archivo in sorted(archivos_actuales):
        print(f"   🔍 {archivo}")
    
    # Aplicar renombrado
    print("\n🔄 Aplicando renombrado...")
    renombrados = 0
    
    for nombre_actual, nombre_nuevo in mapeo_renombres.items():
        if os.path.exists(nombre_actual):
            # Verificar si el archivo nuevo ya existe
            if os.path.exists(nombre_nuevo):
                print(f"⚠️  Saltando: {nombre_nuevo} ya existe")
                continue
                
            os.rename(nombre_actual, nombre_nuevo)
            print(f"✅ Renombrado: {nombre_actual} → {nombre_nuevo}")
            renombrados += 1
        else:
            # Buscar variaciones del nombre
            for archivo in archivos_actuales:
                if nombre_actual.lower() in archivo.lower():
                    os.rename(archivo, nombre_nuevo)
                    print(f"✅ Renombrado (variación): {archivo} → {nombre_nuevo}")
                    renombrados += 1
                    break
    
    # Mostrar resultado final
    archivos_finales = glob.glob("*.ttf") + glob.glob("*.TTF")
    print(f"\n📊 RESULTADO FINAL:")
    print(f"   Total de archivos: {len(archivos_finales)}")
    print(f"   Archivos renombrados: {renombrados}")
    print(f"\n📁 Archivos finales:")
    for archivo in sorted(archivos_finales):
        print(f"   ✅ {archivo}")

# Ejecutar
if __name__ == "__main__":
    print("🎯 RENOMBRADOR DE FUENTES")
    print("=" * 50)
    renombrar_fuentes_correctamente()