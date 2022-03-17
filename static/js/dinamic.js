let editar = document.getElementById('editar');
let editar_link = document.getElementById('editlink');
let inscribir = document.getElementById('inscribir');
let inscribir_link = document.getElementById('inscribirlink');
let info = document.getElementById('info');
let info_link = document.getElementById('infolink');

editar.addEventListener('mouseover', () => {
    editar_link.style = 'color: #ffff';
});

editar.addEventListener('mouseout', () => {
    editar_link.style = 'color: #A7A1AE';
});

inscribir.addEventListener('mouseover', () => {
    inscribir_link.style = 'color: #ffff';
});

inscribir.addEventListener('mouseout', () => {
    inscribir_link.style = 'color: #A7A1AE';
});

info.addEventListener('mouseover', () => {
    info_link.style = 'color: #ffff';
});

info.addEventListener('mouseout', () => {
    info_link.style = 'color: #A7A1AE';
});
