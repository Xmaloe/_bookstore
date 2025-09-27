from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import subprocess

@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            # Defina o caminho para o seu repositório
            repo_dir = '/home/Analice/bookstore'
            
            # Comando de git pull usando subprocess
            result = subprocess.run(
                ["git", "-C", repo_dir, "pull"],
                check=True,
                capture_output=True,
                text=True
            )
            
            # Retorne a saída do comando para verificar o sucesso
            return HttpResponse(f"Updated code on PythonAnywhere:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            # Em caso de erro, capture a saída e mostre no response
            return HttpResponse(f"Failed to update code:\n{e.stderr}")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
