import { collection, doc, setDoc, getDocs } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js";
import {db} from "./registroConect.js";

class Usuario{
    constructor(correo, password){
        this.correo = correo;
        this.password = password;
    }
    async addDataCollection(){
        let result = await setDoc(doc(db, "users", this.correo), 
        {   correo: this.correo,
            password: this.password
        });
        console.log('insert ===>',result)
    }
    async getDataCollection() {
      const usuarios = collection(db, 'users');
      const resultado = await getDocs(usuarios);
      const list = resultado.docs.map(doc => doc.data());
      console.log('see list ===>', list)
      return list;
    }
}
const usuarioForm = document.getElementById('formulario__login');
usuarioForm.addEventListener('submit', async(e) => { 
    e.preventDefault();
    const correo = usuarioForm['email'].value;
    const password = usuarioForm['password'].value;
    let user = new Usuario(correo, password);
    user.getDataCollection();
    await user.addDataCollection();
    window.location.reload();
});