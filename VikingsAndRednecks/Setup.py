from cx_Freeze import setup, Executable 

build_exe_options = {"include_files":["lib_images"]}



setup(name ="VikingsAndRednecks",
      version ="1.0",
      description="Alex's Game",
      options = {"build_exe": build_exe_options },
      executables =[Executable("VikingsAndRednecks.py")])