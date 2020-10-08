# vermisnotas.xyz

## Descripción
Este proyecto busca automatizar la recopilación de notas de los alumnos en WebAssign y desplegarlas en una página web. 

Por medio de **Selenium** se automatizó el login y la extracción de notas. **Gspread** fue utilizado para actualizar un Google Sheet con las notas y utilizando **pandas** se guarda localmente una copia del Google Sheet. **Jinja** y **Flask** nos permiten desplegar la copia del Google Sheet dinámicamente en la pagina web que ha sido registrada en el dominio de www.vermisnotas.xyz/. Se aquirió el nombre del dominio con **namecheap.com** y se hizo el deployment con **Heroku**. 


## Descripción General de la Arquitectura
![Descripción General de la Arquitectura](https://github.com/steven-n-wilson/vermisnotas.xyz/blob/master/static/images/architectureOverview.png)

## Setup Local


