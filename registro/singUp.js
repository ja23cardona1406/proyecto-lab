import { collection, doc, setDoc, getDocs } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js";
import {db} from "./registroConect.js";

class Usuario{
  constructor(nombre,correo,usuario,password){
    this.nombre = nombre;
    this.correo = correo;
    this.usuario = usuario;
    this.password = password;
  }
  async addDataCollection(){
    let result = await setDoc(doc(db, "users",this.correo), 
    {   nombre: this.nombre,
        correo: this.correo,
        usuario: this.usuario,
        password: this.password
    });
    console.log("Document written");
  }
  async getDataCollection() {
      const usuarios = collection(db, 'users');
      const resultado = await getDocs(usuarios);
      const list = resultado.docs.map(doc => doc.data());
      console.log('see list ===>', list)
      return list;
    }
}
const usuarioForm = document.getElementById('formulario__register');
usuarioForm.addEventListener('submit', async(e) => { 
    e.preventDefault();
    const nombre = usuarioForm['name'].value;
    const correo = usuarioForm['email1'].value;
    const usuario = usuarioForm['user'].value;
    const password = usuarioForm['password2'].value;
    let user = new Usuario(nombre,correo,usuario,password);
    user.getDataCollection();
    await user.addDataCollection();
    window.location.reload();
});
