; setup_GeneradorConstancias.iss - ejemplo básico
[Setup]
AppName=Generador Constancias
AppVersion=2.0
DefaultDirName={pf}\GeneradorConstancias
DefaultGroupName=Generador Constancias
OutputBaseFilename=GeneradorConstancias_Installer_v2.0
Compression=lzma
SolidCompression=yes

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
; Si usaste --onefile: copiar el exe
Source: "dist\GeneradorConstancias.exe"; DestDir: "{app}"; Flags: ignoreversion
; Si usaste --onedir: incluir carpeta entera (ejemplo)
; Source: "dist\GeneradorConstancias\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

; incluir assets adicionales si hiciste onefile y extraes en tiempo de ejecución, no necesario si todo está embebido
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\Generador Constancias"; Filename: "{app}\GeneradorConstancias.exe"

[Run]
Filename: "{app}\GeneradorConstancias.exe"; Description: "Lanzar Generador Constancias"; Flags: nowait postinstall skipifsilent
