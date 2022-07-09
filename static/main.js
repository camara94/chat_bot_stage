// @flow
import "@babel/polyfill";
let a = document.createElement("a");
a.href = "https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Modules"
let texte = document.createTextNode("Les Modules en js");
a.appendChild(texte)
document.body.append(a)