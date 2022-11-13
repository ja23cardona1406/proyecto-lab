 // Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
import { getFirestore } from 'https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCz-NWgnQr-EznnDsUC60_6j0o2d8UBDaE",
  authDomain: "registro-dee63.firebaseapp.com",
  databaseURL: "https://registro-dee63-default-rtdb.firebaseio.com",
  projectId: "registro-dee63",
  storageBucket: "registro-dee63.appspot.com",
  messagingSenderId: "538388442683",
  appId: "1:538388442683:web:ee1df766c68c2965b3361e",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app); // esto sirve para exportar la base de datos


