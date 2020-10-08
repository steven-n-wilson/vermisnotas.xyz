# vermisnotas.xyz

## Descripción
Este proyecto busca automatizar la recopilación de notas de los alumnos en WebAssign y desplegarlas en una página web. Por medio de **Selenium** se automatizó el login y la extracción de notas. **Gspread** fue utilizado para actualizar un Google Sheet con las notas y utilizando **pandas** se guarda localmente una copia del Google Sheet. **Jinja** nos permite desplegar la copia del Google Sheet dinámicamente en la pagina web que ha sido registrada en el dominio de www.vermisnotas.xyz/, se aquirió el nombre del dominio con namecheap.com y se hizo el deployment con Heroku. 
