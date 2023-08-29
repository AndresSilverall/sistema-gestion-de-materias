const getBtn = document.getElementById("delete")

function preventDelete() {
    getBtn.addEventListener("click", (e) => {
        const confirmAction = confirm("¿Seguro que deseas eliminar esta materia?");
        if (!confirmAction) {
            e.preventDefault();
        }
    })
}


preventDelete();