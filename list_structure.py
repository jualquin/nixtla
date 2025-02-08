import os

def print_directory_structure(root_dir, indent=''):
    for item in os.listdir(root_dir):
        if item.startswith('.') or item in [ '.circleci' '.venv', 'lightning_logs']:
            continue
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            print(f"{indent}{item}/")
            print_directory_structure(item_path, indent + '    ')
        else:
            print(f"{indent}{item}")

# Cambia 'root_dir' a la ruta de tu proyecto
root_dir = 'c:/Users/julian.quintero/WORKSPACE/NEURAL_FORECAST/neuralforecast'
print_directory_structure(root_dir)