import os, sys, platform, shutil, time, venv
from pathlib import Path
from includes.clr import Clr

def bullet(path: Path, lab:str):
    print(Clr.brush("\t[Running]","blue","bold"), "=>", Clr.brush("VENVEASY","green", "under_line"));
    start_time = time.time();

    if not sys.version_info > (2, 2) or not hasattr(sys, "base_prefix"): return print("\n\t",Clr.brush("[ERROR]", "red"),"=>", Clr.brush("Python version must be >=3", "gray"))
    if os.path.exists(path): return print("\n\t", Clr.brush("[ERROR]", "red"),"=> The given path:", Clr.brush(os.path.abspath(path), "yellow", "under_line"), "already exists!\n")

    print(Clr.brush("\t[Info]","blue","bold"), "=>", Clr.brush("Platform:","cyan", "bold"), Clr.brush(platform.system(),"purple"),",", Clr.brush("Path:","cyan", "bold"), "[",Clr.brush(f"{os.path.abspath(path)}","yellow"),"]");

    bar = Clr.brush("━","green","bold");
    print()

    v = venv.EnvBuilder(system_site_packages=True, with_pip=True)
    os.system("powershell Set-ExecutionPolicy RemoteSigned -Scope CurrentUser")
    
    venvctx = v.ensure_directories(path)
    print(f"\r\t\t{bar*2} 5%", end="\r")
    v.setup_python(venvctx)
    print(f"\r\t\t{bar*7} 18%", end="\r")
    v.post_setup(venvctx)
    print(f"\r\t\t{bar*12} 34%", end="\r")
    v.setup_scripts(venvctx)
    print(f"\r\t\t{bar*18} 64%", end="\r")
    v.install_scripts(venvctx, path+"/Scripts")
    print(f"\r\t\t{bar*22} 77%", end="\r")
    v.create(path)
    print(f"\r\t\t{bar*26} 84%", end="\r")
    v.upgrade_dependencies(venvctx)
    print(f"\r\t\t{bar*26} 90%", end="\r")
    v.create_configuration(venvctx)
    print(f"\r\t\t{bar*30} 100%", end="\r")

    print()

    end_time = time.time();
    print(Clr.brush("\t[Done]","blue","bold"), "=>", Clr.brush("VENVEASY","green", "under_line"), Clr.brush("create","green"), Clr.brush("Virtual Envirement","cyan", "bold"), "[",Clr.brush(f"{path.split('/')[-1]}","yellow"),"]", Clr.brush("with succes in","green"), Clr.brush(f"{end_time - start_time:.3f}s","purple"));

    if lab != "-lab": return

    if shutil.which("code"):
        print(Clr.brush("\t[Running]","blue","bold"), "=>", Clr.brush("Text Editor:","cyan", "bold"), Clr.brush('vscode',"purple"));
        os.system(f"powershell code {os.path.abspath(path)}")
    elif shutil.which("sublime"):
        print(Clr.brush("\t[Running]","blue","bold"), "=>", Clr.brush("Text Editor:","cyan", "bold"), Clr.brush('sublime',"purple"));
        os.system(f"powershell sublime {os.path.abspath(path)}")
    elif shutil.which("atom"):
        print(Clr.brush("\t[Running]","blue","bold"), "=>", Clr.brush("Text Editor:","cyan", "bold"), Clr.brush('sublime',"purple"));
        os.system(f"powershell atom {os.path.abspath(path)}")


bullet(sys.argv[1], sys.argv[2])