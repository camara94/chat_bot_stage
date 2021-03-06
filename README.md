# Chat Bot Pour Le Stage

## Installation de Anaconda 20/01/2022

* [https://docs.anaconda.com/anaconda/install/windows/](https://docs.anaconda.com/anaconda/install/windows/)


## Installation de Rasa Python de la version 3.6

* conda create -n rasa-bot python=3.6
* [https://youtu.be/4ewIABo0OkU](https://youtu.be/4ewIABo0OkU)

## Activation de l'environnement Rasa

* activate rasa-bot 

## Installation de Rasa core

* pip install -U --user rasa_core

## le site officiel du framework

ce site, nous permet d'installer spacy et les corpus des differents.

## Le Site Officiel du Framework Spacy usage(consulté le 24/01/2022)

* [https://spacy.io/](https://spacy.io/)
  
## installation

### Installation de Spacy
<pre>
<code>
    pip install -U --user pip setuptools wheel 
    pip install -U --user spacy 
</code>
</pre>

### Corpus

C'est un dictionnaire de mot qui regroupe est un mots et règle d'une langue.

### Installation du Corpus Anglais

<code>python -m spacy download en_core_web_sm </code>

### Installation du Corpus Françaiss

<code>python -m spacy download fr_core_news_sm</code>

## Congigurations de la variable d'environnement

Ajouter aux variables d'**env**,  cette configuration permet de rendre la commande 
<code>rasa</code> disponible globalement dans le pc.<br/>
<code>C:\Users\Christine Gnama\AppData\Roaming\Python\Python38\Scripts</code>

## Creation d'un projet 

* <code>rasa init</code> :
  1. demande l'emplacement du dossier(le lien ou le chenmin complet du dossier)
  2. Lorsqu'on donne le lien du projet il cree tous les fichiers de configurations du dossier.

## Pour entrainer le model il faut: 

* <code>rasa train</code>
  
## Interagir avec le chatbot sur la console 

* <code>rasa shell</code>
  
## Interagir avec le chatbot sur la page HTML personnaliser

* <code>rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"</code>

# Intégrer le chatbot à une page web(consulté le 25/01/2022)

un projet open source se trouvant sur gitHub permettant d'intergré à n'importe quelle souce
[https://github.com/scalableminds/chatroom](https://github.com/scalableminds/chatroom) 

## pour intégrer le chat à n'importe quell site professionnelle
<pre>
<code>
&lt;head&gt; 
  &lt; link  rel =" feuille de style " href =" https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.css " /&gt;
 &lt;/head&gt;
&gl;body&gt;
  &lt;div  class =" chat-container "&gt; &lt;/div&gt;

  &lt; script  src =" https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@master/dist/Chatroom.js "&lt; &lt;;/script&gt;
type de script="texte/javascript"&gt;
    var chatroom = nouvelle fenêtre.Chatroom({
      hôte : "http://localhost:5005",
      titre : "Discuter avec Mike",
      conteneur : document.querySelector(".chat-container"),
      welcomeMessage : "Bonjour, je suis Mike. Comment puis-je vous aider ?",
      reconnaissance vocale : "en-US",
      voiceLang : "en-US"
    });
    chatroom.openChat();
  &lt;/script&gt;
&lt;/body&gt;
</code>
</pre>

## Un exemple de conversation au café (consulté le 26/01/2022)

* [https://www.languefr.net/2018/06/dialogues-en-francais-au-cafe.html?fullpost](https://www.languefr.net/2018/06/dialogues-en-francais-au-cafe.html?fullpost)



## le lien de la documenation du site officiel de Rasa (consulté le 26/01/2022)

* [https://rasa.com/docs/rasa/nlu/components/](https://rasa.com/docs/rasa/nlu/components/)


## Vérification de Quelques Commande Rasa

### Validataion de Modification et format YAML

Commande permettant de verifier si notre code  n'a pas d'erreurs, 
s'il ya l'erreur il affiche les details de l'erreur

* <code>rasa data validate</code>

# Comment lancer une action personnalisée avec Rasa

* <code>rasa run actions</code>
  
## definition de chatbot

* [https://www.imagescreations.fr/qu-est-ce-qu-un-chatbot/](https://www.imagescreations.fr/qu-est-ce-qu-un-chatbot/)

## Configuration de rasa à spacy
pour configurer Spacy on importe le frameWork à travers 
**SpacyNLP** et tous les modules qui va avec à travers ce lien: <br/> 
[https://rasa.com/docs/rasa/tuning-your-model/](https://rasa.com/docs/rasa/tuning-your-model/)


## Accès à son compte dévellopeur Facebook

pour acceder à son compte developer Facebook , il suffit d'ecrire developer Facebook
https://developers.facebook.com/apps/&gt;IDDUCOMPTE&lt;/dashboard/

## Installation ngrok

* [https://ngrok.com/download](https://ngrok.com/download)
  
## Q u'est ce que NGROK

la commande ngrok permet d'acceder aux applications dans les  reseaux locaux. 

## Configuration du chat bot à facebook

pour relier mon chatBot à facebook jai utilisé ce lien
[https://rasa.com/docs/rasa/connectors/facebook-messenger/](https://rasa.com/docs/rasa/connectors/facebook-messenger/)

## pour relancer ngrok il suffit de mettre:  

* <code>ngrok http 5005</code>
  
 et copie l'url en ajoutant ce anpoint à la fin de l'url de **ngrok**:  <code>/webhooks/facebook/webhook</code>

exemple:
* <code>https://4d1d-102-109-10-17.ngrok.io/webhooks/facebook/webhook</code>
  
* apres je viens dans facebook developper au niveau de l'url de rappel et mettre l'url en question puis modifier sur l'url de rappel


## Pour chaque lancement du bot il faut 3 terminal: l'ordre dde lanceent nest pas important

1. <code>rasa run actions</code>: verifier si les actions existent
2. <code>rasa run</code>: pour que le bot sois lancé en local
3. <code>ngrok http 5005</code>
et à la fin de lexecution du terminal ngrok http 5005 je prends l'url en https et ajoute : /webhooks/facebook/webhook

