# Trabajo Práctico Lnx 

Se enumeran los pasos para el despliegue de un contenedor Docker para la ejecución de una aplicación en python.

 - información importante 
  
      - Ansible dnf python3 no funciona con Centos 7,  por tal motivo, el despliegue no es posible en CentOS 7.

## Despliegue

-	Paso 1: Clonado del repositorio Git
---
          # git clone https://github.com/FrancoMartinCuello/diplomatura2022s1.git
          # cd diplomatura2022s1
---

-	Paso 2: Instalación de ansible
  - Para distribuciones redhat - (distribuciones debian use “apt”)
---
          # sudo yum install ansible
---

-	Paso 3: Editar el inventario de ansible para definir el/los host donde se hará el despliegue de la aplicación.
---
          # vi host.yml
---

-	Por defecto el inventario esta preparado para realizar el despliegue en el host local.
---

     all:
      vars:
        ansible_python_interpreter: /usr/bin/python3
      children:
        local:
    local:
      vars:
        ansible_connection: local
      hosts:
        localhost
---

-	Paso 4: Ejecutar el playbook de ansible
  
          # ansible-playbook -i host.yml playbook/PlaybookImagesApp.yaml

