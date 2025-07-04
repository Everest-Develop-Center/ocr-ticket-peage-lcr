## OCR API - LCR péage routier

Cette solution API met à disposition une route qui permet d'extraire le numéro d'un ticket de péage à partir d'une image
Les extensions autorisées sont les suivantes : 
- png
- jpeg et,
- jpg

### Usage

La dernière version est 1.0 disponible sur docker hub sous le nom 
everest17/api-ocr-lcr-peage:1.0

Pour lancer le conteneur faite la commande suivante : 

```commandline 
docker run -d -v {VOTRE_VOLUME}:storage -p {VOTRE_PORT}:8000 everest17/api-ocr-lcr-peage:1.0
```

Pour consommer l'api

Il vous faut le bearer token suivant : 
``` 
bWKoGqmjDBy9UPmJ2dtD7a97X4i6lbYrFecsE2GCMuLFMKLiGABbIO8KEiQ1Gey6
```

```commandline
 curl -X POST http://{votre_serveur}:{votre_port}/retrieve-ticket-number \
  -F "image=@chemin/vers/ton_image.jpg"
 ```