let editar = document.querySelectorAll('.editar');
let editar_link = [...document.querySelectorAll('.editar a')];

let inscribir = document.querySelectorAll('.inscribir');
let inscribir_link = [...document.querySelectorAll('.inscribir a')];

let info = document.querySelectorAll('.info');
let info_link = [...document.querySelectorAll('.info a')];


[...editar].forEach( (item, index) => {
    item.addEventListener('mouseover', () => {
        editar_link[index].style = 'color: #ffff';
    });
});

[...editar].forEach( (item, index) => {
    item.addEventListener('mouseout', () => {
        editar_link[index].style = 'color: #A7A1AE';
    });
});

[...inscribir].forEach( (item, index) => {
    item.addEventListener('mouseover', () => {
        inscribir_link[index].style = 'color: #ffff';
    });
});

[...inscribir].forEach( (item, index) => {
    item.addEventListener('mouseout', () => {
        inscribir_link[index].style = 'color: #A7A1AE';
    });
});

[...info].forEach( (item, index) => {
    item.addEventListener('mouseover', () => {
        info_link[index].style = 'color: #ffff';
    });
});

[...info].forEach( (item, index) => {
    item.addEventListener('mouseout', () => {
        info_link[index].style = 'color: #A7A1AE';
    });
});