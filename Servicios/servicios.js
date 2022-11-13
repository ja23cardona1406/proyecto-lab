import { collection, doc, setDoc, getDocs } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js";
import {db} from "./conexion.js";

class Envio{
    constructor(name, correo,comprobante,direccion){
        this.name = name;
        this.correo = correo;
        this.comprobante = comprobante;
        this.direccion = direccion;
    }
    async addDataCollection(){
        let result = await setDoc(doc(db, "envio", this.name), 
        {   name: this.name,
            correo: this.correo,
            comprobante: this.comprobante,
            direccion: this.direccion
        });
        console.log(result)
    }
    async getDataCollection() {
      const envios = collection(db, 'envio');
      const resultado = await getDocs(envios);
      const list = resultado.docs.map(doc => doc.data());
      console.log(list)
      return list;
    }
}
const servicioForm = document.getElementById('formulario-servicios');
servicioForm.addEventListener('submit', async(e) => { 
    e.preventDefault();
    const nombre = servicioForm['name'].value;
    const correo = servicioForm['email'].value;
    const comprobante = servicioForm['comprobante'].value;
    const direccion = servicioForm['direccion'].value;
    let send = new Envio(nombre,correo,comprobante,direccion);
    send.getDataCollection();
    await send.addDataCollection();
    window.location.reload();
});