# final_project

- Abrit Git Bash y crear un directorio de trabajo 

cd
mkdir -p Documents/proyecto
cd 
Documents/proyecto


- Clonamos el proyecto y vamos al directorio

git clone https://github.com/andreloluciano/final_project.git

- Abrimos la carpeta con Visual Studio Code

code .

- Dentro del Visual Studio Code vamos al proyecto y activamos el entorno virtual

cd final_project
python -m venv venv   
.\venv\Scripts\activate

- Una vez activado, instalamos los requerimientos y hacemos migración

pip install -r requirements.txt
python manage.py makemigrations   
python manage.py migrate  

- Por último, corremos el servidor

python manage.py runserver

