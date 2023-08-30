function preventDelete() {
    const getBtn = document.querySelectorAll(".btn btn-sm btn-danger")
    getBtn.addEventListener("click", (e) => {
        const confirmAction = confirm("¿Seguro que deseas eliminar esta materia?");
        if (!confirmAction) {
            e.preventDefault();
        }
    })
}


//activar el evento invocandose asi mismo
(function(){
	preventDelete();
})()